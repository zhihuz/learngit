# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "env_china5e"
# 抓取网站名
website = "中国能源网"
# 抓取URLs配置
urls = [
    # 每一条新闻前面都是一个关键字, 需要拼接
    # 例如,【节能减排】 行为改变有多难？  节能减排是关键字, 后者是标题
    {'keyword': '环保', 'url': 'http://www.china5e.com/news/energy-conservation/index_1.html'},
    {'keyword': '环保,深度分析', 'url': 'http://www.china5e.com/depth-analysis/energy-conservation/'},
]

