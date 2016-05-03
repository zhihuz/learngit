# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = 'cpca1'
# 抓取网站名
source_name = '全国汽车市场研究会'
# 抓取URLs配置
entrance = [
    {'keyword': '汽车,市场动态', 'url': "http://www.cpca1.org/news.asp?types=news&Page=1"},
    {'keyword': '汽车,政策解读', 'url': "http://www.cpca1.org/news.asp?types=policy&Page=1"},
    {'keyword': '汽车,市场分析', 'url': "http://www.cpca1.org/news.asp?types=topics&Page=1"},
    {'keyword': '汽车,数据', 'url': "http://www.cpca1.org/news.asp?types=news&anid=12&Page=1"},
]
