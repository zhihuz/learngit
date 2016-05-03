# -*- coding: utf-8 -*-

import scrapy

class IndustryInfoItem(scrapy.Item):
    """
    @summary: 行业资讯基本信息
    """
    # 数据库字段
    # 必要字段
    title = scrapy.Field()                #  标题
    content = scrapy.Field()              #  正文
    publish_time = scrapy.Field()         #  发布时间    
    crawl_website = scrapy.Field()        #  抓取资讯的网站名
    crawl_url = scrapy.Field()            #  抓取资讯的URL
    # 非必要字段
    digest = scrapy.Field()               #  摘要
    author = scrapy.Field()               #  作者
    source_website = scrapy.Field()       #  发布资讯发布源
    source_url = scrapy.Field()           #  发布资讯的源URL
    keyword = scrapy.Field()              #  关键字
    icon = scrapy.Field()                 #  资讯图标
    image = scrapy.Field()                #  附图:图片1,图片2,...

    # 抓取图片相关
    # image_path = scrapy.Field()
    image_urls = scrapy.Field()           # 图片链接列表
    image_info = scrapy.Field()           # 图片信息列表, 每张图片包含path和url属性, 以及下载状态   
 
    def to_db_object(self):
        data = {}
        data['title'] = self['title']
        data['digest'] = self['digest']
        data['content'] = self['content']
        data['icon'] = self['icon']
        data['image'] = self['image']
        data['author'] = self['author']
        data['keyword'] = self['keyword']
        data['publish_time'] = self['publish_time']
        data['source_website'] = self['source_website']
        data['source_url'] = self['source_url']
        data['crawl_website'] = self['crawl_website']
        data['crawl_url'] = self['crawl_url']
        return data
