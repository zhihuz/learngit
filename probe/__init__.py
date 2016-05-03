# -*- coding: utf-8 -*-

#from probe.crawler.settings import LOG_DIR
from probe.utils.log import SpiderLogger

LOG_DIR = "/home/solosseason/probe/center/logs"
logger = SpiderLogger(logger="Spider",log_dir=LOG_DIR).getLog()
