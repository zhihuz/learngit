# -*- coding: utf-8 -*-

from libshare.db.table.info import RawInfo
from libshare.mysql.ConnectionPool import Mysql

class RawInfoDB(object):

    def __init__(self):
        self.mysql = Mysql()

    def isExists(self, crawl_url, remark=""):
        """
        @summary: 查看资讯是否存在
        @param crawl_url: str类型, 资讯抓取URL 
        @param remark: str类型, 这里remark用于数据源入口标识
        @return: 存在True, 不存在False
        """
        result = self.query_any({'crawl_url':crawl_url,'remark':remark},attributes=['id'])
        return len(result)>0

    def query(self, info_id, attributes=['title','digest','content','icon','image','author','publish_time','source_website','source_url','crawl_website','crawl_url','keyword','remark','attachment']):
        """
        @summary: 获取单个资讯
        @param info_id: int类型, 资讯id
        @param attributes: list类型, 指定字段
        @return: 返回dict
        """
        result = self.query_any({'id':info_id}, attributes)
        if len(result)==0:
            return {}
        return result[0]

    def insert(self, info):
        """
        @summary: 添加一条资讯
        @param info: RawInfo类型
        @return: 成功返回资讯id, 否则返回-1
        """
        if isinstance(info, RawInfo):
            statement = "insert into raw_info(title,digest,content,icon,image,author,publish_time,source_website,source_url,crawl_website,crawl_url,keyword,remark,attachment) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param = (info.get_title(),info.get_digest(),info.get_content(),info.get_icon(),info.get_image(),info.get_author(),info.get_publish_time(),info.get_source_website(),info.get_source_url(),info.get_crawl_website(),info.get_crawl_url(),info.get_keyword(),info.get_remark(),info.get_attachment())
            print "insert statement: ", statement%param
            recordID = self.mysql.insertOne(statement, param)
            self.mysql.end()
            return recordID
        else:
            return -1
    
    def query_any(self, condition, attributes=['title','digest','content','icon','image','author','publish_time','source_website','source_url','crawl_website','crawl_url','keyword','remark','attachment']):
        """
        @summary: 查询资讯
        @param condition: dict类型, 查询条件, e.g. condition={'title':'标题','author':'作者'}
        @param attributes: list类型, 指定字段输出
        @return: 成功返回list
        """
        statement = 'select '+','.join(attributes)+' from raw_info where '+' and '.join([key+"=%s" for key in condition.keys()])
        result = self.mysql.getAll(statement, condition.values())
        self.mysql.end()
        return result

    def insert_one(self, data):
        """
        @summary: 添加一条资讯
        @param data: dict类型, 资讯信息
        @return: 成功返回资讯id, 否则返回-1
        """
        return self.insert(RawInfo.toObject(data))
