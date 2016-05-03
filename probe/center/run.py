# -*- coding: utf-8 -*-

"""
@summary: 爬虫启动脚本
@mark: 整个工程使用统一时间格式: %Y-%m-%d %H:%M:%S  以方便传递时间, 例如2015-10-13 16:00:00
"""
import sys
sys.path.append("/home/solosseason")

import json
import time
import traceback
import imp
import ConfigParser
import uuid
from optparse import OptionParser
from datetime import datetime
from multiprocessing import Pool
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from probe import logger
#from probe.db.service.StockDB import requestStocks
from scrapy.settings import Settings
from probe.conf.rt import test_settings

DELAY = 60 #18000  # 下次启动爬取的间隔，单位：秒
parser = OptionParser()
parser.add_option('-c', '--config', default=None, help="爬虫配置文件")
parser.add_option('-s', '--start', default=None, help="测试用, 开始时间, 格式为%Y-%m-%d %H:%M:%S, 如2016-01-01 00:00:00, 若不设置, 默认为一年前的时间")
parser.add_option('-e', '--end', default=None, help="测试用, 结束时间, 格式为%Y-%m-%d %H:%M:%S, 如2016-01-01 00:00:00, 若不设置, 默认为当前时间")      
(opts, files) = parser.parse_args()
# import 爬虫配置文件模块
confpath = "../crawler/configs/" + opts.config + ".py"
confname = opts.config.split("/")[-1]
conf = imp.load_source(confname, confpath)

class SpiderConf(object):
    # 爬虫配置项
    def __init__(self, path, conf):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(path)
        self.crawl_mode = self._get_crawl_mode()
        self.params = self._get_params()
        self.blocks = self._get_blocks()
        self.config = self._make_config(conf)

    def _get(self, field, key):
        return self.cf.get(field, key)

    def _get_crawl_mode(self):
        return self._get("spiderconf", "crawl_mode")

    def _get_params(self):
        retry_times = int(self._get("spiderconf", "retry_times"))
        page_num = int(self._get("spiderconf", "page_num"))
        dont_filter = int(self._get("spiderconf", "dont_filter"))
        params = {}
        if retry_times:
            params['retry_times'] = retry_times
        if page_num:
            params['page_num'] = page_num
        if dont_filter:
            params['dont_filter'] = (False if dont_filter == 0 else True)
        return params

    def _get_blocks(self):
        return int(self._get("spiderconf", "blocks"))

    # 爬虫配置文件模块生成字典
    def _make_config(self, conf):
        config = {}
        config_attr = []
        for attr in dir(conf):
            if not attr.startswith('_'):
                config_attr.append(attr)
        for attr in config_attr:
            config[attr] = getattr(conf, attr)
        if 'entrance' not in config.keys():
            config['entrance'] = ['000000'] #[str(stk['full_code']) for stk in requestStocks(stypes=['上证A','深证A'], attributes=['full_code'])]
        return config

    def get_spiderconf(self):
        spiderconf = {'config': self.config, 'params': self.params, 'crawl_mode': self.crawl_mode, 'blocks': self.blocks}
        return spiderconf

class Task():
    # 调度任务
    def __init__(self, spiderconf):
        self.spiderconf = spiderconf
        self.spider = spiderconf['config']['spider_name']

    # 分块
    def _split_entrances(self, entrances, blocks):
        entrance_list = []
        num = len(entrances)/blocks
        if num == 0:
            entrance_list.append(entrances)
            return entrance_list
        for i in xrange(0, (blocks-1)*num, num):
            entrance_list.append(entrances[i:i+num])
        entrance_list.append(entrances[(blocks-1)*num:])
        return entrance_list

    def get_tasks(self):
        entrances = self._split_entrances(self.spiderconf['config']['entrance'], self.spiderconf['blocks'])
        self.spiderconf.pop('blocks')
        tasks = []
        for (i,entrance) in enumerate(entrances):
            self.spiderconf['config']['entrance'] = entrance
            task = {'task_id': str(uuid.uuid1()), 'spider_name': self.spider, 'spider_conf': json.dumps(self.spiderconf)}
            tasks.append(task)
        return tasks


def crawl(tasks): #(spider, entrances, start, end, mode, params):
    # 启动爬虫
    try:
        setting = Settings()
        if 'category' in json.loads(tasks[0]['spider_conf'])['config'].keys():
            if json.loads(tasks[0]['spider_conf'])['config']['category'] == u'industry':
                print 'settings: industry'
#                setting.setmodule(industry_settings)
            elif json.loads(tasks[0]['spider_conf'])['config']['category'] == u'stock_notice':
                print 'settings: notice'
#                setting.setmodule(notice_settings)
            elif json.loads(tasks[0]['spider_conf'])['config']['category'] == u'stock_research':
                print 'settings: research'
#                setting.setmodule(research_settings)
        else:
            print '------debug mode, use test_settings------'
            setting.setmodule(test_settings)
        process = CrawlerProcess(setting)
        for task in tasks:
            logger.info("crawl {0} from {1}".format(task['spider_name'], datetime.now()))
            spider_conf = json.loads(task['spider_conf'])
            process.crawl(task['spider_name'], configs=json.dumps(spider_conf['config']), start_time=start_time, end_time = end_time, crawl_mode = spider_conf['crawl_mode'], params = json.dumps(spider_conf['params']))
        process.start()
    except Exception,e:
        traceback.print_exc()


start_time = opts.start
end_time = opts.end

sconf = SpiderConf("case.ini", conf)
spiderconf = sconf.get_spiderconf()
t = Task(spiderconf)
tasks = t.get_tasks()
#for task in tasks:
#    print task
while True:
    pool = Pool(processes=1)
    pool.apply_async(crawl, args=(tasks,))
    pool.daemon = True
    pool.close()
    pool.join()
    if spiderconf['crawl_mode'] == 'hist':    # 若为hist模式, 直接退出
        exit()
    break
    time.sleep(DELAY)
