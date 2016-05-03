# -*- coding: utf-8 -*-

import scrapy

class InfoItem(scrapy.Item):
    """
    @summary: 资讯基本信息
    """
    attributes = ('title','content','publish_time','crawl_url','crawl_website','digest','source_website','source_url','author','icon','image','keyword','remark','attachment')
    # 数据库字段
    # 必要字段
    title = scrapy.Field()                #  标题
    content = scrapy.Field()              #  正文
    publish_time = scrapy.Field()         #  发布时间    
    crawl_website = scrapy.Field()        #  抓取资讯的网站名
    crawl_url = scrapy.Field()            #  抓取资讯的URL
    # 特殊字段
    keyword = scrapy.Field()              #  关键字
    remark = scrapy.Field()               #  备注
    # 非必要字段
    digest = scrapy.Field()               #  摘要
    author = scrapy.Field()               #  作者
    source_website = scrapy.Field()       #  发布资讯发布源
    source_url = scrapy.Field()           #  发布资讯的源URL
    icon = scrapy.Field()                 #  资讯图标
    image = scrapy.Field()                #  附图: 图片1,图片2,...
    attachment = scrapy.Field()           #  附件: 附件1,附件2,...

    # 抓取图片相关
    image_urls = scrapy.Field()           # 图片链接列表
    image_info = scrapy.Field()           # 图片信息列表, 每张图片包含path和url属性, 以及下载状态   

    # 运行参数
    retry_count = 0

    def to_dict(self):
        """
        @summary: 将item对象转为dict类型
        @return: dict类型数据
        """
        data = {}
        for attr in self.attributes:
            data[attr] = self[attr]
        return data
