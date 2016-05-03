# -*- coding: utf-8 -*-

import re
from datetime import datetime
from scrapy.exceptions import DropItem
from probe import logger
from probe.crawler.items.info import InfoItem
from probe.utils.format_utils import make_str, make_unicode


class TypeCheckPipeline(object):
    """
    @summary: 类型Item字段类型
    """
    def __init__(self):
        self.head = 'TypeCheckPipeline'

    def process_item(self, item, spider):
        """
        @summary: 对Item字段进行类型检查 
        @param item: Item资讯数据对象
        @param spider: 爬虫对象
        """
        if isinstance(item, InfoItem) == False:
            logger.error("Error##{0}##{1}##item type is not correct!".format(self.head, spider.name))
            raise DropItem("[%s] Item type is not correct (url %s)" % (self.head, item['crawl_url']))
        else:
            for attr in ('title','content','crawl_url','crawl_website','keyword','remark','digest','source_website','source_url','author','icon','image','attachment'):
                if attr in item and isinstance(item[attr], unicode) == False:
                    logger.warning("Warning##{0}##{1}##{2}##{3} type is not unicode".format(self.head, spider.name, item['crawl_url'], attr))
                    item[attr] = make_unicode(item[attr])
            if 'publish_time' in item and isinstance(item['publish_time'], datetime) == False:
                logger.warning("Warning##{0}##{1}##{2}##publish_time type is not datetime".format(self.head, spider.name, item['crawl_url']))
            return item
            
            
class DataCleanPipeline(object):
    """
    @summary: 类型Item字段类型
    """
    def __init__(self):
        self.head = 'DataCleanPipeline'

    def process_item(self, item, spider):
        """
        @summary: 对Item字段进行类型检查 
        @param item: Item资讯数据对象
        @param spider: 爬虫对象
        """
	#######################################################################################################
        #第一种情况，爬取网站名在摘要和关键字中
        #if re.findall(item['crawl_website'], item['digest']):
        #    re.sub(item['crawl_website'], "", item['digest'])
        #    logger.info("INFO##{0}##{1}##Delte crawl_website name from digest".format(self.head, spider.name))
        #if item['crawl_website'] in re.split(',', item['keyword']):
        #    re.sub(item['crawl_website'], "", item['keyword'])
        #    logger.info("INFO##{0}##{1}##Delte crawl_website name from keywords".format(self.head, spider.name))
        
        #用来删除爬去网站名+讯|消息等情况，如北极星太阳能光伏网讯:
        if re.findall(item['crawl_website']+u'.*:', item['content']):
            re.sub(item['crawl_website']+u'.*:', "", item['content'])
            
        #如果一个段落中只有原标题这一句话，删除整个段落
        if re.findall(u'原标题[^\n]?</p>', item['content']): #这里需要使用非贪婪模式
            re.sub(u'<p>[^p]*原标题.*?</p>', "", item['content'])
            logger.info(u"INFO##{0}##{1}##Delete 原标题".format(self.head, spider.name))
        #如果原标题出现在段落中的一部分，删除到\n为止，因为原标题中可能有空格存在
        elif re.findall(u'原标题.*?\n', item['content']): 
            re.sub(u'原标题.*?\n', "", item['content'])
            logger.info(u"INFO##{0}##{1}##Delete 原标题".format(self.head, spider.name))
            
        #出现免责声明直接删除屌整个段落            
        if re.findall(u'免责声明', item['content']):
            re.sub(u'<p>[^p]*免责声明.*?</p>', "", item['content'])
        
        #http://www.china5e.com/news/news-939692-1.html 处理广告链接
        if re.findall(u'详情.*http://', item['content']):
            logger.info(u"INFO##{0}##{1}##Delete Ad url".format(self.head, spider.name))
            #logger.info(re.findall(u'<p>[^<p>]*详情.*http://.*?</p>', item['content'])[0])
            logger.info(re.findall(u'<p>[^p]*详情.*http://.*?</p>', item['content'])[0])
            re.sub(u'<p>[^p]*详情.*http://.*?</p>', "", item['content'])
        
        #http://news.bjx.com.cn/html/20151127/685786.shtml
        if re.findall(u'相关阅读', item['content']):
            logger.info(u"INFO##{0}##{1}##Delete Ad url".format(self.head, spider.name))
            #logger.info(re.findall(u'<p>[^<p>]*详情.*http://.*?</p>', item['content'])[0])
            logger.info(re.findall(u'<p>[^p]*相关阅读.*?</p>', item['content'])[0])
            re.sub(u'<p>[^p]*相关阅读.*?</p>', "", item['content'])
        
        if re.findall(u'更多精彩内容', item['content']):
            logger.info(u"INFO##{0}##{1}##Delete Ad url".format(self.head, spider.name))
            #logger.info(re.findall(u'<p>[^<p>]*详情.*http://.*?</p>', item['content'])[0])
            logger.info(re.findall(u'<p>[^p]*更多精彩内容.*?</p>', item['content'])[0])
            re.sub(u'<p>[^p]*更多精彩内容.*?</p>', "", item['content'])
            
        #http://money.163.com/16/0129/18/BEH4Q70400254R91.html
        #广告多而且复杂，从文章广告开始到div结束全部替换
        if re.findall(u'重点推荐', item['content']):
            logger.info(u"INFO##{0}##{1}##Delete Ad url".format(self.head, spider.name))
            #logger.info(re.findall(u'<p>[^<p>]*详情.*http://.*?</p>', item['content'])[0])
            logger.info(re.findall(u'<p>[^p]*更多精彩内容.*?</div>', item['content'])[0])
            re.sub(u'<p>[^p]*更多精彩内容.*?</p>', "</div>", item['content']) 
        return item



