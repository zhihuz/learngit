# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "huanbao_inen"
# 抓取网站名
website = "国际节能环保网"
# 抓取URLs配置
urls = [
    # 注意1: 文章中包括关键字,需要合并
    # 注意2: 有些文章是不是防盗链还是什么, 请注意一下: http://huanbao.in-en.com/html/huanbao-2243065.shtml
    # 注意3: 这个网站有点奇怪, 感觉就是北极星的clone
    # 大气治理
    {'keyword': '环保,大气治理,脱硫脱硝', 'url': 'http://huanbao.in-en.com/daqi/tltx/'},
    {'keyword': '环保,大气治理,除灰除尘', 'url': 'http://huanbao.in-en.com/daqi/Ash/'},
    {'keyword': '环保,大气治理,VOCs', 'url': 'http://huanbao.in-en.com/daqi/vocs/'},
    {'keyword': '环保,大气治理,空气净化', 'url': 'http://huanbao.in-en.com/daqi/AirPurifier/'},
    {'keyword': '环保,大气治理,大气监测', 'url': 'http://huanbao.in-en.com/daqi/dqjc/'},
    # 水处理
    {'keyword': '环保,水处理,工业废水', 'url': 'http://huanbao.in-en.com/water/gyfs/'},
    {'keyword': '环保,水处理,市政污水', 'url': 'http://huanbao.in-en.com/water/municipal/'},
    {'keyword': '环保,水处理,污泥', 'url': 'http://huanbao.in-en.com/water/sludge/'},
    # 固废处理
    {'keyword': '环保,固废处理,垃圾处理', 'url': 'http://huanbao.in-en.com/gufei/refuse/'},
    {'keyword': '环保,固废处理,工业固废', 'url': 'http://huanbao.in-en.com/gufei/industry/'},
    {'keyword': '环保,固废处理,危废处置', 'url': 'http://huanbao.in-en.com/gufei/hazardous/'},
    # 环境修复 
    {'keyword': '环保,环境修复,土壤修复', 'url': 'http://huanbao.in-en.com/environment/soil/'},
    {'keyword': '环保,环境修复,场地修复', 'url': 'http://huanbao.in-en.com/environment/cdxf/'},
    {'keyword': '环保,环境修复,流域治理', 'url': 'http://huanbao.in-en.com/environment/valley/'},
    # 节能
    {'keyword': '环保,节能,余热余压', 'url': 'http://huanbao.in-en.com/jieneng/yryy/'},
    {'keyword': '环保,节能,工业节能', 'url': 'http://huanbao.in-en.com/jieneng/gyjn/'},
    #{'keyword': '环保,节能,合同能源管理', 'url': 'http://huanbao.in-en.com/jieneng/htnygl/'},
    # 环境监测
    {'keyword': '环保,环境监测', 'url': 'http://huanbao.in-en.com/jiance/'},
    {'keyword': '环保,环境数据', 'url': 'http://huanbao.in-en.com/data/'},
]
