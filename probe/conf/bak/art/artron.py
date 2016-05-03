# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "artron"
# 抓取网站名
website = "雅昌艺术网"
# 抓取URLs配置
urls = [
    # 1. 资讯本身包含关键字; 
    # 2. 有些标题需要分离出来作为一个关键字
    # 例如,【雅昌快讯】雅昌文化集团与蘇富比艺术学院达成战略协议, 雅昌快讯是关键字, 后面是标题
    {'keyword': '艺术品,艺术市场', 'url': "http://news.artron.net/morenews/list728/"},
    {'keyword': '艺术品,媒体关注', 'url': "http://news.artron.net/morenews/list734/"},
    {'keyword': '艺术品,评论', 'url': "http://news.artron.net/morenews/list731/"},
    {'keyword': '艺术品,展览', 'url': "http://news.artron.net/morenews/list732/"},
    {'keyword': '艺术品,雅昌独家', 'url': "http://news.artron.net/morenews/list730/"},
    # 其它待定
]

