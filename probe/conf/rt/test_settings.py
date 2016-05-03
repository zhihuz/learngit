# -*- coding: utf-8
"""
@summary: 项目配置
"""
import sys
sys.path.append("../")

BOT_NAME = 'crawler'
SPIDER_MODULES = ['crawler.spiders.energy','crawler.spiders.steel','crawler.spiders.robot']

DATA_BASE = "/home/hello/data/hello/"

# 下载器中间件
DOWNLOADER_MIDDLEWARES = {
    'probe.crawler.middlewares.random_useragent.RandomUserAgent': 100,
    }

# 持久化组件
ITEM_PIPELINES = {
    # item字段类型检查
    'probe.crawler.pipelines.process.TypeCheckPipeline': 200,
    # 资讯配图处理
    #'probe.crawler.pipelines.image.ImagePipeline': 400,
    # 资讯图片处理
    #'probe.crawler.pipelines.image.IconPipeline': 500,
    # 数据清洗	
    #'probe.crawler.pipelines.process.DataCleanPipeline': 550,
    # item字段标准化
    'probe.crawler.pipelines.process.NormalizePipeline': 600,
    # 数据清洗
    'probe.crawler.pipelines.process.DataCleanPipeline' : 650,
}

# 图片
IMAGES_EXPIRES = 10
IMAGES_STORE = DATA_BASE+"/images"

# 日志
LOG_DIR = DATA_BASE+"/logs"
LOG_LEVEL = 'DEBUG'
# 失败后重连次数
RETRY_TIMES = 500

# 下载延迟
DOWNLOAD_DELAY = 0.75

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

# rt模式下每次抓取的页面个数
PAGE_NUM = 3
