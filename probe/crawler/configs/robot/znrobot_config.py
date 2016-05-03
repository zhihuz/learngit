# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "robot.znrobot"
# 抓取网站名
source_name = "智能机器人"
# 抓取URLs配置
entrance = [
    # 行业新闻
    {'keyword': '机器人,行业新闻,展会动态', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=14"},
    {'keyword': '机器人,行业新闻,国际动态', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=31"},
    {'keyword': '机器人,行业新闻,企业快讯', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=23"},
    {'keyword': '机器人,行业新闻,政策', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=19"},
    # 智能机器人
    {'keyword': '机器人,智能机器人,人工智能', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=22"},
    {'keyword': '机器人,智能机器人,无人驾驶', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=33"},
    {'keyword': '机器人,智能机器人,网络机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=36"},
    {'keyword': '机器人,智能机器人,纳米机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=37"},
    {'keyword': '机器人,智能机器人,服务机器人,餐饮机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=43"},
    {'keyword': '机器人,智能机器人,服务机器人,教育机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=44"},
    {'keyword': '机器人,智能机器人,服务机器人,扫地机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=45"},
    {'keyword': '机器人,智能机器人,服务机器人,娱乐机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=46"},
    {'keyword': '机器人,智能机器人,服务机器人,医疗机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=47"},
    {'keyword': '机器人,智能机器人,服务机器人,无人机', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=48"},
    {'keyword': '机器人,智能机器人,服务机器人,陪伴机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=53"},
    # 工业机器人
    {'keyword': '机器人,工业机器人,农业机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=3"},
    ## 没内容 {'keyword': '机器人,工业机器人,物流机器人,AVG', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=26"},
    {'keyword': '机器人,工业机器人,装配机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=4"},
    {'keyword': '机器人,工业机器人,特种机器人', 'url': "http://www.znrobot.com/portal.php?mod=list&catid=9"},
    # 机器人相关（没内容，待定）
]
