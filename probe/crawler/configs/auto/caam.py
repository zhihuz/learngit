# -*- coding: utf-8 -*-

category = 'industry'
# 爬虫名称(调度使用)
spider_name = 'caam'
# 抓取网站名
source_name = '中国汽车工业协会'
# 抓取URLs配置
entrance = [
    {'keyword': '汽车,企业动态,国内', 'url': "http://www.caam.org.cn/newslist/a1-1.html"},
    {'keyword': '汽车,行业动态,国内', 'url': "http://www.caam.org.cn/newslist/a2-1.html"},
    {'keyword': '汽车,企业动态,国际交流', 'url': "http://www.caam.org.cn/newslist/a3-1.html"},
    {'keyword': '汽车,海外', 'url': "http://www.caam.org.cn/newslist/a5-1.html"},
    {'keyword': '汽车,其它', 'url': "http://www.caam.org.cn/newslist/a6-1.html"},
    {'keyword': '汽车,展会', 'url': "http://www.caam.org.cn/newslist/a7-1.html"},
]
