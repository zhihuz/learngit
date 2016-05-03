# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from probe import logger
from probe.db.service.RawInfoDB import RawInfoDB
from mario.db.service.stock import RawStockNoticeDB, RawStockResearchDB


class NoticeRepeatPipeline(object):
    """
    @summary: 检查Item是否已经抓取
    """
    def __init__(self):
        """
        @summary: 构造器
        """
        self.db = RawStockNoticeDB()
        self.head  = 'NoticeRepeatPipeline'

    def process_item(self, item, spider):
        """
        @summary: 查看资讯是否已抓取
        @mark: 检查crawl_url字段
        @param item: Item资讯数据对象
        @param spider: 爬虫对象
        """
        # 检查字段crawl_url
        if 'crawl_url' not in item or not item['crawl_url']:
            logger.error("[%s] Item lack crawl_url, drop it!" % (self.head))
            raise DropItem("Item lacks key attribute")
        else:
            if self.db.has({'crawl_url':item['crawl_url']}):
                logger.info("[%s] Item of %s has been crawled, drop it!" % (self.head, item['crawl_url']))
                raise DropItem("[%s] Info exists (url %s)" % (self.head, item['crawl_url']))
            else:
                return item


class ResearchRepeatPipeline(object):
    """
    @summary: 检查Item是否已经抓取
    """
    def __init__(self):
        """
        @summary: 构造器
        """
        self.db = RawStockResearchDB()
        self.head  = 'ResearchRepeatPipeline'

    def process_item(self, item, spider):
        """
        @summary: 查看资讯是否已抓取
        @mark: 检查crawl_url字段
        @param item: Item资讯数据对象
        @param spider: 爬虫对象
        """
        # 检查字段crawl_url
        if 'crawl_url' not in item or not item['crawl_url']:
            logger.error("[%s] Item lack crawl_url, drop it!" % (self.head))
            raise DropItem("Item lacks key attribute")
        else:
            if self.db.has({'crawl_url':item['crawl_url']}):
                logger.info("[%s] Item of %s has been crawled, drop it!" % (self.head, item['crawl_url']))
                raise DropItem("[%s] Info exists (url %s)" % (self.head, item['crawl_url']))
            else:
                return item


class IndustryRepeatPipeline(object):
    """
    @summary: 检查Item是否已经抓取
    """
    def __init__(self):
        self.ridb = RawInfoDB()
        self.head = 'RepeatPipeline'

    def process_item(self, item, spider):
        """
        @summary: 查看资讯是否已抓取
        @mark: 这里通过crawl_url和remark两个字段查询
               其虫, remark用于判断数据源的不同入口（因为关键字需要在去重阶段合并）
        @param item: Item资讯数据对象
        @param spider: 爬虫对象
        """
        # 检查字段crawl_url
        if 'crawl_url' not in item or not item['crawl_url']:
            logger.error("[%s] Item lack crawl_url, drop it!" % (self.head))
            raise DropItem("Item lacks key attribute")
        else:
            # 数据库查询
            if self.ridb.has(item['crawl_url'],item['remark']):
                logger.info("[%s] Item of %s has been crawled, drop it!" % (self.head, item['crawl_url']))
                raise DropItem("[%s] Info exists (url %s)" % (self.head, item['crawl_url']))
            else:
                return item

