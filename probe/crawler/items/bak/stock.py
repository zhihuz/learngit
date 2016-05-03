# -*- coding: utf-8 -*-

import scrapy

class NoticeItem(scrapy.Item):
    """
    @summary: 公告基本信息
    """
    # 数据库字段
    # 必要字段
    title = scrapy.Field()                #  标题
    stock_id = scrapy.Field()             #  股票id
    publish_time = scrapy.Field()         #  发布时间
    crawl_website = scrapy.Field()        #  抓取网站名
    crawl_url = scrapy.Field()            #  抓取的URL
    # 非必要字段
    digest = scrapy.Field()               #  摘要
    content = scrapy.Field()              #  内容
    attachment_url = scrapy.Field()       #  附件URL
    source_website = scrapy.Field()       #  源网站名
    source_url = scrapy.Field()           #  源链接

    def to_db_object(self):
        data = {}
        data['title'] = self['title']
        data['stock_id'] = self['stock_id']
        data['publish_time'] = self['publish_time']
        data['attachment_url'] = self['attachment_url']
        data['crawl_website'] = self['crawl_website']
        data['crawl_url'] = self['crawl_url']
        data['digest'] = self['digest']
        return data

class ResearchItem(scrapy.Item):
    """
    @summary: 研报基本信息
    """
    # 数据库字段
    # 必要字段
    title = scrapy.Field()                #  标题
    stock_id = scrapy.Field()             #  股票id
    content = scrapy.Field()              #  正文
    publish_time = scrapy.Field()         #  发布时间
    crawl_website = scrapy.Field()        #  抓取网站的网站 
    crawl_url = scrapy.Field()            #  抓取的URL

    # 非必要字段
    digest = scrapy.Field()               #  摘要
    attachment_url = scrapy.Field()       #  附件URL
    source_website = scrapy.Field()       #  源网站名
    source_url = scrapy.Field()           #  源URL
    author = scrapy.Field()               #  作者(列表,格式:大毛,二毛,小明)
    institution = scrapy.Field()          #  机构名称
    grade = scrapy.Field()                #  评级
