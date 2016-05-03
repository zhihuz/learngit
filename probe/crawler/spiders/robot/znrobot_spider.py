# -*- coding: utf-8 -*-

import re
from datetime import datetime
from probe import logger
from probe.utils.format_utils import make_unicode, extract_title
from probe.utils.formatter import HtmlFormatter
from probe.crawler.items.industry import IndustryInfoItem
from probe.crawler.spiders.info_spider import IndustryInfoSpider
from probe.crawler.items.info import InfoItem


class ZnRobotSpider(IndustryInfoSpider):
    """
    @summary: 智能机器人网站资讯爬虫
    @mark:继承抽象基类IndexSpider
    """
    name = "robot.znrobot"                     # 爬虫名称
   

    def _get_result(self, response):
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
            results = response.xpath("//dl[@class='cl csmz_lb_list']")
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
                # 爬取链接
                item['crawl_url'] = "http://www.znrobot.com/"+ul.xpath("./dt/a/@href").extract()[0]
                # 发布时间publish_time
                publish_time = ul.xpath("./dd/span[@class='xg1']/text()").extract()[0].strip()
                item['publish_time'] = datetime.strptime(publish_time, "%Y-%m-%d %H:%M")

                # 爬取网站
                item['crawl_website'] = self._website
                # 爬取链接
                item['crawl_url'] = "http://www.znrobot.com/"+ul.xpath("./dt/a/@href").extract()[0]
                # # 资讯标题
                # item['title'] = ul.xpath("./dt/a/text()").extract()[0]
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
        # 所有索引仅有一页
        return

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
            title = re.split("-", response.xpath('//meta[@name="keywords"]/@content').extract()[0])[0].strip()
            # 判断和处理【关键字】标题特殊情况
            item['title'], title_keyword = extract_title(title)
            # 关键字keyword
            # 若标题中抽取关键字
            if title_keyword != None:
                item['keyword'] += ','+title_keyword
            keywords = item['keyword'].split(',')
            item['keyword'] = ','.join(list(set(keywords))) # set用于去掉重复关键字
            # 摘要
            item['digest'] = response.xpath('//meta[@name="description"]/@content').extract()[0]
            # 源网站source_website和源链接source_url
            # sourace_url抽取比较多样化,不同网页风格可能不同
            def matchurl(raw_url):
                return re.findall(r"(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",raw_url[0]) if raw_url else [u""]
            raw_source_url = response.xpath('//font[@color="#c0c0c0"]//span[1]//text()').extract() or response.xpath('//font[@color="#c0c0c0"]//span//text()').extract() or response.xpath('//font[@color="#c0c0c0"]//text()').extract() or response.xpath("//font[@color='#C0C0C0']//text()").extract()
            source_url = matchurl(raw_source_url)
            if not source_url:
                raw_source_url = response.xpath('//font[@color="#c0c0c0"]/span[2]/text()').extract()
            source_url = matchurl(raw_source_url)
            item["source_url"] = source_url[0]
            item['source_website'] = u""
            # 提取content
            temp_content = response.xpath("//td[@id='article_content']").extract()[0]
            index = temp_content.find("免责声明")
            content = temp_content[:index]
            item['content'] = HtmlFormatter.format_content(content)
            # 资讯配图url(pipeline处理)
            item['image_urls'] = []
            for img_url in response.xpath("//td[@id='article_content']//img/@src").extract():
                if not img_url.startswith("http"): #以http打头的链接是淘宝店铺二维码,应过滤
                    item['image_urls'].append("http://www.znrobot.com/"+img_url)
        except Exception, e:
            logger.warning("Warning##{0}##_finish_item##{1}, because of {2}!".format(self.name, item['crawl_url'], e))
        return item
