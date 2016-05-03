# -*- coding: utf-8 -*-

import re
from datetime import datetime
from probe import logger
from probe.utils.format_utils import make_unicode, extract_title
from probe.utils.formatter import HtmlFormatter
from probe.crawler.items.info import InfoItem
from probe.crawler.spiders.info_spider import IndustryInfoSpider
#from probe.crawler.configs.auto import chinaev as config


class ChinaevSpider(IndustryInfoSpider):
    """
    @summary: 节能与新能源汽车网爬虫 
    @mark: 继承抽象基类IndustryInfoSpider
    """
    name = "chinaev"                               # 爬虫名称
    #_website = make_unicode(config.source_name)   # 数据源(抓取网站)
    #_config = config.entrance                     # 数据源入口配置 

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
            results = response.xpath("//div[@class='ui-box-content newslist']/ul/li[not(contains(@class,'dotted-line'))]")
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
                # 爬取链接crawl_url
                item['crawl_url'] = "http://www.chinaev.org/DisplayView/Normal/News/"+ul.xpath("./a/@href").extract()[0]
                # 发布时间publish_time 
                publish_time = ul.xpath("./span/text()").extract()[0]
                item['publish_time'] = datetime.strptime(publish_time, "%Y-%m-%d %H:%M:%S")
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
        attr = re.split("=", response.url)
        page = int(attr[-1])
        pages = response.xpath("//div[@class='ep-pages']/a[last()]/@href").extract()[0]
        maxpage = int(re.split("=", pages)[-1])
        #crawlpage = 3
        if page < maxpage:  # if self.crawl_mode == 1 else(crawlpage if crawlpage<maxpage else maxpage)):
            page += 1
            attr[-1] = str(page)
        else:
            logger.info("Get last index page: %s" % response.url)
            return 
        return "=".join(attr)

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
            title = re.split("--", response.xpath("//title/text()").extract()[0])[0].strip()
            # 判断和处理【关键字】标题特殊情况
            item['title'], title_keyword = extract_title(title)
            print item['title'].encode('utf-8')
            # 关键字keyword
            # 若标题中抽取关键字
            if title_keyword != None:
                item['keyword'] += ','+title_keyword
            item['keyword'] = ','.join(set(item['keyword'].split(',')))   # set用于去掉重复关键字
            # 源网站source_website
            if response.xpath("//span[@class='comefrom']/text()").extract():
                item['source_website'] = response.xpath("//span[@class='comefrom']/text()").extract()[0]
            # 资讯摘要digest
            if response.xpath("//p//strong/text()").extract():
                item['digest'] = response.xpath("//p//strong/text()").extract()[0]
            # 资讯内容content
            content = response.xpath("//div[@class='content']").extract()
            item['content'] = HtmlFormatter.format_content(content[0])
            # 资讯配图url
            item['image_urls'] = []
            for img_url in response.xpath("//div[@class='content']//img/@src").extract():
                if re.match("file:.*", img_url):
                    continue
                elif re.match("http.*", img_url):
                    item['image_urls'].append(img_url)
                else:
                    img_url = "http://www.chinaev.org"+img_url
                    item['image_urls'].append(img_url)                
        except Exception, e:
            logger.warning("Warning##{0}##_finish_item##{1}, because of {2}!".format(self.name, item['crawl_url'], e))
        return item
