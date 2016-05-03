# -*- coding: utf-8 -*-

from libshare.db.table.stock import StockResearch 
from libshare.mysql.ConnectionPool import Mysql

class StockResearchDB(object):
    """
    @summary: 股票研报表单数据库封装
    """
    def __init__(self):
        self.mysql = Mysql()
        self.table = StockResearch.table
        self.columns = StockResearch.columns  

    def isExists(self, crawl_url):
        """
        @summary: 查看研报是否已被抓取
        @param crawl_url: str类型, 抓取URL 
        @return: 存在True, 不存在False
        """
        result = self.query_any({'crawl_url':crawl_url}, attributes=['id'])
        return len(result)>0

    def insert_one(self, data):
        """ 
        @summary: 添加一条股票研报
        @param data: dict类型, 股票研报信息
        @return: 成功返回资讯id, 否则返回-1
        """
        return self.insert(StockResearch.toObject(data)) 

    def insert(self, info):
        """
        @summary: 添加股票研报
        @param info: StockResearch类型, 股票研报对象
        @return: 成功返回记录id, 否则返回-1
        """
        if isinstance(info, StockResearch):
            statement = "insert into "+self.table+"(title,digest,content,publish_time,stock_id,source_website,source_url,crawl_website,crawl_url,attachment_url,author,institution,grade) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param = (info.get_title(),info.get_digest(),info.get_content(),info.get_publish_time(),info.get_source_website(),info.get_source_url(),info.get_crawl_website(),info.    get_crawl_url(),info.get_attachment_url(),info.get_author(),info.get_institution(),info.get_grade()) 
            recordID = self.mysql.insertOne(statement, param)
            print statement%param
            self.mysql.end()
            return recordID
        else:
            return -1

    def query_any(self, condition, attributes=self.columns):
        """
        @summary: 查询股票研报
        @param condition: dict类型, 查询条件, e.g. condition={'title':'标题','author':'作者'}
        @param attributes: list类型, 指定字段输出
        @return: 成功返回list
        """
        statement = 'select '+','.join(attributes)+' from '+self.table+' where '+' and '.join([key+"=%s" for key in condition.keys()])
        result = self.mysql.getAll(statement, condition.values())
        self.mysql.end()
        return result
