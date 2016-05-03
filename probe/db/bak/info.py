# -*- coding: utf-8 -*-

class IndustryInfo(object):
    """
    @summary: 行业资讯 
    """
    def __init__(self, title, digest, content, icon, image, author, publish_time, source_website, source_url, crawl_website, crawl_url):
        self.__title = title                    #  标题
        self.__digest = digest                  #  摘要
        self.__content = content                #  正文
        self.__icon = icon                      #  资讯图标
        self.__image = image                    #  附图:图片1,图片2,...
        self.__author = author                  #  作者
        self.__publish_time = publish_time      #  发布时间
        self.__source_website = source_website  #  发布资讯发布源
        self.__source_url = source_url          #  发布资讯的源URL
        self.__crawl_website = crawl_website    #  抓取资讯的网站名
        self.__crawl_url = crawl_url            #  抓取资讯的URL
    def get_title(self):
        return self.__title
    def get_digest(self):
        return self.__digest
    def get_content(self):
        return self.__content
    def get_icon(self):
        return self.__icon
    def get_image(self):
        return self.__image
    def get_author(self):
        return self.__author
    def get_publish_time(self):
        return self.__publish_time
    def get_source_website(self):
        return self.__source_website
    def get_source_url(self):
        return self.__source_url
    def get_crawl_website(self):
        return self.__crawl_website
    def get_crawl_url(self):
        return self.__crawl_url
    @staticmethod
    def toObject(data):
        return IndustryInfo(data['title'],data['digest'],data['content'],data['icon'],data['image'],data['author'],data['publish_time'],data['source_website'],data['source_url'],data['crawl_website'],data['crawl_url'])


class RawInfo(object):
    """
    @summary: 抓取资讯 
    """
    def __init__(self, title, digest, content, icon, image, author, keyword, publish_time, source_website, source_url, crawl_website, crawl_url, remark, attachment):
        self.__title = title                    #  标题
        self.__digest = digest                  #  摘要
        self.__content = content                #  正文
        self.__icon = icon                      #  资讯图标
        self.__image = image                    #  附图:图片1,图片2,...
        self.__author = author                  #  作者
        self.__keyword = keyword                #  关键字
        self.__publish_time = publish_time      #  发布时间
        self.__source_website = source_website  #  发布资讯发布源
        self.__source_url = source_url          #  发布资讯的源URL
        self.__crawl_website = crawl_website    #  抓取资讯的网站名
        self.__crawl_url = crawl_url            #  抓取资讯的URL
        self.__remark = remark                  #  备注
        self.__attachment = attachment          #  附件:附件1,附件2,...
    def get_title(self):
        return self.__title
    def get_digest(self):
        return self.__digest
    def get_content(self):
        return self.__content
    def get_icon(self):
        return self.__icon
    def get_image(self):
        return self.__image
    def get_author(self):
        return self.__author
    def get_keyword(self):
        return self.__keyword
    def get_publish_time(self):
        return self.__publish_time
    def get_source_website(self):
        return self.__source_website
    def get_source_url(self):
        return self.__source_url
    def get_crawl_website(self):
        return self.__crawl_website
    def get_crawl_url(self):
        return self.__crawl_url
    def get_remark(self):
        return self.__remark
    def get_attachment(self):
        return self.__attachment
    @staticmethod
    def toObject(data):
        return RawInfo(data['title'],data['digest'],data['content'],data['icon'],data['image'],data['author'],data['keyword'],data['publish_time'],data['source_website'],data['source_url'],data['crawl_website'],data['crawl_url'],data['remark'],data['attachment'])


class RawInfoMap(object):
   """
   @summary: 资讯映射关系(从RawInfo到IndustryInfo)
   """
   def __init__(self, raw_id, info_id):
       self.__raw_id = raw_id
       self.__info_id = info_id
   def get_raw_id(self):
       return self.__raw_id
   def get_info_id(self):
       return self.__info_id
