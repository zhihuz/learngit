# -*- coding: utf-8 -*-

import json
from probe import logger
from datetime import datetime
from datetime import timedelta
from abc import ABCMeta, abstractmethod
from scrapy import Spider
from scrapy import Request
from probe.crawler.spiders.base_spider import BaseSpider
from probe.utils.format_utils import make_unicode, make_repr


class IndustryInfoSpider(BaseSpider):
    """
    @summary: 行业资讯爬虫抽象基类
              针对目录页面的数据入口
    """
    # 实现抽象类和接口机制
    __metaclass__ = ABCMeta
    # 成员变量
    # 行业爬虫不需要其他成员变量

    def __init__(self, configs=None, start_time=None, end_time=None, crawl_mode='rt', params={}, *args, **kwargs):
        """
        @summary: 爬虫构造器 
        @param config: 爬虫配置项
        @param start_time: datetime类型, 爬虫抓取数据的起始时间（抓取页面需按时间排序）
        @param end_time: datetime类型, 爬虫抓取数据的终止时间
        @param crawl_mode: str类型, 抓取模式, rt（实时监控)和hist(历史抓取), 默认为实时监控
        @param params: dict类型, 其他配置
        """
        super(IndustryInfoSpider, self).__init__(configs, start_time, end_time, crawl_mode, params, *args, **kwargs)
        # 数据入口
        #if not self.configs:
        #    self.configs = self._config
    # 行业爬虫基类不需要重写其他方法

    #def start_requests(self):
    #    """
    #    @summary:启动爬虫时会首先调用这个方法，子类不需要重构
    #    """
    #    for conf in self.configs:
    #        try:
    #            yield Request(conf['url'], callback = self.parse_index, meta = {'conf':conf, 'page_num':1})
    #        except Exception, e:
    #            logger.warning("Warning##{0}##start_requests##{1}##{2}, because of {3}!".format(self.name, conf['keyword'], conf['url'], e))

    #def parse_index(self, response):
    #    """
    #    @summary: 处理目录页面
    #    @param response: start_requests()方法发送请求所得到响应
    #    @return: list类型, 待爬目录页面的资讯Request列表
    #    @remark: 输入按发布时间排序, 输出按发布时间倒排
    #    """
    #    conf = response.meta['conf']
    #    page_num = response.meta['page_num']
    #    item_list = self._get_result(response, conf)
    #    # 如果目录中没有内容，返回空列表
    #    if not item_list:
    #        return []
    #    has_next_page = True
    #    requests = []
    #    for item in item_list:
    #        if 'publish_time' in item and item['publish_time']:
    #            if item['publish_time'] < self.from_time:
    #                has_next_page = False
    #                continue
    #            elif item['publish_time'] > self.end_time:
    #                continue
    #            req = Request(url=item['crawl_url'], callback=self.parse_page, meta={'item':item}, dont_filter=self.dont_filter)
    #            requests.append(req)
    #    # 如需要翻页, 添加下一页的Request; 否则关闭生成器
    #    if has_next_page and (self.crawl_mode == 'hist' or (self.crawl_mode == 'rt' and page_num < self.page_num)):
    #        next_page = self._next_result_page(response)
    #        if next_page:
    #            requests.append(Request(url=next_page, callback=self.parse_index, meta={'conf':conf, 'page_num':page_num+1}))
    #    return requests

    #def parse_page(self, response):
    #    """
    #    @summary: 处理一个网页
    #    @param:parse_index()方法发送的请求所返回的响应
    #    @return:一个列表，_finish_item()所处理的结果
    #    """
    #    item = response.meta["item"]
    #    del response.meta['item']
    #    if 'retry_times' not in response.meta:
    #        response.meta['retry_times'] = 0
    #    try:
    #        result = self._finish_item(item, response)
    #        return result
    #    except Exception, e:
    #        if response.meta['retry_times'] > self.retry_times:
    #            logger.warning("Warning##{0}##parse_page##{1}, because of {2}!".format(self.name, response.url, e))
    #        else:
    #            return Request(url=response.url, callback=self.parse_page, meta={'item':item, 'retry_times':response.meta['retry_times']+1}, dont_filter=self.dont_filter)
    #    return

    #@abstractmethod
    #def _get_result(self, response):
    #    """         
    #    @summary: 处理目录页面, 从列表中提取资讯信息
    #    @remark: 这里必须获取item的crawl_url和publish_time
    #    @param response: page页面
    #    @param config: 爬虫配置项
    #    @return: crawlers.items.Base或其子类对象列表
    #             这里注意, 返回结果需按publish_time降序排列
    #    """ 
    #    pass

    #@abstractmethod
    #def _next_result_page(self, response):
    #    """
    #    @summary: 抽取下一页目录的URL
    #    @param response: 当前处理的目录页面
    #    @return: 下一页目录的URL
    #    """
    #    pass

    #@abstractmethod
    #def _finish_item(self, item, response):
    #    """
    #    @summary: 处理资讯内容页面
    #              抽取页面属性, 填充item字段
    #    @param item: item对象, 来自self._get_result()
    #    @param response: 当前处理网页
    #    @return: 处理完的item对象或新构造的Request对象
    #    """
    #    pass
