# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "robot.Kr"
# 抓取网站名
source_name = "Kr"
# 抓取URLs配置
entrance = [
        {'keyword': '早期项目', 'url': "http://36kr.com/asynces/posts/feed_column_more.json?column=starding&b_url_code="},
        {'keyword': 'B轮后',   'url': "http://36kr.com/asynces/posts/feed_column_more.json?column=bplus&b_url_code="},
        {'keyword': '大公司',   'url': "http://36kr.com/asynces/posts/feed_column_more.json?column=company&b_url_code="},
        {'keyword': '资本',    'url': "http://36kr.com/asynces/posts/feed_column_more.json?column=capital&b_url_code="},
        {'keyword': '深度',    'url': "http://36kr.com/asynces/posts/feed_column_more.json?column=deep&b_url_code="},
        {'keyword': '研究',    'url': "http://36kr.com/asynces/posts/feed_column_more.json?column=research&b_url_code="},
]
