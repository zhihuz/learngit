# -*- coding: UTF-8 -*-

from libshare.db.table.stock import Stock
from libshare.mysql.ConnectionPool import Mysql

def requestStocks(stypes=['上证A','深证A'], attributes=['id','full_code','code']):
    """
    @param stock_types: list类型, 市场列表, 包括上证A、深证A
    @param attributes: list类型, 指定获取字段, 注意需包含full_code
    @return: list类型, 股票列表
    """
    attr_list = attributes
    if 'full_code' not in attributes:
        attr_list.append('full_code')
    sdb = StockDB()
    results = []
    for st in stypes:
        if st == '上证A':
            stocks = sdb.query_market('SH', attr_list)
            for st in stocks:
                if st['full_code'].encode("utf-8").startswith('60'):
                    results.append(st)
        if st == '深证A':
            stocks = sdb.query_market('SZ', attr_list)
            for st in stocks:
                if st['full_code'].encode("utf-8").startswith('30') or st['full_code'].encode("utf-8").startswith('00'):
                    results.append(st)
    return results

class StockDB(object):

    def __init__(self):
        self.mysql=Mysql()

    def query_market(self, market, attributes=[]):
        """
        @summary: 获取相应市场股票
        @param market: str类型, 市场缩写(e.g. 'SH','SZ','HK','US')
        @param attributes: list类型, 获取股票相关字段
        @return: 若查询成功, 返回结果集, 否则返回[]
        """
        if len(attributes) == 0:
            attr_list = ["id","name","full_code","code","acronym","market","totals","outstanding","total_assets","liquid_assets","fixed_assets","pd","reps","eps","bvps","reserved","crps","listed_date"]
        else:
            attr_list = attributes
        statement = 'select %s '%(','.join(attr_list)) + ' from stock where market=%s'
        print statement
        result= self.mysql.getAll(statement,(market,))
        self.mysql.end()
        return result


if __name__ == "__main__":
    from probe.db.service.StockDB import requestStocks
    # 股票
    stocks = requestStocks(stypes=['上证A','深证A'], attributes=['full_code'])
    print [str(stk['full_code']) for stk in stocks]
