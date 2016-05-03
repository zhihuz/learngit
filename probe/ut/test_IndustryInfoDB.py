# -*- coding: utf-8 -*-

import datetime
from libshare.db.table.info import IndustryInfo
from libshare.mysql.ConnectionPool import Mysql

if __name__ == "__main__":
    # 测试1: insert函数 
    title = '文章标题'
    digest = '文章摘要'
    content = '文章内容'
    image = 'industry/full/fig1.jpg,industry/full/fig2.jpg'  # 1. 注意路径; 2. 这里有个问题，冗余资讯的图是否要存，然后是否和清理后的资讯存一个地方
    author = '作者名称'
    keyword = '光伏,标签1,标签2,标签3'
    publish_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    source_website = '源网站'
    source_url = 'www.source.com'
    crawl_website = '抓取网站'
    crawl_url = '抓取URL'
    # 资讯保存
    info = IndustryInfo(title, digest, content, image, author, publish_time, source_website, source_url, crawl_website, crawl_url)
    iidb = IndustryInfoDB()
    info_id = iidb.insert(info)
    print 'info_id:',info_id
    # 测试2: query 函数
    print iidb.query(info_id) 
