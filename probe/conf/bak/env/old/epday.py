# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "epday"
# 抓取网站名
website = "中国环境保护网"
# 抓取URLs配置
urls = [
    # 发布者admin不是作者
    # 资讯中包含关键字
    {'keyword': '环保,行业动态,国内', 'url': 'http://www.epday.com/?action-category-catid-17'},
    {'keyword': '环保,行业动态,国际', 'url': 'http://www.epday.com/?action-category-catid-16'},
    {'keyword': '环保,行业动态,产业', 'url': 'http://www.epday.com/?action-category-catid-18'},
    # {'keyword': '环保,行业动态,评论', 'url': 'http://www.epday.com/?action-category-catid-158'},
]
