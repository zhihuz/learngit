# -*- coding: utf-8 -*-

# 爬虫名称(运行调度使用)
spider_name = "guangfu_bjx"
# 数据源名称(抓取网站名)
source_name = "北极星太阳能光伏网"
# 数据源入口(抓取URLs配置)
entrance = [
    # 原材料及辅料
    {'keyword': '光伏,原材料,辅料,硅片', 'url': 'http://guangfu.bjx.com.cn/gp/?page=1'},
    {'keyword': '光伏,原材料,辅料,要闻', 'url': 'http://guangfu.bjx.com.cn/ycl/List.aspx?classid=562&page=1'},
    #{'keyword': '光伏,系统工程,发电项目', 'url': 'http://guangfu.bjx.com.cn/fdxm/?page=17'},
]
