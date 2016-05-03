# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "orgcc"
# 抓取网站名
website = "中国文化艺术网"
# 抓取URLs配置
urls = [
    # 1. 资讯本身包含关键字, 需合并; 
    {'keyword': '艺术品,产业政策', 'url': "http://www.orgcc.com/news/list314.html"},
    {'keyword': '艺术品,国内资讯', 'url': "http://www.orgcc.com/news/list2.html"},
    {'keyword': '艺术品,国际资讯', 'url': "http://www.orgcc.com/news/list318.html"},
    {'keyword': '艺术品,拍卖动态', 'url': "http://www.orgcc.com/news/list32.html"},
    # 其它待定
]

