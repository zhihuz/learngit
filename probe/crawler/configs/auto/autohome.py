# -*- coding: utf-8 -*-

category = 'industry'
# 爬虫名称(调度使用)
spider_name = 'autohome'
# 抓取网站名
source_name = '汽车之家' 
# 抓取URLs配置
entrance = [
    {'keyword': "汽车,行业动态", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=7"},
    {'keyword': "汽车,热点追踪", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=10"},
    {'keyword': "汽车,车闻轶事", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=40"},
    {'keyword': "汽车,国产新车", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=70"},
    {'keyword': "汽车,进口新车", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=71"},
    {'keyword': "汽车,召回碰撞", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=87"},
    {'keyword': "汽车,市场分析", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=114"},
    {'keyword': "汽车,用户调研", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=115"},
    {'keyword': "汽车,高端访谈", 'url': "http://www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page=1&ExcptArtIds=882295,882285,882174&class2Id=135"},
]
