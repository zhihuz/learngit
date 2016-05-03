# -*- coding: utf-8 -*-

from libshare.db.service.base import BaseServiceDB
from libshare.db.table.info import RawInfo

class RawInfoDB(BaseServiceDB):
    """
    @summary: 原始资讯表单
              数据库操作封装
    """
    namelist = RawInfo.namelist  
    table = RawInfo.table 

    def __init__(self):
        """
        @summary: 构造器
        """
        super(RawInfoDB, self).__init__()

    def has(self, crawl_url, remark=""):
        """
        @summary: 查看资讯是否存在
        @param crawl_url: str类型, 资讯抓取URL 
        @param remark: str类型, remark用于数据源入口标识
        @return: 存在True, 不存在False
        """
        result = self.query({'crawl_url':crawl_url}, attributes=['remark'])
        if result:
            return remark in result[0]['remark'].split(":")
        else:
            return False

if __name__=="__main__":
    ridb = RawInfoDB()
    print ridb.has("http://guangfu.bjx.com.cn/news/20160309/714559.shtml", remark="光伏,原材料,辅料,要闻")
