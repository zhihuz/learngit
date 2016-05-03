# -*- coding: utf-8 -*-

import re
from datetime import datetime
from probe import logger
from probe.utils.format_utils import make_unicode, extract_title
from probe.utils.formatter import HtmlFormatter
from probe.crawler.spiders.info_spider import IndustryInfoSpider
from probe.crawler.items.info import InfoItem
import traceback

class RobotChinaSpider(IndustryInfoSpider):

    """
    @summary: 中国机器人网爬虫
    @mark: 继承抽象基类IndustryInfoSpider
    """
    name = "robot.robotchina"                     # 爬虫名称

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
            results = None
            if config['keyword'] in ["机器人,行业资讯","机器人,展会资讯"]:
                results = response.xpath("//div[@id='tab']/ul[@class='zx2ul']/div")
            if config['keyword']== '机器人,企业新闻':
                results=response.xpath("//div[@class='catlist']/ul[@class='s41r']/li")
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
                item['crawl_url'] = ul.xpath("./a/@href").extract()[0]
                # 发布时间publish_time,分别处理
                if config['keyword'] in ["机器人,行业资讯","机器人,展会资讯","机器人,行业专题"]:
                    # 从crawl_url中抽取publish_time,并拼接成标准格式
                    publish_time = item['crawl_url'].split('/')
                    publish_time = publish_time[-3][:-2]+'-'+publish_time[-3][-2:]+'-'+publish_time[-2]
                    item['publish_time'] = datetime.strptime(publish_time, "%Y-%m-%d")
                if config['keyword']=='机器人,企业新闻':
                    publishtime = ul.xpath("./em/text()").extract()[0]
                    item['publish_time'] = datetime.strptime(publishtime, "%Y-%m-%d %H:%M")
                if config['keyword'] == "机器人,新闻人物,访谈":
                    publishtime = ul.xpath("./img/@src")[0].replace("http://www.robot-china.com/file/upload/","").split("/")
                    publishtime = publishtime[0][:4]+"-"+publishtime[0][4:]+"-"+publishtime[1]
                    item['publish_time'] = datetime.strptime(publishtime, "%Y-%m-%d")

                rel.append(item)
            # 根据发布时间排序
            rel.sort(key=lambda d: d['publish_time'], reverse=1)
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
        attr = re.split("-|.html", response.url)
        # 当前所抓取的页码
        page = int(attr[-2])
        # 从目录页中获取的最后一页的页码
        maxpage = response.xpath("//a[@class='page'][last()]/text()").extract()
        if maxpage:
            maxpage = int(maxpage[0])
        else:
            maxpage = 1
        # maxpage = 1
        if page < maxpage:
            page += 1
            attr[-2] = str(page)
        else:
            # 当前页码已达到本次设置的最后一页（不论哪个模式），返回空
            logger.info("Get last index page: %s" % response.url)
            return
        return "-".join(attr[:-1])+".html"

    def _finish_item(self, item, response):
        """
        @summary: 处理资讯内容页面
                  抽取页面属性, 填充item字段
        @param item: item对象, 来自self._get_result()
        @param response: 当前处理网页
        @return: 处理完的item对象或新构造的Request对象
        """
        try:
            # 发布日期，部分格式不标准的需格式化
            if item['keyword'] in [make_unicode("机器人,行业资讯"),make_unicode("机器人,展会资讯"),make_unicode("机器人,行业专题"),make_unicode("机器人,新闻人物,访谈")]:
                # 标题title
                title = re.split("-", response.xpath('//title/text()').extract()[0])[0].strip()
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
                # # 标题title
                # item['title'] = response.xpath('//meta[@name="keywords"]/@content').extract()[0]
                # 源网站source_website和源链接source_url
                item['source_website'] = response.xpath("//ul[@id='plshare']/li[3]/text()").extract()[0][3:].strip()
                item['source_url'] = u""
                # 内容content
                content = response.xpath("//div[@id='content']/div[@id='article']").extract()[0]
                item['content'] = HtmlFormatter.format_content(content)
                # 资讯配图url(pipeline处理)
                item['image_urls'] = []
                for img_url in response.xpath("//div[@id='article']/div/img/@src").extract():
                    if re.match("http.*", img_url):
                        item['image_urls'].append(img_url)
                    else:
                        item['image_urls'].append("http://http://www.robot-china.com/"+img_url)
            if item['keyword'] == make_unicode('机器人,企业新闻'):
                # 标题title
                title = re.split("-", response.xpath("//div[@class='title']").extract()[0])[0].strip()
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
                # # 标题title
                # item['title']=response.xpath("//div[@class='title']").extract()[0]
                # 源网站source_website和源链接source_url
                item['source_website'] = u""
                item['source_url'] = u""
                # 内容content
                content = response.xpath("//div[@id='content']").extract()[0]
                item['content'] = HtmlFormatter.format_content(content)
                # 资讯配图url(pipeline处理)
                item['image_urls'] = []
                for img_url in response.xpath("//div[@id='content']/p/img/@src").extract():
                    if re.match("http.*", img_url):
                        item['image_urls'].append(img_url)
                    else:
                        item['image_urls'].append("http://inhand.robot-china.com/"+img_url)
        except Exception, e:
            logger.warning("Warning##{0}##_finish_item##{1}, because of {2}!".format(self.name, item['crawl_url'], e))
	    traceback.print_exc()
            sys.exit(1)
        return item
