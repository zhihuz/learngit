#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from probe.db.service.RawInfoDB import RawInfoDB
from libshare.db.table.info import RawInfo
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
    info = RawInfo(title, digest, content, image, author, publish_time, source_website, source_url, crawl_website, crawl_url, keyword)
    ridb = RawInfoDB()
    info_id = ridb.insert(info)
    print 'info_id:', info_id

    # 测试2: insert_one函数
    data = {}
    data['title'] = title+'2'
    data['digest'] = digest
    data['content'] = content
    data['image'] = image
    data['author'] = author
    data['keyword'] = keyword
    data['publish_time'] = publish_time
    data['source_website'] = source_website
    data['source_url'] = source_url
    data['crawl_website'] = crawl_website
    data['crawl_url'] = crawl_url
    info_id = ridb.insert_one(data)
    print 'info_id:',info_id
    
    # 测试3: query函数
    print ridb.query(1) 
    print ridb.query(2)
    print 'aaaaaaaaa: '
    print ridb.query_any({'title':'文章标题','digest':'文章摘要11'})
