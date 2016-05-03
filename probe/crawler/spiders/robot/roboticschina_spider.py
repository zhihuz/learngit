# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta
from scrapy import Request, FormRequest
from probe import logger
from probe.utils.format_utils import make_unicode, extract_title
from probe.utils.formatter import HtmlFormatter
from probe.crawler.items.info import InfoItem
from probe.crawler.spiders.info_spider import IndustryInfoSpider


class RoboticsChinaSpider(IndustryInfoSpider):

    """
    @summary: 机器人网爬虫
    @mark: 继承抽象基类IndustryInfoSpider
    """
    name = "robot.roboticschina"                     # 爬虫名称

    def __init__(self, configs=None, start_time=None, end_time=None, crawl_mode='rt', params={}, *args, **kwargs):
        super(RoboticsChinaSpider, self).__init__(configs, start_time, end_time, crawl_mode, params, *args, **kwargs)
        # 表单数据填充,如果登录名和密码信息比较重要,可以写在安全位置的txt中,代码读取路径或者设为手动输入
        self.formdata = {"formAction": "login",
                         "loginName": "sybil_spider@163.com", #账号需要先行注册,此处可切换其他账号和密码
                         "password": "sybil2016",
                         "rememberMe": "on"}
        # headers填充,伪装成浏览器
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"
        self.headers = {
                        "Referer": "http://www.roboticschina.com/login.do",  #"http://www.roboticschina.com/login.do?_ga=1.35947296.1080796918.1455464735",  #对付防盗链设置, 为跳转来源的url
                        "User-Agent": self.user_agent,
                        "Connection": "keep-alive"
                        #"X-Requested-With": "XMLHttpRequest",
                        #"Cookie": cookie
                        }
        # 需要登陆的起始网页
        self.start_urls = ["http://www.roboticschina.com/login-submit.do"]
        

    def start_requests(self):
        """
        @summary:启动爬虫时会首先调用这个方法(重构了基类里的此方法)，提交表单数据,并模拟登陆
        """
        for i, confurl in enumerate(self.start_urls):
            yield FormRequest(confurl,
                              formdata=self.formdata,
                              callback=self.parse_config,
                              meta={'cookiejar': i},  # cookiejar是为了防止掉线,需要再次登陆
                              headers=self.headers)

    def parse_config(self, response):
        """
        @summary: 登陆后会调用此方法,解析配置文件中entrance里的链接,功能同基类里的start_request方法相同
        @param response:来自start_requests的登陆结果
        @return: 解析结果
        """
        query_count = 0
        conf = None
        try:
            for conf in self.configs['entrance']:
                yield Request(conf['url'],
                              headers=self.headers,
                              callback=self.parse_index,
                              meta={'cookiejar': response.meta['cookiejar'], 'conf': conf})
                query_count += 1
        except Exception, e:
            logger.error("Query No.{0} can't be encoded in {1}, because of {2}!"
                         .format(str(query_count), self.name, e))

    def parse_index(self, response):
        """
        @summary: 处理目录页面
        @param response: start_requests()方法发送请求所得到响应
        @return: list类型, 待爬目录页面的资讯Request列表
        @remark: 输入按时间倒排序
        """
        conf = response.meta['conf']
        cookiejar = response.meta['cookiejar']
        item_list = self._get_result(response)
        del response.meta['conf']
        del response.meta['cookiejar']
        # 如果目录中没有内容，返回空列表
        if not item_list:
            return []
        has_next_page = True
        requests = []
        for item in item_list:
            if 'publish_time' in item and item['publish_time']:
                if item['publish_time'] < self.from_time:
                    has_next_page = False
                    continue
                elif item['publish_time'] > self.end_time:
                    continue
                req = Request(url=item['crawl_url'], callback=self.parse_page, meta={'item': item, 'cookiejar': cookiejar}, dont_filter=self.dont_filter)

                requests.append(req)
        # 如需要翻页, 添加下一页的Request; 否则关闭生成器
        if has_next_page and self._next_result_page(response):
            requests.append(Request(url=self._next_result_page(response), callback=self.parse_index, meta={'conf': conf, 'cookiejar': cookiejar}))
        return requests

    def parse_page(self, response):
        """
        @summary: 处理一个网页
        @param:parse_index()方法发送的请求所返回的响应
        @return:一个列表，_finish_item()所处理的结果
        """
        item = response.meta["item"]
        cookiejar = response.meta['cookiejar']
        del response.meta['item']
        del response.meta['cookiejar']
        try:
            result = self._finish_item(item, response)
            return result
        except Exception, e:
            if item.retry_count > self._retry_times:
                logger.warning("Warning##{0}##parse_page##{1}, because of {2}!".format(self.name, response.url, e))
            else:
                item.retry_count += 1
                return Request(url=response.url, callback=self.parse_page, meta={'item': item, "cookiejar": cookiejar}, dont_filter=self._dont_filter)
        return

    def _get_result(self, response):
        """
        @summary: 处理目录页面, 从列表中提取资讯信息
        @remark: 这里必须获取item的crawl_url和publish_time
        @param response: page页面
        @param config: 爬虫配置项
        @return: crawlers.items.Base或其子类对象列表
        """
        rel = []
        conf = response.meta['conf']
        try:
            results = response.xpath("//div[@class='list_Item graphic clear_Sub']/div[@class='item_Con clear_Sub']")
            if not results:
                logger.warning("Warning##{0}##_get_result, cannot get data from {1}!".format(self.name, config['url']))
                return
            for ul in results:
                item = InfoItem()
                ## 静态配置项
                # (先验)关键字keyword
                # 将配置项转换为unicode, 和爬虫抓取文本类型一致
                keyword_list = ul.xpath("./div[@class='item_Extra_Info']/p/a/text()").extract()
                keyword = set(conf['keyword']+keyword_list)
                item['keyword'] = ",".join(keyword)
                # 备注remark
                # 这里将静态关键字作为url入口标识
                item['remark'] = item['keyword']
                # 抓取网站crawl_website
                item['crawl_website'] = self._website
                ## 目录页面中抽取信息
                # 爬取链接
                item['crawl_url'] = ul.xpath("./h2/a/@href").extract()[0]
                # 发布时间publish_time
                publishtime=ul.xpath("./span[@class='pub_Time']/text()").extract()[0].encode("utf-8")
                temp_time="-".join(re.split("年|月|日",publishtime)[:-1])
                item['publish_time'] = datetime.strptime(temp_time, "%Y-%m-%d")
                rel.append(item)
            # 根据发布时间排序
            rel.sort(key=lambda d:d['publish_time'], reverse=1)
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
        attr = re.split("_|.HTM", response.url)
        # 当前所抓取的页码
        page = int(attr[-2])
        # 从目录页中获取的最后一页的页码
        pages=response.xpath("//div[@class='page_List']/ol[@class='clearfix']/li[last()]/a/text()").extract()[0]
        maxpage = int(pages)
        # maxpage = 1
        if page < maxpage:
            page += 1
            attr[-2] = str(page)
        else:
            # 当前页码已达到本次设置的最后一页（不论哪个模式），返回空
            logger.info("Get last index page: %s" % response.url)
            return
        return "_".join(attr[:-1])+".HTM"

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
            title = re.split("-", response.xpath("//head/title/text()").extract()[0])[0].strip()
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
            source_website = response.xpath('//meta[@name="AUTHOR"]/@content').extract()
            item['source_website'] = source_website[0] if source_website else u""
            item['source_url'] = u""
            # 内容content
            content = ''
            raw_contents = response.xpath("//div[@class='article_Content']/p/text()").extract()
            for temp in raw_contents:
                content += temp
            item['content'] = HtmlFormatter.format_content(content)
            # 资讯配图url(pipeline处理)
            item['image_urls'] = []
            for img_url in response.xpath("//div[@class='article_Content']/p/img/@src").extract():
                if re.match("http.*", img_url):
                    item['image_urls'].append(img_url)
                else:
                    item['image_urls'].append("http://image.roboticschina.com/"+img_url)

        except Exception, e:
            logger.warning("Warning##{0}##_finish_item##{1}, because of {2}!".format(self.name, item['crawl_url'], e))
        return item
