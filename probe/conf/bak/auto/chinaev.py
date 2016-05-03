# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = 'chinaev'
# 抓取网站名
source_name = '节能与新能源汽车网'
# 抓取URLs配置
entrance = [
    {'keyword': '汽车,新能源车,政策,法规', 'url': "http://www.chinaev.org/DisplayView/Normal/News/QueryResult.aspx?1=1&lb=%E6%94%BF%E7%AD%96%E6%B3%95%E8%A7%84&&page=1"},
    {'keyword': '汽车,新能源车,电动汽车,电动车', 'url': "http://www.chinaev.org/DisplayView/Normal/News/QueryResult.aspx?title=&keyWords=&company=&country=&chexing=&lb=%E7%94%B5%E5%8A%A8%E6%B1%BD%E8%BD%A6&&page=1"},
    {'keyword': '汽车,新能源车,天然气汽车', 'url': "http://www.chinaev.org/DisplayView/Normal/News/QueryResult.aspx?title=&keyWords=&company=&country=&chexing=&lb=%E5%A4%A9%E7%84%B6%E6%B0%94%E6%B1%BD%E8%BD%A6&&page=1"},
    {'keyword': '汽车,新能源车,零部件', 'url': "http://www.chinaev.org/DisplayView/Normal/News/QueryResult.aspx?title=&keyWords=&company=&country=&chexing=&lb=%E9%9B%B6%E9%83%A8%E4%BB%B6&&page=1"},
    {'keyword': '汽车,新能源车,基础设施', 'url': "http://www.chinaev.org/DisplayView/Normal/News/QueryResult.aspx?title=&keyWords=&company=&country=&chexing=&lb=%E5%9F%BA%E7%A1%80%E8%AE%BE%E6%96%BD&&page=1"},
]
