# -*- coding: utf-8 -*-

# 爬虫名称(运行调度使用)
spider_name = "energy.cpnn"
# 数据源名称(抓取网站名)
source_name = "中国电力新闻网"
# 数据源入口(抓取URLs配置)
entrance = [
    # 
    # 注意1: 第一页url   http://www.cpnn.com.cn/dw/default.htm 
    #        第二页开始  http://www.cpnn.com.cn/dw/default_1.htm
    # 
    # 注意2: 缺少发布时间，每个目录页倒着抓取
    #
    # 注意3: 标题处理函数需要完善, 有类似如下标题, 前半部分抽取作为关键字, 后半部分为标题
    #        数读电网丨18亿元：江津建设坚强智能电网 
    #        "数独电网"加入keyword，"18亿元：江津建设坚强智能电网"为标题
    #    
    {'keyword': '能源,电网', 'url': 'http://www.cpnn.com.cn/dw/default.htm'},
    {'keyword': '能源,发电', 'url': 'http://www.cpnn.com.cn/fdpd/zxun/default.htm'},
    {'keyword': '能源,发电,行业市场', 'url': 'http://www.cpnn.com.cn/fdpd/hysc/default.htm'},
    {'keyword': '能源,发电,数据', 'url': 'http://www.cpnn.com.cn/fdpd/shuj/default.htm'},
    {'keyword': '能源,发电,人物', 'url': 'http://www.cpnn.com.cn/fdpd/renw/default.htm'},
    {'keyword': '能源,电力,科技', 'url': 'http://www.cpnn.com.cn/js/default.htm'},
    {'keyword': '能源,财经', 'url': 'http://www.cpnn.com.cn/dlcj/default.htm'},
    {'keyword': '能源,访谈', 'url': 'http://www.cpnn.com.cn/gdft/default.htm'},
    # 这个链接样式可能跟前面有差别, 每条资讯可能都是 关键字｜标题 的形势
    {'keyword': '能源,电气设备', 'url': 'http://www.cpnn.com.cn/dqztbpd/hyzx/default.html'},
]
#
# 栏目无用: 中电专稿 
#
