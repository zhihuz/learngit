# -*- coding: utf-8 -*-

import sys
sys.path.append("/home/solosseason")

import re
from datetime import datetime
from probe import logger
from probe.utils.format_utils import make_unicode, extract_title
from probe.utils.formatter import HtmlFormatter
from probe.crawler.items.info import InfoItem
from probe.crawler.spiders.info_spider import IndustryInfoSpider

class PrcsteelSpider(IndustryInfoSpider):
    """
    @summary: 中国钢铁新闻网爬虫
    @mark: 继承抽象基类IndustryInfoSpider
    """
    name = "steel.prcsteel"                     # 爬虫名称

    def _get_result(self, response):       # config在下面定义
        """
        @summary: 处理目录页面, 从列表中提取资讯信息
        @remark: 这里必须获取item的crawl_url和publish_time
        @param response: page页面
        @param config: 爬虫配置项
        @return: crawlers.items.Base或其子类对象列表
        """
        rel = []
        config = response.meta['conf']
        try:
            results = response.xpath("//div[@class='analyse-list f-clrfix']")
            if not results:
                logger.warning("Warning##{0}##_get_result, cannot get data from {1}!".format(self.name, config['url']))
                return
            for ul in results:
                item = InfoItem()
                ## 静态配置项
                # (先验)关键字keyword
                # 将配置项转换为unicode, 和爬虫抓取文本类型一致
                item['keyword'] = make_unicode(config['keyword'])
                # 备注remark
                # 这里将静态关键字作为url入口标识
                item['remark'] = item['keyword']
                # 抓取网站crawl_website
                item['crawl_website'] = self._website
                ## 目录页面中抽取信息
                # 爬取链接,获取的链接为相对链接，需要拼接为完整链接
                item['crawl_url'] = ul.xpath(".//dt/a/@href").extract()[0]
                # 发布时间publish_time
                publish_time = '-'.join(re.findall("[0-9]+",ul.xpath(".//p[@class='author-con']/text()").extract()[0]))
                item['publish_time'] = datetime.strptime(publish_time, "%Y-%m-%d")
                rel.append(item)
            # 根据发布时间排序
            rel.sort(key=lambda d:d['publish_time'], reverse = 1)
        except Exception, e:
            logger.warning("Warning##{0}##_get_result##{1}##{2}, because of {3}!".format(self.name, response.url, item['crawl_url'], e))
        finally:
            return rel

    def _next_result_page(self, response):
        """
        @summary: 获取当前目录页的下一页URL
        @param response: 当前的目录页
        @return: 下一页目录的URL或空值
        """
        # 当前所抓取的页码
        curUrl = response.url
        page = int(re.findall("[0-9]+",curUrl)[0]) / 10 +1
        maxPage = int(response.xpath("//div[@id='m-page']/div[@id='page_bar']/a[last()-2]/text()").extract()[0])
        if page >= maxPage:
            # 当前页码已达到本次设置的最后一页（不论哪个模式），返回空
            logger.info("Get last index page: %s" % response.url)
            return
        return re.sub("[0-9]+",str(page*10),curUrl)

    def _finish_item(self, item, response):
        """
        @summary: 处理资讯内容页面
                  抽取页面属性, 填充item字段
        @param item: item对象, 来自self._get_result()
        @param response: 当前处理网页
        @return: 处理完的item对象或新构造的Request对象
        """
        try:
            # 标题title
            title = re.split("-", response.xpath("//label[@id='infoTitle']/text()").extract()[0].strip())[0]
            # 判断和处理【关键字】标题特殊情况
            item['title'], title_keyword = extract_title(title)
            # 关键字keyword
            # 若标题中抽取关键字
            if title_keyword != None:
                item['keyword'] += ','+title_keyword
            # 若资讯中包含关键字
            # keywords = response.xpath("//div[@class='list_key']//a/text()").extract()
            # if keywords:
            #     keywords.extend(item['keyword'].split(','))
            #     item['keyword'] = ','.join(list(set(keywords))) # set用于去掉重复关键字
            # 源网站source_website和源链接source_url
            item['source_website'] = response.xpath("//label[@id='NewsFrom']/text()").extract()[0]
            item['source_url'] = u""
            # 内容content
            content = response.xpath("//div[@id='infoContent']").extract()[0]
            item['content'] = HtmlFormatter.format_content(content)
            # 资讯配图url(pipeline处理)
            item['image_urls'] = []
            for img_url in response.xpath("//div[@id='infoContent']//img/@src").extract():
                if re.match("http.*", img_url):
                    item['image_urls'].append(img_url)
                else:
                    item['image_urls'] = "http://pub.prcsteel.com/news_html/"+img_url
        except Exception, e:
            logger.warning("Warning##{0}##_finish_item##{1}, because of {2}!".format(self.name, item['crawl_url'], e))
        return item
