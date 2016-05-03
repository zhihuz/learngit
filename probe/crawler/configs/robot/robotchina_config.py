# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "robot.robotchina"
# 抓取网站名
source_name = "中国机器人网"
# 抓取URLs配置
entrance = [
    # 工业机器人
     {'keyword': '机器人,行业资讯', 'url': "http://www.robot-china.com/news/list-937-1.html"},
     #有个别外链
     {'keyword': '机器人,企业新闻', 'url': "http://www.robot-china.com/company/news-htm-page-1.html"},
     {'keyword': '机器人,展会资讯', 'url': "http://www.robot-china.com/news/list-1140-1.html"},
     #索引页没有时间
     # {'keyword': '机器人,行业专题', 'url': "http://www.robot-china.com/zhuanti/list-187-1.html"},
     #只有三条数据，而且无法提取时间
     #{'keyword': '机器人,新闻人物,访谈', 'url': "http://www.robot-china.com/news/#newsrw"},
]
