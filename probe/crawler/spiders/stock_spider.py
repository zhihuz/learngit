# -*- coding: utf-8 -*-

import urllib
from datetime import datetime
from datetime import timedelta
from abc import ABCMeta, abstractmethod
from scrapy import Spider
from scrapy import Request
from probe.crawler.spiders.base_spider import BaseSpider
from probe.utils.format_utils import make_unicode, make_repr, make_str 
from probe import logger
#from probe.crawler.settings import PAGE_NUM, RETRY_TIMES     

class StockInfoSpider(BaseSpider):
    """
    @summary: 股票爬虫抽象基类
              针对目录页面的数据入口
    """
    # 实现抽象类和接口机制
    __metaclass__ = ABCMeta
    # 成员变量
    _base_url = ""       # 数据源入口基地址

    def __init__(self, configs=None, start_time=None, end_time=None, crawl_mode='rt', params={}, *args, **kwargs):
        """
        @summary: 构造器
        @param full_code: 股票完整代码
        @param start_time: 爬取起始时间, 抓取start_time之后的页面资讯
        @param end_time: 抓取结束时间, 抓取end_time之前的页面资讯
        @param crawl_mode: 爬虫抓取模式, 包括实时监控rt, 历史抓取hist
        @param params: dict类型, 其他配置参数
        """
        super(StockInfoSpider, self).__init__(configs, start_time, end_time, crawl_mode, params, *args, **kwargs)        
        # 股票代码
        ## 这部分代码放到调度器里        
        #if not self.configs:
        #   self.configs = [str(stk['full_code']) for stk in requestStocks(stypes=['上证A','深证A'], attributes=['full_code'])]
        self.stock_code = {}
        for full_code in self.configs['entrance']:
            self.stock_code[full_code] = full_code.split('.')[0]
        # 转为unicode
        self._keyword = make_unicode(self.configs['keyword'])   
        # 防止url转义
        self._base_url = make_repr(make_str(self.configs['base_url']))
        print self.configs, self._keyword, self._base_url, self.from_time, self.end_time, self.crawl_mode, self.retry_times, self.page_num, self.dont_filter, self._website

    # 股票爬虫基类只需要重构start_requests方法
    def start_requests(self):
        """
        @summary: 开始请求, 启动爬虫首先调用该方法
        @mark: 有特殊需求的爬虫需要重构该方法
        """
        
        for full_code in self.configs['entrance']:
            url = self._base_url.format(urllib.quote(self.stock_code[full_code].encode(self._encoding)))
            try:
                yield Request(url, self.parse_index, meta={'conf':full_code, 'page_num':1})
            except Exception, e:
                logger.warning("Warning##{0}##start_requests##{1}##{2}, because of {3}!".format(self.name, full_code, url, e))
                # 用utf8出现异常的时候再尝试用gbk
                yield Request(self._base_url.format(self.stock_code[full_code].encode("gbk")), self.parse_index, meta={'conf':full_code, 'page_num':1})


    #def parse_index(self, response):
    #    """
    #    @summary: 处理目录页面，返回指向待爬取网页的Request列表
    #    @param response:start_requests()方法发送的请求所返回的响应
    #    @return:list型, 结果包含目录页每篇新闻的url和时间，按时间倒序排列
    #    """
    #    requests = []
    #    if 'retry' not in response.meta:
    #        response.meta['retry'] = 0

    #    full_code = response.meta['conf']
    #    page_num = response.meta['page_num']
    #    print 'page_num: ', page_num
    #    try:
    #        item_list = self._get_result(response)
    #        # 如果目录中没有内容，返回空列表
    #        if not item_list:
    #            return requests
    #        next_page = True  # 目录是否需要翻页
    #        # 逐条测试从目录中提取的网页列表
    #        for item in item_list:
    #            if 'publish_time' in item and item['publish_time']:
    #                if item['publish_time'] <= self.from_time:  # 网页发布时间早于self.from_time
    #                    next_page = False
    #                    continue
    #                elif item['publish_time'] > self.end_time:  # 网页发布时间晚于self.end_time
    #                    continue
    #                req = Request(url=item['crawl_url'], callback=self.parse_page, meta={'item':item, 'conf':full_code}, dont_filter=self.dont_filter, priority=1)
    #                # 传递已抽取信息
    #                requests.append(req)
    #        # 如需要翻页,添加下一页的Request;否则关闭生成器
    #        if next_page and (self.crawl_mode == 'hist' or (self.crawl_mode == 'rt' and page_num < self.page_num)):
    #            next_page = self._next_result_page(response)
    #            if next_page:
    #                requests.append(Request(next_page, self.parse_index, meta={'conf':full_code, 'page_num':page_num+1}))
    #    except Exception, e:
    #        if response.meta['retry'] > self.retry_times:
    #            logger.warning("Warning##{0}##parse_index##{1}##{2}, because of {3}!".format(self.name, response.meta['conf'], response.url, e))
    #        else:
    #            print 'retry1'
    #            req = Request(url=response.url, callback=self.parse_index, meta={'retry':response.meta['retry']+1, 'conf':response.meta['conf'], 'page_num': page_num}, dont_filter=self.dont_filter)
    #            requests.append(req)
    #            #yield req
    #    return requests

    #def parse_page(self, response):
    #    """
    #    @summary: 处理一个网页
    #    @param: parse_index()方法发送的请求所返回的响应
    #    @return: 一个列表，_finish_item()所处理的结果
    #    """
    #    item = response.meta["item"]
    #    del response.meta['item']
    #    if 'retry' not in response.meta:
    #        response.meta['retry'] = 0
    #    print response.meta['retry'], response.meta['conf']
    #    try:
    #        result = self._finish_item(item, response)
    #        return result
    #    except Exception, e:
    #        if response.meta['retry'] > self.retry_times:
    #        #if item.retry_count > self._retry_times:
    #            logger.warning("Warning##{0}##parse_page##{1}##{2}, because of {3}!".format(self.name, response.meta['conf'], response.url, e))
    #        else:
    #            print 'retry2'
    #            #item.retry_count += 1
    #            req = Request(url=response.url, callback=self.parse_page, meta={'item':item, 'retry':response.meta['retry']+1, 'conf':response.meta['conf']}, dont_filter=self.dont_filter)
    #            return req
    #            #return Request(response.url, self.parse_page)
    #    return


    #@abstractmethod
    #def _get_result(self, response):
    #    """
    #    @summary: 从目录页面中获取资讯列表
    #              至少抽取资讯的url和publish_time
    #    @param response: 目录页面
    #    @return: crawlers.items.Base或其子类对象列表
    #             这里注意, 返回结果需按publish_time降序排列，
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
    #    @summary: 处理单个网页，抽取属性并填充item对象
    #              网页的属性可以从self._get_result()或本函数中提取
    #    @param item: self._get_result()中提取的item对象
    #    @param response: 当前处理网页
    #    @return: 处理完毕的item对象或新构造的Request对象
    #    """
    #    pass

