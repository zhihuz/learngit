# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "huanbao_bjx"
# 抓取网站名
website = "北极星节能环保网"
# 抓取URLs配置
urls = [
    # 大气治理
    {'keyword': '环保,大气治理,脱硫脱硝', 'url': 'http://huanbao.bjx.com.cn/tlts/'},
    {'keyword': '环保,大气治理,除灰除尘', 'url': 'http://huanbao.bjx.com.cn/chcc/'},
    {'keyword': '环保,大气治理,VOCs', 'url': 'http://huanbao.bjx.com.cn/vocs/'},
    {'keyword': '环保,大气治理,综合', 'url': 'http://huanbao.bjx.com.cn/dqzlzh/'},
    {'keyword': '环保,大气治理,要闻', 'url': 'http://huanbao.bjx.com.cn/dqzl/List/658'},
    {'keyword': '环保,大气治理,市场', 'url': 'http://huanbao.bjx.com.cn/dqzl/List/658/89'}, 
    {'keyword': '环保,大气治理,技术', 'url': 'http://huanbao.bjx.com.cn/dqzl/List/658/88'},
    # 水处理
    {'keyword': '环保,水处理,工业废水', 'url': 'http://huanbao.bjx.com.cn/gyfs/'},
    {'keyword': '环保,水处理,市政污水', 'url': 'http://huanbao.bjx.com.cn/wscl/'},
    {'keyword': '环保,水处理,污泥', 'url': 'http://huanbao.bjx.com.cn/sclwn/'},
    {'keyword': '环保,水处理,综合', 'url': 'http://huanbao.bjx.com.cn/sclzh/'},
    {'keyword': '环保,水处理,要闻', 'url': 'http://huanbao.bjx.com.cn/scl/List/541'},
    {'keyword': '环保,水处理,市场', 'url': 'http://huanbao.bjx.com.cn/scl/List/541/89'},
    {'keyword': '环保,水处理,技术', 'url': 'http://huanbao.bjx.com.cn/scl/List/541/88'},
    # 固废处理
    {'keyword': '环保,固废处理,垃圾处理', 'url': 'http://huanbao.bjx.com.cn/ljcl/'},
    {'keyword': '环保,固废处理,工业固废', 'url': 'http://huanbao.bjx.com.cn/gygf/'},
    {'keyword': '环保,固废处理,危废处置', 'url': 'http://huanbao.bjx.com.cn/wfcz/'},
    {'keyword': '环保,固废处理,综合', 'url': 'http://huanbao.bjx.com.cn/gfclzh/'},
    {'keyword': '环保,固废处理,要闻', 'url': 'http://huanbao.bjx.com.cn/gfcl/List/640'},
    {'keyword': '环保,固废处理,市场', 'url': 'http://huanbao.bjx.com.cn/scl/List/640/89'},
    {'keyword': '环保,固废处理,技术', 'url': 'http://huanbao.bjx.com.cn/scl/List/640/88'},
    # 环境修复 
    {'keyword': '环保,环境修复,土壤修复', 'url': 'http://huanbao.bjx.com.cn/trxf/'},
    {'keyword': '环保,环境修复,场地修复', 'url': 'http://huanbao.bjx.com.cn/cdxf/'},
    {'keyword': '环保,环境修复,流域治理', 'url': 'http://huanbao.bjx.com.cn/lyzl/'},
    {'keyword': '环保,环境修复,综合', 'url': 'http://huanbao.bjx.com.cn/hjxfzh/'},
    {'keyword': '环保,环境修复,要闻', 'url': 'http://huanbao.bjx.com.cn/gfcl/List/669'},
    {'keyword': '环保,环境修复,市场', 'url': 'http://huanbao.bjx.com.cn/scl/List/669/89'},
    {'keyword': '环保,环境修复,技术', 'url': 'http://huanbao.bjx.com.cn/scl/List/669/88'},
    # 节能
    {'keyword': '环保,节能,余热余压', 'url': 'http://huanbao.bjx.com.cn/yryy/'},
    {'keyword': '环保,节能,工业节能', 'url': 'http://huanbao.bjx.com.cn/gyjn/'},
    {'keyword': '环保,节能,合同能源管理', 'url': 'http://huanbao.bjx.com.cn/htnygl/'},
    {'keyword': '环保,节能,综合', 'url': 'http://huanbao.bjx.com.cn/jnzh/'},
    {'keyword': '环保,节能,要闻', 'url': 'http://huanbao.bjx.com.cn/jn/List/535'},
    {'keyword': '环保,节能,市场', 'url': 'http://huanbao.bjx.com.cn/jn/List/535/89'},
    {'keyword': '环保,节能,技术', 'url': 'http://huanbao.bjx.com.cn/jn/List/535/88'},
    # 环境监测
    {'keyword': '环保,环境监测,项目', 'url': 'http://huanbao.bjx.com.cn/xmxx/'},
    {'keyword': '环保,环境监测,数据分析,数据', 'url': 'http://huanbao.bjx.com.cn/sjdq/'},
    {'keyword': '环保,环境监测,行业评论,评论', 'url': 'http://huanbao.bjx.com.cn/hypl/'},
    {'keyword': '环保,环境监测,人物访谈,访谈', 'url': 'http://huanbao.bjx.com.cn/rwft/'},
    ##{'keyword': '环保,环境监测,政策,法规', 'url': 'http://huanbao.bjx.com.cn/zcfg/'},
    {'keyword': '环保,环境监测,技术', 'url': 'http://huanbao.bjx.com.cn/jsqy/'},
    {'keyword': '环保,环境监测,国际资讯', 'url': 'http://huanbao.bjx.com.cn/gjzx/'},
    # 节能环保
    {'keyword': '环保,要闻,新闻', 'url': 'http://huanbao.bjx.com.cn/NewsList'},
    {'keyword': '环保,市场', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=89'},
    {'keyword': '环保,企业', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=76'},
    {'keyword': '环保,企业动态', 'url': 'http://huanbao.bjx.com.cn/ex/CompanyNewsList'},
    ##{'keyword': '环保,政策,法规', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=100'},
    {'keyword': '环保,项目', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=103'},
    {'keyword': '环保,招标', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=79'},
    {'keyword': '环保,访谈', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=121'},
    {'keyword': '环保,国际', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=82'}, 
    {'keyword': '环保,数据', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=111'},
    {'keyword': '环保,技术', 'url': 'http://huanbao.bjx.com.cn/NewsList?id=88'},
    {'keyword': '环保,展会', 'url': 'http://huanbao.bjx.com.cn/Ex/ExhibitionListhyyw'},
]
