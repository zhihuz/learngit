# -*- coding: utf-8 -*-
import urllib
import json
from datetime import datetime
from datetime import timedelta
from abc import ABCMeta, abstractmethod
from scrapy import Spider
from scrapy import Request
from probe.utils.format_utils import make_unicode, make_repr 
from probe import logger

class BaseSpider(Spider):
    """
    @summary: 爬虫抽象基类
              针对目录页面的数据入口
    """
    # 实现抽象类和接口机制
    __metaclass__ = ABCMeta
    # 成员变量
    name = ""            # 爬虫名称(运行使用)
    _encoding = "utf8"   # 字符编码, 默认为utf8

    def __init__(self, configs=None, start_time=None, end_time=None, crawl_mode='rt', params={}, *args, **kwargs):
        """
        @summary: 构造器
        @param configs: 初始配置
        @param start_time: 爬取起始时间, 抓取start_time之后的页面资讯
        @param end_time: 抓取结束时间, 抓取end_time之前的页面资讯
        @param crawl_mode: 爬虫抓取模式, 包括实时监控rt, 历史抓取hist
        @param params: dict类型, 其他配置参数
        """
        super(BaseSpider, self).__init__(*args, **kwargs)
        # 初始配置: 行业爬虫是一组entrances, 股票爬虫是一组full_codes
        if configs:
            self.configs = json.loads(configs)
        else:
            self.configs = None
        # 若起始时间未设置, 默认为一年前
        if start_time:
            self.from_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        else:
            self.from_time = datetime.now() - timedelta(days=365) 
        # 若结束时间未设置，默认为当前时刻
        if end_time:
            self.end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        else:
            self.end_time = datetime.now()
        # 抓取模式, 默认为实时监控, 否则为历史抓取
        if crawl_mode == 'hist':
            self.crawl_mode = crawl_mode
        else:
            self.crawl_mode = 'rt'
            self.end_time = datetime.now()
        if params:
            params_dict = json.loads(params)
        else:
            params_dict = {}
        # 其他配置参数，包括重试次数，是否过滤重复url，实时监控时需要检查的页面数等
        self.retry_times = (params_dict['retry_times'] if 'retry_times' in params_dict else 100)
        self.dont_filter = (params_dict['dont_filter'] if 'dont_filter' in params_dict else True)
        self.page_num = (params_dict['page_num'] if 'page_num' in params_dict else 3)
        print 'start:',self.from_time, type(self.from_time), 'end:',self.end_time, type(self.end_time), 'mode:',self.crawl_mode, 'retry:',self.retry_times, type(self.retry_times), 'page:',self.page_num, type(self.page_num), 'filter:',self.dont_filter, type(self.dont_filter)
        # 转为unicode
        self._website = make_unicode(self.configs['source_name'])

    def start_requests(self):
        """
        @summary: 开始请求, 启动爬虫首先调用该方法
        @mark: 股票爬虫需要重构该方法
        """
        
        for config in self.configs['entrance']:
            try:
                print config
                yield Request(config['url'], self.parse_index, meta={'conf':config, 'page_num':1})
            except Exception, e:
                logger.warning("Warning##{0}##start_requests##{1}##{2}, because of {3}!".format(self.name, config['keyword'], config['url'], e))


    def parse_index(self, response):
        """
        @summary: 处理目录页面，返回指向待爬取网页的Request列表
        @param response:start_requests()方法发送的请求所返回的响应
        @return:list型, 结果包含目录页每篇新闻的url和时间，按时间倒序排列
        """
        print response
        requests = []
        if 'retry' not in response.meta:
            response.meta['retry'] = 0

        conf = response.meta['conf']
        page_num = response.meta['page_num']
        try:
            item_list = self._get_result(response)
            # 如果目录中没有内容，返回空列表
            if not item_list:
                return requests

            logger.debug("from {0} scraped {1} items".format(response.url,len(item_list)))
            has_next_page = True  # 目录是否需要翻页
            # 逐条测试从目录中提取的网页列表
            for item in item_list:
                # print "item: ", item
                if 'publish_time' in item and item['publish_time']:
                    if item['publish_time'] < self.from_time:  # 网页发布时间早于self.from_time
                        has_next_page = False
                        continue
                    elif item['publish_time'] > self.end_time:  # 网页发布时间晚于self.end_time
                        continue
                    req = Request(url=item['crawl_url'], callback=self.parse_page, meta={'item':item, 'conf':conf}, dont_filter=self.dont_filter, priority=1)
                    # 传递已抽取信息
                    requests.append(req)
            # 如需要翻页,添加下一页的Request;否则关闭生成器
            if has_next_page and (self.crawl_mode == 'hist' or (self.crawl_mode == 'rt' and page_num < self.page_num)):
                next_page = self._next_result_page(response)
                if next_page:
                    requests.append(Request(next_page, self.parse_index, meta={'conf':conf, 'page_num':page_num+1}))
        except Exception, e:
            if response.meta['retry'] >= self.retry_times:
                logger.warning("Warning##{0}##parse_index##{1}##{2}, because of {3}!".format(self.name, response.meta['conf'], response.url, e))
            else:
                print 'retry1'
                print response.meta['retry']+1, conf, page_num, item_list
                req = Request(url=response.url, callback=self.parse_index, meta={'retry':response.meta['retry']+1, 'conf':conf, 'page_num': page_num}, dont_filter=self.dont_filter)
                requests.append(req)
        return requests

    def parse_page(self, response):
        """
        @summary: 处理一个网页
        @param: parse_index()方法发送的请求所返回的响应
        @return: 一个列表，_finish_item()所处理的结果
        """
        item = response.meta["item"]
        del response.meta['item']
        if 'retry' not in response.meta:
            response.meta['retry'] = 0
        try:
            result = self._finish_item(item, response)
            return result
        except Exception, e:
            if response.meta['retry'] > self.retry_times:
                logger.warning("Warning##{0}##parse_page##{1}##{2}, because of {3}!".format(self.name, response.meta['conf'], response.url, e))
            else:
                print 'retry2', response.meta['conf'], response.meta['retry']
                req = Request(url=response.url, callback=self.parse_page, meta={'item':item, 'retry':response.meta['retry']+1, 'conf':response.meta['conf']}, dont_filter=self.dont_filter)
                return req
        return


    @abstractmethod
    def _get_result(self, response):
        """
        @summary: 从目录页面中获取资讯列表
                  至少抽取资讯的url和publish_time
        @param response: 目录页面
        @return: crawlers.items.Base或其子类对象列表
                 这里注意, 返回结果需按publish_time降序排列，
        """
        pass

    @abstractmethod
    def _next_result_page(self, response):
        """
        @summary: 抽取下一页目录的URL
        @param response: 当前处理的目录页面
        @return: 下一页目录的URL
        """
        pass

    @abstractmethod
    def _finish_item(self, item, response):
        """
        @summary: 处理单个网页，抽取属性并填充item对象
                  网页的属性可以从self._get_result()或本函数中提取
        @param item: self._get_result()中提取的item对象
        @param response: 当前处理网页
        @return: 处理完毕的item对象或新构造的Request对象
        """
        pass


