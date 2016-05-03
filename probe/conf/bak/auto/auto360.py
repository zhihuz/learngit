# -*- coding: utf-8 -*-

# 爬虫名称(调度使用)
spider_name = 'auto360'
# 抓取网站名
source_name = "中国汽车资讯中心网"
# 抓取URLs配置
entrance = [
    # 政策法规
    {'keyword': "汽车,政策法规", 'url': "http://www.autochina360.com/news/zhengcebiaozhun/list_24_1.html"},
    # 汽车行业资讯
    {'keyword': "汽车,乘用车", 'url': "http://www.autochina360.com/news/zc/cyc/list_3_1.html"},
    {'keyword': "汽车,商用车", 'url': "http://www.autochina360.com/news/zc/syc/list_4_1.html"},
    {'keyword': "汽车,数据", 'url': "http://www.autochina360.com/news/zc/shujujiance/list_69_1.html"},
    # 零部件
    {'keyword': "汽车,动力总成", 'url': "http://www.autochina360.com/news/lbj/dlzcpf/list_6_1.html"},
    {'keyword': "汽车,底盘系统", 'url': "http://www.autochina360.com/news/lbj/dpxt/list_7_1.html"},
    {'keyword': "汽车,轮胎及材料", 'url': "http://www.autochina360.com/news/lbj/ltjcl/list_8_1.html"},
    {'keyword': "汽车,电子器件",   'url': "http://www.autochina360.com/news/lbj/dzdq/list_9_1.html"},
    {'keyword': "汽车,技术创新", 'url': "http://www.autochina360.com/news/lbj/jishuchuangxin/list_106_1.html"},
    # 售后
    {'keyword': "汽车,汽车维修", 'url': "http://www.autochina360.com/news/hsc/qcwx/list_11_1.html"},
    {'keyword': "汽车,汽车保养", 'url': "http://www.autochina360.com/news/hsc/qcby/list_12_1.html"},
    {'keyword': "汽车,售后服务", 'url': "http://www.autochina360.com/news/hsc/shfw/list_13_1.html"},
    {'keyword': "汽车,汽车用品", 'url': "http://www.autochina360.com/news/hsc/qcyp/list_14_1.html"},
    {'keyword': "汽车,企业召回", 'url': "http://www.autochina360.com/news/hsc/qiyezhaohui/list_107_1.html"},
    # 行业
    {'keyword': "汽车,装备制造", 'url': "http://www.autochina360.com/news/hyfw/zbzz/list_16_1.html"},
    {'keyword': "汽车,汽车物流", 'url': "http://www.autochina360.com/news/hyfw/qcwl/list_17_1.html"},
    {'keyword': "汽车,企业管理", 'url': "http://www.autochina360.com/news/hyfw/qygl/list_18_1.html"},
    {'keyword': "汽车,汽车改装", 'url': "http://www.autochina360.com/news/hyfw/qcgz/list_19_1.html"},
    {'keyword': "汽车,金融服务", 'url': "http://www.autochina360.com/news/hyfw/jrfw/list_20_1.html"},
    {'keyword': "汽车,燃油燃气", 'url': "http://www.autochina360.com/news/hyfw/ryrq/list_21_1.html"},
    # 其它
    {'keyword': "汽车,互联网营销", 'url': "http://www.autochina360.com/news/hulianwangyingxiao/list_29_1.html"},
    {'keyword': "汽车,车联网", 'url': "http://www.autochina360.com/news/chelianwang/list_28_1.html"},
    {'keyword': "汽车,新能源车", 'url': "http://www.autochina360.com/news/xinnenyuan/list_27_1.html"},
    {'keyword': "汽车,产业投资", 'url': "http://www.autochina360.com/news/chanyetouzi/list_23_1.html"},
    {'keyword': "汽车,经销商", 'url': "http://www.autochina360.com/news/jingxiaoshang/list_22_1.html"},
    # 数据
    {'keyword': "汽车,数据新闻", 'url': "http://www.autochina360.com/news/zc/shujujiance/list_69_1.html"},
    {'keyword': "汽车,乘用排行", 'url': "http://www.autochina360.com/information/chengyongchepaixing/list_149_1.html"},
    {'keyword': "汽车,商用车排行", 'url': "http://www.autochina360.com/information/shangyongchepaixing/list_150_1.html"},
    {'keyword': "汽车,零部件排行", 'url': "http://www.autochina360.com/information/lingbujianpaixing/list_151_1.html"},
    {'keyword': "汽车,其它排行", 'url': "http://www.autochina360.com/information/qitapaixing/list_152_1.html"},
    # 工程机械
    {'keyword': "汽车,行业研究", 'url': "http://www.autochina360.com/finance/hangyeyanjiu/list_143_1.html"},
    {'keyword': "汽车,宏观资讯", 'url': "http://www.autochina360.com/finance/hongguanzixun/list_141_1.html"},
    {'keyword': "汽车,行业动态", 'url': "http://www.autochina360.com/cmchina360/xingye/xingyedongtai/list_182_1.html"},
    {'keyword': "汽车,分析评论", 'url': "http://www.autochina360.com/cmchina360/xingye/fenxipinglun/list_183_1.html"},
    {'keyword': "汽车,人物访谈", 'url': "http://www.autochina360.com/cmchina360/xingye/renwufangtan/list_185_1.html"},
    {'keyword': "汽车,二手租赁", 'url': "http://www.autochina360.com/cmchina360/xingye/ershouzulin/list_190_1.html"},
    # 企业动态
    {'keyword': "汽车,整车",   'url': "http://www.autochina360.com/cmchina360/zhengchechangqiyedongtai/list_179_1.html"},
    {'keyword': "汽车,零部件", 'url': "http://www.autochina360.com/cmchina360/lingbujianqiyedongtai/list_180_1.html"},
    {'keyword': "汽车,展会",   'url': "http://www.autochina360.com/cmchina360/zhanhuiluntan/zhanhuixinwen/list_186_1.html"},
]
