# -*- coding: utf-8 -*-

import re
from datetime import datetime
from probe import logger
from probe.utils.format_utils import make_unicode, extract_title
from probe.utils.formatter import HtmlFormatter
from probe.crawler.spiders.info_spider import IndustryInfoSpider
from probe.crawler.items.info import InfoItem
import traceback

class CpngiSpider(IndustryInfoSpider):
    """
    @summary: 智能机器人网站资讯爬虫
    @mark:继承抽象基类IndexSpider
    """
    name = "energy.cnenergy"                     # 爬虫名称


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
            results = response.xpath("//div[@class='main4_left_m1']")[:15]
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
                conf = config['url']
                crawl_url = ul.xpath("./div[@class='main4_left_m1_t']/a/@href").extract()[0]
                if crawl_url.startswith("../../"):
                    item["crawl_url"] = re.sub("(\.+/)+","http://www.cnenergy.org/",crawl_url)
                elif crawl_url.startswith("../"):
                    item["crawl_url"] = re.sub("(\.+/)+",conf[:conf.rfind("/",0,len(conf)-1)+1],crawl_url)
                elif crawl_url.startswith("./"):
                    item["crawl_url"] = re.sub("(\.+/)+",conf,crawl_url)
                # 发布时间publish_time
                item['publish_time'] = datetime.strptime(re.findall("t([0-9]+)_",crawl_url)[0],'%Y%m%d')
                rel.append(item)
            # 根据发布时间排序
            rel.sort(key=lambda d:d['publish_time'], reverse = 1)
        except Exception, e:
            traceback.print_exc()
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
            if not curUrl.endswith("html"):
                return curUrl + "shijian_31.html"
            if curUrl.endswith("shijian_31.html"):
                return curUrl.replace("shijian_31.html","shijian_31_1.html")
            return re.sub("[0-9]+\.html",str(int(re.split("_|\.",curUrl)[-2]) + 1)+".html",curUrl)
        except Exception, e:
            traceback.print_exc()
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
            title = re.split("_", "".join(response.xpath("//div[@class='xltitle']//text()").extract()))[0].strip()
            # 判断和处理【关键字】标题特殊情况
            item['title'], title_keyword = extract_title(title)
            # 关键字keyword
            # 若标题中抽取关键字
            if title_keyword != None:
                item['keyword'] += ','+title_keyword
            keywords = response.xpath("//span[@class='xltimerr']/text()").extract()
            if keywords:
                keywords = keywords[0]
                keywords = keywords.replace(";",",") +"," + item['keyword']
                item['keyword'] = ','.join(list(set(keywords.split(',')))) # set用于去掉重复关键字
            # 摘要
            item['digest'] = u''
            item["source_url"] = u""
            source_website = response.xpath("//span[@class='laiyuan']/span/text()").extract()
            item['source_website'] = source_website[0] if source_website else u""
            # 提取content
            content = response.xpath("//div[@class='xlcontent']/div[@class='TRS_Editor']").extract()[0]
            item['content'] = HtmlFormatter.format_content(content)
            # 资讯配图url(pipeline处理)
            item['image_urls'] = []
            for img_url in response.xpath("//div[@class='xlcontent']//img/@src").extract():
                if img_url.startswith("http"): #以http打头的链接是淘宝店铺二维码,应过滤
                    item['image_urls'].append(img_url)
                else:
                    item['image_urls'].append(item['crawl_url'].replace(item['crawl_url'][item['crawl_url'].rindex("/"):],img_url[1:]))
        except Exception, e:
            traceback.print_exc()
            logger.warning("Warning##{0}##_finish_item##{1}, because of {2}!".format(self.name, item['crawl_url'], e))
        return item
