# -*- coding: utf-8 -*-

# 爬虫名称(运行调度使用)
spider_name = "energy.inewenergy"
# 数据源名称(抓取网站名)
source_name = "能源财经网"
# 数据源入口(抓取URLs配置)
entrance = [
    {'keyword': '能源,新闻', 'url': 'http://www.inewenergy.com/news/list_35_1.html'},
    {'keyword': '能源,公司', 'url': 'http://www.inewenergy.com/news/gongsi/list_15_1.html'},
    {'keyword': '能源,人物', 'url': 'http://www.inewenergy.com/news/renwu/list_18_1.html'},
    {'keyword': '能源,报告', 'url': 'http://www.inewenergy.com/news/hybg/list_27_1.html'},
    {'keyword': '能源,股票', 'url': 'http://www.inewenergy.com/news/zhengquan/list_36_1.html'},
    {'keyword': '能源,政策', 'url': 'http://www.inewenergy.com/news/zhengcefagui/list_43_1.html'},
    {'keyword': '能源,数据', 'url': 'http://www.inewenergy.com/news/shuju/list_50_1.html'},
    {'keyword': '能源,焦点', 'url': 'http://www.inewenergy.com/news/focus/list_51_1.html'},
]
