# -*- coding: utf-8 -*-# 爬虫名称(运行调度使用)spider_name = "pvnews"# 数据源名称(抓取网站名)source_name = "PV News"# 数据源入口(抓取URLs配置)entrance = [    # 注意: 该网站有点特殊,第二页开始为index_2.html    #       入口请自行调整    #{'keyword': '太阳能,光伏,政策', 'url':'http://pvnews.cn/hangyezhengce/index.html'},    {'keyword': '太阳能,光伏,要闻', 'url':'http://pvnews.cn/chanyeyaowen/index.html'},    {'keyword': '太阳能,光伏,企业动态', 'url':'http://pvnews.cn/qiyedongtai/index.html'},    {'keyword': '太阳能,光伏,评论', 'url':'http://pvnews.cn/chanyepinglun/index.html'},    {'keyword': '太阳能,光伏,访谈', 'url':'http://pvnews.cn/renwufangtan/index.html'},    {'keyword': '太阳能,光伏,能源资讯', 'url':'http://pvnews.cn/nengyuanzixun/index.html'},    {'keyword': '太阳能,光伏,技术,百科', 'url':'http://pvnews.cn/hangyebaike/index.html'},    {'keyword': '太阳能,光伏,技术,科技动向', 'url':'http://pvnews.cn/kejiqingbao/index.html'},    {'keyword': '太阳能,光伏,数据', 'url':'http://pvnews.cn/hangqingzoushi/index.html'},    {'keyword': '太阳能,光伏,报道', 'url':'http://pvnews.cn/zhuantibaodao/index.html'},    {'keyword': '太阳能,光伏,上市公司,金融股市', 'url':'http://pvnews.cn/shangshigongsi/index.html'},    {'keyword': '太阳能,光伏,财经', 'url':'http://pvnews.cn/guangfucaijing/index.html'},    {'keyword': '太阳能,光伏,展会', 'url':'http://pvnews.cn/zhanhuituijian/index.html'},    ]