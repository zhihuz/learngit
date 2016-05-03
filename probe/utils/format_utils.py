# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta


def make_unicode(text):
    """
    @summary: 转换为unicode
    """
    if isinstance(text, unicode):
        return text
    else:
        return text.decode('utf-8')


def make_str(text):
    """
    @summary: 转换为str
    """
    if isinstance(text, str):
        return text
    else:
        return text.encode('utf-8')


def make_repr(text):
    """
    @summary: 生成非转移字符串
    """
    return repr(text)[1:-1]


def extract_title(title):
    """
    @summary: 从标题中提取关键字
              针对【关键字】标题的格式处理
    @param title: unicode类型, 标题
    @return: 返回unicode格式处理后的标题和关键字
             若不存在返回标题和None
    """
    utitle = make_unicode(title.strip())
#    result = re.findall(u'【[\s\S]*?】', utitle)
    result = re.match(u'【[\s\S]*?】', utitle)
    if result:
       keyword = result.group()
       utitle = re.sub(keyword, '', utitle)
       keyword = re.sub(u'【|】', '', keyword)
       return utitle, keyword
    else:
       return utitle, None

def cal_datetime(show_time):
    match = re.search(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', show_time)
    if match:
        return datetime.strptime(match.group(), '%Y-%m-%d %H:%M:%S')
    else:
        if u'小时' in show_time:
            hour = int(show_time.split(u'小时')[0])
            return datetime.now() - timedelta(hours=hour)
        elif u'昨天' in show_time:
            match_hour = re.search(r'\d\d:\d\d', show_time)
            if match_hour:
                return datetime.strptime((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d') + ' ' + match_hour.group(), '%Y-%m-%d %H:%M')
            else:
                return datetime.now() - timedelta(days=1)
        elif u'天' in show_time:
            day = int(show_time.split(u'天')[0])
            return datetime.now() - timedelta(days=day)
        elif u'月' in show_time:    
            # 这里注意: 
            # 若crawl_url中可以抽取日期的年份和月份, 如http://www.orgcc.com/news/2015/11/85100.html, 
            # 需要将crawl_url抽取的时间(2015-11)与该函数得到的时间的年和月(e.g.2015-12)比较, 
            # 如果结果相同, 则使用cal_datetime得到的时间作为publish_time, 
            # 否则将crawl_url抽取的时间的最后一天作为publish_time(e.g.2015-11-30 00:00:00)   
            # 暂时先这样做可以吗?
            month = int(show_time.split(u'个月')[0])
            return datetime.now() - timedelta(days=month*30)    # 这里直接按照每个月30天计算, 因为'3个月前'本身就不精确, 所以没有必要再具体计算每个月的天数
        elif u'星期' in show_time:
            week = int(show_time.split(u'个星期')[0])
            return datetime.now() - timedelta(weeks=week)
        elif u'分钟' in show_time:
            minute = int(show_time.split(u'分钟')[0])
            return datetime.now() - timedelta(minutes=minute)
        return


if __name__ == '__main__':
    #import chardet

    a = u'你好'
    b = '你好'
    #print b
    #print type(a),make_unicode(a),type(make_unicode(a))
    print make_unicode(b),type(make_unicode(b))
    #print type(a), type(make_str(a))
    c = '【关键字】标题的格式处理'
    c = u'第二届APEC汽车对话 “新能源汽车推广应用的国际经验”专题研讨会<br/>成功召开'
    print extract_title(c)[0], extract_title(c)[1]
    #print make_repr('dfg\njl\'rrf"vc')
    #print cal_datetime(u'3个星期前')