class NormalizePipeline(object):
    """
    @summary: 标准化Item 
    @mark: 原始行业资讯表单包括14个字段(id除外), 其中:
           - 必要字段: title, content, publish_time, crawl_url, crawl_website
           - 特殊字段: keyword, remark
           - 非必要字段: digest, source_website, source_url, author, icon, image, attachment
    """
    def __init__(self):
        self.head = 'NormalizePipeline'

    def process_item(self, item, spider):
        """
        @summary: 标准化处理数据
        @param item: item对象
        @param spider: 爬虫对象
        """
        # 必要字段(除content)
        for attr in ('title', 'publish_time', 'crawl_url', 'crawl_website'):
            if attr not in item or not item[attr]:
                logger.error("[%s] Item of %s lack %s, drop it!" % (self.head, item['crawl_url'], attr))
                raise DropItem("Item lacks key attribute")
        
        # 内容content
        # 特殊情况: 浪潮资讯只有pdf附件, 没有内容
        if 'content' not in item or not item['content']:
            if 'attachment' not in item or not item['attachment']:
                logger.error("[%s] Item of %s lack content, drop it!" % (self.head, item['crawl_url']))
                raise DropItem("Item lacks key attribute") 
            else:
                item['content'] = ''

        # 发布时间转为str
        if isinstance(item['publish_time'],datetime):
            item['publish_time'] = item['publish_time'].strftime('%Y-%m-%d %H:%M:%S')
        # 特殊字段处理
        for attr in ('keyword', 'remark'):
            if attr not in item:
                logger.warning("Can't get keyword and remark from %s" % item['crawl_url'])
                item[attr] = ''
        # 非必要字段处理
        try:
            # 如果摘要不存在, 设定使用内容的前80字作为资讯摘要
            if 'digest' not in item:
                if not item['content']:
                    item['digest'] = ''
                else:
                    item['digest'] = re.sub("<.{1,3}?>", "", item['content'][0:320])
        except Exception, e:
            logger.warning("Can't get digest from %s" % item['crawl_url'])
        # 如果源网站不存在, 设置为抓取网站
        if 'source_website' not in item or item['source_website'] == "":
            item['source_website'] = item['crawl_website']
            item['source_url'] = item['crawl_url']
        else:
            if 'source_url' not in item:
               item['source_url'] = ''
        # 其它字段不存在, 设置为空
        for attr in ('author', 'image', 'icon', 'attachment'):
            if attr not in item:
                item[attr] = ''
        # 将字段由unicode为str
        for attr in item.attributes:
            item[attr] = make_str(item[attr])
        return item


#class StorePipeline(object):
#    """
#    @summary: 将Item存储到数据库
#    """
#    def __init__(self):
#        self.ridb = RawInfoDB()
#        self.head = 'StorePipeline'
#
#    def process_item(self, item, spider):
#        """
#        @summary: 存储数据 
#        """
#        # 生成资讯对象数据
#        info = item.to_dict()
#        # 保存数据库
#        self.ridb.insert(info)
