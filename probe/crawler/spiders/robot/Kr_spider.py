# -*- coding: utf-8 -*-

import sys
sys.path.append("/home/solosseason")

import re
from datetime import datetime
from probe import logger
from probe.utils.format_utils import make_unicode, extract_title
from probe.utils.formatter import HtmlFormatter
from probe.crawler.spiders.info_spider import IndustryInfoSpider
from probe.crawler.items.info import InfoItem
import json

class KrSpider(IndustryInfoSpider):
    """
    @summary: 智能机器人网站资讯爬虫
    @mark:继承抽象基类IndexSpider
    """
    name = "robot.Kr"       # 爬虫名称
    _urlCode = 0

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
            results = json.loads(response.body)
            if not results:
                logger.warning("Warning##{0}##_get_result, cannot get data from {1}!".format(self.name, config['url']))
                return
            for ul in results['data']['feed_posts']:
                item = InfoItem()
                ## 静态配置项
                # (先验)关键字keyword
                # 将配置项转换为unicode, 和爬虫抓取文本类型一致
                # # 资讯标题
                item['title'] = ul['title']
                item['keyword'] = make_unicode(config['keyword'])
                # 备注remark
                # 这里将静态关键字作为url入口标识
                item['remark'] = item['keyword']
                # 抓取网站crawl_website
                item['crawl_website'] = self._website
                ## 目录页面中抽取信息
                # 爬取链接
                item['crawl_url'] = make_unicode("http://36kr.com/p/{0}.html".format(str(ul['url_code'])))
                # logger.warning(item['crawl_url'])
                # 发布时间publish_time
                publishTime = ul['published_at'].split(".")[0].replace("T"," ")
                item['publish_time'] = datetime.strptime(publishTime, "%Y-%m-%d %H:%M:%S")
                rel.append(item)
            # 根据发布时间排序
            rel.sort(key=lambda d:d['publish_time'], reverse = 1)
            self._urlCode = results['data']['feed_posts'][-1]['url_code']
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
            curUrl = response.url
            nextUrl = curUrl.split("&")[0] +"&b_url_code=" +str(self._urlCode)
            # logger.warning("cur page:"+nextUrl)
            return nextUrl
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
            results = response.xpath("//div/@data-props").extract()[0]
            dataDic = json.loads(results)['data']['post']
            # 关键字
            keyWords = dataDic['display_tag_list']
            keyWords.extend(item['keyword'].split(','))
            item['keyword'] = ','.join(list(set(keyWords)))
            # 摘要
            item['digest'] = dataDic['summary']
            # 源网站source_website和源链接source_url
            item["source_url"] = dataDic['extra']['source_urls'] or u""
            item['source_website'] = u""
            # 提取content
            item['content'] = HtmlFormatter.format_content(dataDic['display_content'])
            # 资讯配图url(pipeline处理)
            item['image_urls'] = dataDic['cover']
        except Exception, e:
            logger.warning("Warning##{0}##_finish_item##{1}, because of {2}!".format(self.name, item['crawl_url'], e))
        return item
