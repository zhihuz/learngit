# -*- coding: utf-8 -*-

# 爬虫名称(运行调度使用)
spider_name = "steel.glinfo"
# 数据源名称(抓取网站名)
source_name = "大宗商品网"
# 数据源入口(抓取URLs配置)
entrance = [
    {'keyword': '综合,钢铁', 'url': 'http://info.glinfo.com/article/p-280------0-0-0-----1.html'},
    {'keyword': '综合,钢铁,热点', 'url': 'http://info.glinfo.com/article/p-281------0-0-0-----1.html'},
    {'keyword': '综合,钢铁,国内经济', 'url': 'http://info.glinfo.com/article/p-282------0-0-0-----1.html'},
    ##{'keyword': '国外', 'url': 'http://info.glinfo.com/article/p-283------0-0-0-----1.html'},
    ##{'keyword': '钢铁,协会动态', 'url': 'http://info.glinfo.com/article/p-284------0-0-0-----1.html'},
    # 与上面样式有一定区别
    {'keyword': '钢铁相关,综合,行业经济', 'url': 'http://info.glinfo.com/article/p-285------0-0-0-----1.html'},
    {'keyword': '钢铁相关,综合,基础建设', 'url': 'http://info.glinfo.com/article/p-286------0-0-0-----1.html'},
    {'keyword': '钢铁相关,基础建设', 'url': 'http://info.glinfo.com/article/p-287------0-0-0-----1.html'},
    ##{'keyword': '投资动态', 'url': 'http://info.glinfo.com/article/p-288------0-0-0-----1.html'},
    {'keyword': '房产,房地产,钢铁下游', 'url': 'http://info.glinfo.com/article/p-290------0-0-0-----1.html'},
    {'keyword': '房产,房地产,钢铁下游', 'url': 'http://info.glinfo.com/article/p-291------0-0-0-----1.html'},
    {'keyword': '房产,房地产,钢铁下游', 'url': 'http://info.glinfo.com/article/p-292------0-0-0-----1.html'},
    {'keyword': '机械,钢铁下游', 'url': 'http://info.glinfo.com/article/p-294------0-0-0-----1.html'},
    ##{'keyword': '装备制造,钢铁下游', 'url': 'http://info.glinfo.com/article/p-295------0-0-0-----1.html'},
    ##{'keyword': '基础件,钢铁下游', 'url': 'http://info.glinfo.com/article/p-296------0-0-0-----1.html'},
    # 汽车行业
    {'keyword': '汽车,钢铁下游', 'url': 'http://info.glinfo.com/article/p-297------0-0-0-----1.html'},
    {'keyword': '汽车,乘用车,钢铁下游', 'url': 'http://info.glinfo.com/article/p-298------0-0-0-----1.html'},
    {'keyword': '汽车,商用车,钢铁下游', 'url': 'http://info.glinfo.com/article/p-299------0-0-0-----1.html'},
    {'keyword': '汽车,零配件,零部件,钢铁下游', 'url': 'http://info.glinfo.com/article/p-300------0-0-0-----1.html'},
    # 造船行业
    {'keyword': '造船,钢铁下游', 'url': 'http://info.glinfo.com/article/p-301------0-0-0-----1.html'},
    {'keyword': '造船,船舶维修,钢铁下游', 'url': 'http://info.glinfo.com/article/p-302------0-0-0-----1.html'},
    {'keyword': '造船,设备配套,钢铁下游', 'url': 'http://info.glinfo.com/article/p-303------0-0-0-----1.html'},
    #
    ##{'keyword': '化工,能源化工', 'url': 'http://info.glinfo.com/article/p-304------0-0-0-----1.html'},
    {'keyword': '石油,钢铁上游', 'url': 'http://info.glinfo.com/article/p-305------0-0-0-----1.html'},
    {'keyword': '煤炭,煤电,钢铁上游', 'url': 'http://info.glinfo.com/article/p-306------0-0-0-----1.html'},
    ##{'keyword': '电力', 'url': 'http://info.glinfo.com/article/p-307------0-0-0-----1.html'},
    {'keyword': '轻工家电,钢铁下游', 'url': 'http://info.glinfo.com/article/p-308------0-0-0-----1.html'},
    {'keyword': '家电,钢铁下游', 'url': 'http://info.glinfo.com/article/p-309------0-0-0-----1.html'},
    ##{'keyword': '轻工', 'url': 'http://info.glinfo.com/article/p-310------0-0-0-----1.html'},
    ##{'keyword': '物流,物流运输', 'url': 'http://info.glinfo.com/article/p-311------0-0-0-----1.html'},
    ##{'keyword': '物流,物流建设', 'url': 'http://info.glinfo.com/article/p-312------0-0-0-----1.html'},
    ##{'keyword': '航运,船运', 'url': 'http://info.glinfo.com/article/p-313------0-0-0-----1.html'},
    {'keyword': '钢铁相关,综合,行业统计', 'url': 'http://info.glinfo.com/article/p-315------0-0-0-----1.html'},
    {'keyword': '钢铁相关,综合,行业聚焦', 'url': 'http://info.glinfo.com/article/p-318------0-0-0-----1.html'},
    {'keyword': '钢铁相关,综合,行业动态', 'url': 'http://info.glinfo.com/article/p-319------0-0-0-----1.html'},
    {'keyword': '钢铁,钢材', 'url': 'http://info.glinfo.com/article/p-326------0-0-0-----1.html'},
    {'keyword': '综合,财经', 'url': 'http://info.glinfo.com/article/p-320------0-0-0-----1.html'},
    {'keyword': '综合,国内', 'url': 'http://info.glinfo.com/article/p-321------0-0-0-----1.html'},
    {'keyword': '综合,国际', 'url': 'http://info.glinfo.com/article/p-322------0-0-0-----1.html'},
    {'keyword': '综合,政策法规', 'url': 'http://info.glinfo.com/article/p-323------0-0-0-----1.html'},
    {'keyword': '综合,财经评论', 'url': 'http://info.glinfo.com/article/p-324------0-0-0-----1.html'},
    {'keyword': '综合,宏观数据', 'url': 'http://info.glinfo.com/article/p-325------0-0-0-----1.html'},
]
"""
@remark: 统计数据需登录(为调研): 276-279, 326-330, 
         ## 资讯基本不更新
"""
