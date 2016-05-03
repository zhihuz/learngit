# -*- coding: utf-8 -*-

import re
from scrapy import Request
from datetime import datetime
from probe import logger
from probe.utils.format_utils import make_unicode, extract_title
from probe.utils.formatter import HtmlFormatter
from probe.crawler.items.info import InfoItem
from probe.crawler.spiders.info_spider import IndustryInfoSpider

class OfWeekSpider(IndustryInfoSpider):

    """
    @summary: 中国高科技行业门户(机器人网)
    @mark: 继承抽象基类IndustryInfoSpider
    """
    name = "robot.ofweek"                     # 爬虫名称

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
            results = response.xpath("//div[@class='list_model']/div")
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
                item['crawl_url'] = ul.xpath("./h3/a/@href").extract()[0]
                # 发布时间publish_time
                publish_time = ul.xpath("./div/span/text()").extract()[-1].replace("|","").strip()
                item['publish_time'] = datetime.strptime(publish_time, "%Y-%m-%d %H:%M")
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
        try:
            attr = re.split("-|.html", response.url)
            # 当前所抓取的页码
            page = int(attr[-2])
            # 从目录页中获取的最后一页的页码
            pagesResult = response.xpath("//div/div[@class='page']/form/a[last()-1]/text()").extract()
            maxpage = (page if pagesResult[0] == u"上一页" else int(pagesResult[0])) if pagesResult else 1
            # maxpage = 2
            if page < maxpage:
                page += 1
                attr[-2] = str(page)
            else:
                # 当前页码已达到本次设置的最后一页（不论哪个模式），返回空
                logger.info("Get last index page: %s" % response.url)
                return
            return "-".join(attr[:-1])+".html"
        except Exception, e:
            logger.warning("Warning##{0}##_next_result_page##{1}, because of {2}!".format(self.name, response.url, e))
            return None

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
            title = re.split("-", response.xpath("//title/text()").extract()[0])[0].strip()
            # 判断和处理【关键字】标题特殊情况
            item['title'], title_keyword = extract_title(title)
            # 关键字keyword
            # 若标题中抽取关键字
            if title_keyword != None:
                item['keyword'] += ','+title_keyword
            # 若资讯中包含关键字
            keywords = response.xpath("//div[@class='list_key']//a/text()").extract()
            if keywords:
                keywords.extend(item['keyword'].split(','))
                item['keyword'] = ','.join(list(set(keywords))) # set用于去掉重复关键字
            # 源网站source_website和源链接source_url
            source_website = response.xpath("//span[@class='laiyuan']/text()").extract()[0]
            source_website = source_website.strip().split(" ")[-1].strip()
            item['source_website'] = u"OFWEEK 机器人网" if source_website == u"来源：" else source_website
            item['source_url'] = u''
            # 摘要
            item['digest'] = response.xpath('//meta[@name="Description"]/@content').extract()[0]
            # 内容content和资讯配图url(pipeline处理)
            item['content'] = u''
            item['image_urls'] = []
            item = Request(url=item['crawl_url'],
                           callback=self.get_content_and_image_urls,
                           meta={'item': item})
        except Exception, e:
            logger.warning("Warning##{0}##_finish_item##{1}, because of {2}!".format(self.name, item['crawl_url'], e))
        return item

    def get_content_and_image_urls(self, response):
        '''
        @summary 获取(多页)资讯以及插图链接,即content和image_urls字段
        @return: item对象
        '''
        item = response.meta["item"]
        del response.meta['item']
        # 获取资讯内容的最大页码
        max_page = response.xpath("//div[@class='page']/a[last()]/text()").extract()
        if max_page:
            maxpage = int(max_page[0])
        else:
            maxpage = 1
        # 当前页面的url
        current_url = response.url
        # 填充content和image_urls字段
        temp_content = response.xpath("//div[@id='articleC']").extract()[0]
        index = temp_content.find(u"网讯：")
        item['content'] += HtmlFormatter.format_content(temp_content[index+3:]) if index!=-1 else HtmlFormatter.format_content(temp_content)
        item['image_urls'].extend(response.xpath("//div[@id='articleC']/p/img/@src").extract())
        # 最大页数为1，则直接返回item，结束次方法
        if maxpage == 1:
            return item
        # 页面url的样式为:  http://robot.ofweek.com/2015-12/ART-8321202-8120-29035051.html
        #                http://robot.ofweek.com/2015-12/ART-8321202-8120-29035051_2.html
        # 若url中无‘_’字符,则该页为第一页
        if '_' not in current_url:
            # 拼接第二页url
            next_url = current_url[:-5] + "_2.html"
            req = Request(next_url,
                          callback=self.get_content_and_image_urls,
                          meta={'item': item},
                          priority=1)
            return req
        # 拼接第2-maxpage页url
        # 若当前页为http://robot.ofweek.com/2015-12/ART-8321202-8120-29035051_10.html
        # 则url_list样式为['http://robot.ofweek.com/2015-12/ART-8321202-8120-29035051', '10', '']
        url_list = re.split('_|.html',current_url)
        # 判断是否到达最后一页
        if int(url_list[1]) < maxpage:
            next_url = url_list[0]+"_%d" % (int(url_list[1])+1)+".html"
            req = Request(next_url,
                          callback=self.get_content_and_image_urls,
                          meta={'item': item},
                          priority=1)
            return req
        return item


