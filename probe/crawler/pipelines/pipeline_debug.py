# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DebugPipeline(object):
    def __init__(self):
        self.file = open('debug.txt',mode='w') ##现在写入TXT中，以后接入DB
        pass
    def process_item(self, item, spider):
        self.file.write('\n')
        self.file.write(str(item["crawl_url"]))
        self.file.write('\n')
       	self.file.write(item["title"].encode("utf-8"))
        self.file.write('\n')
        self.file.write(str(item['publish_time']))
        self.file.write('\n')
	self.file.write(item['keyword'].encode('utf-8'))
	self.file.write('\n')
	#if item['author']:
	#	self.file.write(item['author'].encode('utf-8'))
	#	self.file.write('\n')
        #self.file.write(item['content'].encode("utf-8"))
        #self.file.write('\n')
	#if (item['source_website']):
        #	self.file.write(item['source_website'].encode("utf-8"))
       	#	self.file.write('\n')
	#self.file.write(item['digest'].encode('utf-8'))
	#self.file.write('\n')
        return item
