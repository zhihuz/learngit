# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "energytrend"
# 抓取网站名
source_name = "集邦新能源网"
# 抓取URLs配置
entrance = [
    #{'keyword': u'技术',
    #    'url': "http://www.energytrend.cn/solar/list-1.html"},
    {'keyword': '分析评论',
        'url': "http://www.energytrend.cn/research/list-1.html"},
    {'keyword': '专题报道',
        'url': "http://www.energytrend.cn/features/list-0.html"},
    {'keyword': '访谈',
        'url': "http://www.energytrend.cn/interview/list-0.html"},
]
