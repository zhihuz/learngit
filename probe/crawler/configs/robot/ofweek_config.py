# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = "robot.ofweek"
# 抓取网站名
source_name = "机器人网"
# 抓取URLs配置
entrance = [
    # 工业机器人
    {'keyword': '机器人,工业机器人,焊接机器人', 'url': "http://robot.ofweek.com/IND-8321224-hanjiejiqiren-1.html"},
    {'keyword': '机器人,工业机器人,喷涂机器人', 'url': "http://robot.ofweek.com/IND-8321225-pentujiqiren-1.html"},
    {'keyword': '机器人,工业机器人,搬运机器人', 'url': "http://robot.ofweek.com/IND-8321226-banyunjiqiren-1.html"},
    {'keyword': '机器人,工业机器人,装配机器人', 'url': "http://robot.ofweek.com/IND-8321227-zhuangpeijiqiren-1.html"},
    {'keyword': '机器人,工业机器人,切割机器人', 'url': "http://robot.ofweek.com/IND-8321228-qiegejiqiren-1.html"},
    {'keyword': '机器人,工业机器人,其它机器人', 'url': "http://robot.ofweek.com/IND-8321229-qitajiqiren-1.html"},
    {'keyword': '机器人,工业机器人,新闻', 'url': "http://robot.ofweek.com/CAT-8321202-8100-News-1.html"},
    {'keyword': '机器人,工业机器人,新品', 'url': "http://robot.ofweek.com/CAT-8321202-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,工业机器人,市场分析', 'url': "http://robot.ofweek.com/CAT-8321202-8400-MarketResearch-1.html"},
    {'keyword': '机器人,工业机器人,技术应用', 'url': "http://robot.ofweek.com/CAT-8321202-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,工业机器人,应用方案', 'url': "http://robot.ofweek.com/CAT-8321202-8900-Applisolutions-1.html"},
    # 机器人配件
    {'keyword': '机器人,机器人配件,控制器', 'url': "http://robot.ofweek.com/IND-8321214-kongzhiqi-1.html"},
    {'keyword': '机器人,机器人配件,示教盒', 'url': "http://robot.ofweek.com/IND-8321215-shijiaohe-1.html"},
    {'keyword': '机器人,机器人配件,传感器', 'url': "http://robot.ofweek.com/IND-8321216-chuanganqi-1.html"},
    {'keyword': '机器人,机器人配件,伺服电机', 'url': "http://robot.ofweek.com/IND-8321217-sifudianji-1.html"},
    {'keyword': '机器人,机器人配件,减速器', 'url': "http://robot.ofweek.com/IND-8321218-jiansuji-1.html"},
    {'keyword': '机器人,机器人配件,机械本体', 'url': "http://robot.ofweek.com/IND-8321219-jixiebenti-1.html"},
    {'keyword': '机器人,机器人配件,检测设备', 'url': "http://robot.ofweek.com/IND-8321219-jixiebenti-1.html"},
    {'keyword': '机器人,机器人配件,夹具', 'url': "http://robot.ofweek.com/IND-8321221-jiaju-1.html"},
    {'keyword': '机器人,机器人配件,线缆与连接', 'url': "http://robot.ofweek.com/IND-8321222-xianlanyulianjie-1.html"},
    {'keyword': '机器人,机器人配件,气压与液压', 'url': "http://robot.ofweek.com/IND-8321223-qiyeyuyeya-1.html"},
    {'keyword': '机器人,机器人配件,新闻', 'url': "http://robot.ofweek.com/CAT-8321201-8100-News-1.html"},
    {'keyword': '机器人,机器人配件,新品', 'url': "http://robot.ofweek.com/CAT-8321201-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,机器人配件,市场分析', 'url': "http://robot.ofweek.com/CAT-8321201-8400-MarketResearch-1.html"},
    {'keyword': '机器人,机器人配件,技术应用', 'url': "http://robot.ofweek.com/CAT-8321201-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,机器人配件,应用方案', 'url': "http://robot.ofweek.com/CAT-8321201-8900-Applisolutions-1.html"},
    # 服务机器人
    {'keyword': '机器人,服务机器人,保洁机器人', 'url': "http://robot.ofweek.com/IND-8321230-baojiejiqiren-1.html"},
    {'keyword': '机器人,服务机器人,教育机器人', 'url': "http://robot.ofweek.com/IND-8321231-jiaoyujiqiren-1.html"},
    {'keyword': '机器人,服务机器人,医疗机器人', 'url': "http://robot.ofweek.com/IND-8321232-yiliaojiqiren-1.html"},
    {'keyword': '机器人,服务机器人,家用机器人', 'url': "http://robot.ofweek.com/IND-8321233-jiayongjiqiren-1.html"},
    {'keyword': '机器人,服务机器人,服务型机器人', 'url': "http://robot.ofweek.com/IND-8321234-fuwuxingjiqiren-1.html"},
    {'keyword': '机器人,服务机器人,娱乐机器人', 'url': "http://robot.ofweek.com/IND-8321235-yulejiqiren-1.html"},
    {'keyword': '机器人,服务机器人,新闻', 'url': "http://robot.ofweek.com/CAT-8321203-8100-News-1.html"},
    {'keyword': '机器人,服务机器人,新品', 'url': "http://robot.ofweek.com/CAT-8321203-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,服务机器人,市场分析', 'url': "http://robot.ofweek.com/CAT-8321203-8400-MarketResearch-1.html"},
    {'keyword': '机器人,服务机器人,技术应用', 'url': "http://robot.ofweek.com/CAT-8321203-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,服务机器人,应用方案', 'url': "http://robot.ofweek.com/CAT-8321203-8900-Applisolutions-1.html"},
    # 特种机器人
    {'keyword': '机器人,特种机器人,军用机器人', 'url': "http://robot.ofweek.com/IND-8321236-junyongjiqiren-1.html"},
    {'keyword': '机器人,特种机器人,农业机器人', 'url': "http://robot.ofweek.com/IND-8321237-nongyejiqiren-1.html"},
    {'keyword': '机器人,特种机器人,水下机器人', 'url': "http://robot.ofweek.com/IND-8321238-shuixiajiqiren-1.html"},
    {'keyword': '机器人,特种机器人,航天机器人', 'url': "http://robot.ofweek.com/IND-8321239-hangtianjiqiren-1.html"},
    {'keyword': '机器人,特种机器人,空间机器人', 'url': "http://robot.ofweek.com/IND-8321240-kongjianjiqiren-1.html"},
    {'keyword': '机器人,特种机器人,救灾机器人', 'url': "http://robot.ofweek.com/IND-8321241-jiuzaijiqiren-1.html"},
    {'keyword': '机器人,特种机器人,新闻', 'url': "http://robot.ofweek.com/CAT-8321204-8100-News-1.html"},
    {'keyword': '机器人,特种机器人,新品', 'url': "http://robot.ofweek.com/CAT-8321204-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,特种机器人,市场分析', 'url': "http://robot.ofweek.com/CAT-8321204-8400-MarketResearch-1.html"},
    {'keyword': '机器人,特种机器人,技术应用', 'url': "http://robot.ofweek.com/CAT-8321204-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,特种机器人,应用方案', 'url': "http://robot.ofweek.com/CAT-8321204-8900-Applisolutions-1.html"},
    # 工业
    {'keyword': '机器人,工业,新闻', 'url': "http://robot.ofweek.com/CAT-8321207-8100-News-1.html"},
    {'keyword': '机器人,工业,新品', 'url': "http://robot.ofweek.com/CAT-8321207-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,工业,市场分析', 'url': "http://robot.ofweek.com/CAT-8321207-8400-MarketResearch-1.html"},
    {'keyword': '机器人,工业,技术应用', 'url': "http://robot.ofweek.com/CAT-8321207-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,工业,应用方案', 'url': "http://robot.ofweek.com/CAT-8321207-8900-Applisolutions-1.html"},
    # 农业
    {'keyword': '机器人,农业,新闻', 'url': "http://robot.ofweek.com/CAT-8321208-8100-News-1.html"},
    {'keyword': '机器人,农业,新品', 'url': "http://robot.ofweek.com/CAT-8321208-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,农业,市场分析', 'url': "http://robot.ofweek.com/CAT-8321208-8400-MarketResearch-1.html"},
    {'keyword': '机器人,农业,技术应用', 'url': "http://robot.ofweek.com/CAT-8321208-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,农业,应用方案', 'url': "http://robot.ofweek.com/CAT-8321208-8900-Applisolutions-1.html"},
    # 军用
    {'keyword': '机器人,军用,新闻', 'url': "http://robot.ofweek.com/CAT-8321208-8100-News-1.html"},
    {'keyword': '机器人,军用,新品', 'url': "http://robot.ofweek.com/CAT-8321208-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,军用,市场分析', 'url': "http://robot.ofweek.com/CAT-8321208-8400-MarketResearch-1.html"},
    {'keyword': '机器人,军用,技术应用', 'url': "http://robot.ofweek.com/CAT-8321208-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,军用,应用方案', 'url': "http://robot.ofweek.com/CAT-8321208-8900-Applisolutions-1.html"},
    # 民用
    {'keyword': '机器人,民用,新闻', 'url': "http://robot.ofweek.com/CAT-8321208-8100-News-1.html"},
    {'keyword': '机器人,民用,新品', 'url': "http://robot.ofweek.com/CAT-8321208-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,民用,市场分析', 'url': "http://robot.ofweek.com/CAT-8321208-8400-MarketResearch-1.html"},
    {'keyword': '机器人,民用,技术应用', 'url': "http://robot.ofweek.com/CAT-8321208-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,民用,应用方案', 'url': "http://robot.ofweek.com/CAT-8321208-8900-Applisolutions-1.html"},
    # 航空
    {'keyword': '机器人,航空,新闻', 'url': "http://robot.ofweek.com/CAT-8321209-8100-News-1.html"},
    {'keyword': '机器人,航空,新品', 'url': "http://robot.ofweek.com/CAT-8321209-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,航空,市场分析', 'url': "http://robot.ofweek.com/CAT-8321209-8400-MarketResearch-1.html"},
    {'keyword': '机器人,航空,技术应用', 'url': "http://robot.ofweek.com/CAT-8321209-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,航空,应用方案', 'url': "http://robot.ofweek.com/CAT-8321209-8900-Applisolutions-1.html"},
    # 教育
    {'keyword': '机器人,教育,新闻', 'url': "http://robot.ofweek.com/CAT-8321212-8100-News-1.html"},
    {'keyword': '机器人,教育,新品', 'url': "http://robot.ofweek.com/CAT-8321212-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,教育,市场分析', 'url': "http://robot.ofweek.com/CAT-8321212-8400-MarketResearch-1.html"},
    {'keyword': '机器人,教育,技术应用', 'url': "http://robot.ofweek.com/CAT-8321212-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,教育,应用方案', 'url': "http://robot.ofweek.com/CAT-8321212-8900-Applisolutions-1.html"},
    # 服务业
    {'keyword': '机器人,服务业,新闻', 'url': "http://robot.ofweek.com/CAT-8321213-8100-News-1.html"},
    {'keyword': '机器人,服务业,新品', 'url': "http://robot.ofweek.com/CAT-8321213-8200-ProductsInfo-1.html"},
    {'keyword': '机器人,服务业,市场分析', 'url': "http://robot.ofweek.com/CAT-8321213-8400-MarketResearch-1.html"},
    {'keyword': '机器人,服务业,技术应用', 'url': "http://robot.ofweek.com/CAT-8321213-8300-TechnologyApplication-1.html"},
    {'keyword': '机器人,服务业,应用方案', 'url': "http://robot.ofweek.com/CAT-8321213-8900-Applisolutions-1.html"},
    # 其它
    {'keyword': '机器人,访谈', 'url': "http://robot.ofweek.com/CATList-8321200-8600-robot-1.html"},
    {'keyword': '机器人,视点', 'url': "http://robot.ofweek.com/CATList-8321200-8500-robot-1.html"},
]
