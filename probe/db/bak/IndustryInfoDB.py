# -*- coding: utf-8 -*-

from libshare.db.table.info import IndustryInfo
from libshare.mysql.ConnectionPool import Mysql

class IndustryInfoDB(object):

    def __init__(self):
        self.mysql = Mysql()

    def query(self, info_id, attributes=['title','source_website','crawl_website','publish_time','content']):
        """
        @summary: 获取单个资讯
        @param info_id: int类型, 资讯id
        @param attributes: list类型, 指定字段
        @return: 返回dict
        """
        statement = 'select '+','.join(attributes)+' from industry_info where id=%s'
        param = (info_id,)
        result = self.mysql.getOne(statement, param)
        self.mysql.end()
        return result

    def insert(self, info):
        """
        @summary: 添加一条资讯
        @param info: IndustryInfo类型
        @return: 成功返回资讯id, 否则返回-1
        """
        if isinstance(info, IndustryInfo):
            sql = "insert into industry_info(title, digest, content, image, author, publish_time, source_website, source_url, crawl_website, crawl_url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param = (info.get_title(),info.get_digest(),info.get_content(),info.get_image(),info.get_author(),info.get_publish_time(),info.get_source_website(),info.get_source_url(),info.get_crawl_website(),info.get_crawl_url())
            print sql%param
            recordID = self.mysql.insertOne(sql,param)
            self.mysql.end()
            return recordID
        else:
            return -1
