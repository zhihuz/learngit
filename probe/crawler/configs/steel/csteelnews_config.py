# -*- coding: utf-8 -*-

# 爬虫名称(运行调度使用)
spider_name = "steel.csteelnews"
# 数据源名称(抓取网站名)
source_name = "中国钢铁新闻网"
# 数据源入口(抓取URLs配置)
entrance = [
    # 注意: 第二页为index_1.html
    # 
    {'keyword': '钢铁,独家报道', 'url': 'http://www.csteelnews.com/xwzx/djbd/index.html'},
    {'keyword': '钢铁,综合,宏观经济', 'url': 'http://www.csteelnews.com/xwzx/hgjj/index.html'},
    {'keyword': '钢铁,综合,评论', 'url': 'http://www.csteelnews.com/xwzx/zjsd/index.html'},
    {'keyword': '钢铁,行业,行业动态', 'url': 'http://www.csteelnews.com/xwzx/xydt/index.html'},
    {'keyword': '钢铁,国外,海外,国际钢铁', 'url': 'http://www.csteelnews.com/xwzx/gjgt/index.html'},
    {'keyword': '钢铁,原材料,原料耐材', 'url': 'http://www.csteelnews.com/xwzx/ylnc/index.html'},
    {'keyword': '钢铁,装备炼建,装备,炼钢', 'url': 'http://www.csteelnews.com/xwzx/zbyj/index.html'},
    {'keyword': '钢铁,综合,节能减排,环保', 'url': 'http://www.csteelnews.com/xwzx/jnjp/index.html'},
    {'keyword': '钢铁,钢铁下游,下游产业', 'url': 'http://www.csteelnews.com/xwzx/gtyh/index.html'},
    ##{'keyword': '钢铁,图片新闻', 'url': 'http://www.csteelnews.com/xwzx/tpxw/index.html'},
    #
    {'keyword': '钢铁,市场,市场分析', 'url': 'http://www.csteelnews.com/sjzx/scfx/index.html'},
    {'keyword': '钢铁,数据,行业指数', 'url': 'http://www.csteelnews.com/sjzx/hyzs/index.html'},
    # 这个是表单(可视化需要关注),可视化问题目前没有解决
    # {'keyword': '钢铁,数据,市场行情', 'url': 'http://www.csteelnews.com/sjzx/scxq/index.html'},
    {'keyword': '钢铁,技术,冶金技术', 'url': 'http://www.csteelnews.com/sjzx/scfx/index.html'},
    ##{'keyword': '钢铁,展会,会展招标', 'url': 'http://www.csteelnews.com/sjzx/hzzb/index.html'},
    ##{'keyword': '钢铁,政策,政策法规', 'url': 'http://www.csteelnews.com/sjzx/zcfg/index.html'},
    ##{'keyword': '钢铁,数据,钢厂调价', 'url': 'http://www.csteelnews.com/sjzx/gcdj/index.html'},
    ##{'keyword': '钢铁,行业报告', 'url': 'http://www.csteelnews.com/sjzx/xybg/index.html'},
    #
    {'keyword': '钢铁,企业,企业资讯', 'url': 'http://www.csteelnews.com/qypd/qyzx/index.html'},
    ##{'keyword': '钢铁,企业,党建政工', 'url': 'http://www.csteelnews.com/qypd/djzg/index.html'},
    {'keyword': '钢铁,企业,经营管理', 'url': 'http://www.csteelnews.com/qypd/qyzx/index.html'},
    ##{'keyword': '钢铁,企业,生产一线', 'url': 'http://www.csteelnews.com/qypd/scyx/index.html'},
    ##{'keyword': '钢铁,企业,企业文化', 'url': 'http://www.csteelnews.com/qypd/qywh/index.html'},
]
"""
@remark: 统计数据基本不更新 
         ## 内容不合适 
"""
