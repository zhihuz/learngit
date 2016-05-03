# -*- coding: utf-8 -*-

import re
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from probe import logger


class ImagePipeline(ImagesPipeline):
    """ 
    @summary: 资讯配图下载 
    """
    def get_media_requests(self, item, info):
        if 'image_urls' in item:
            for (i,url) in enumerate(item['image_urls']):
                item['image_urls'][i] = url.strip()
                yield Request(item['image_urls'][i])

    def item_completed(self, results, item, info):
        # 标记并重定向已下载对应图片的<img>标签
        if 'image_urls' in item:
            flag = 1
            # 下载失败的图片输出日志
            for (i,error) in enumerate([errors for ok, errors in results if not ok]):
                print "error: ", item['crawl_url'],item['image_urls'][i], error.getErrorMessage()
                error.printDetailedTraceback()
                logger.warning("Download image failed: {0} {1} {2}".format(error.getErrorMessage(),item['crawl_url'],item['image_urls'][i]))
                flag = 0
            if not flag:
                raise DropItem("[ImagePipeline] Lack image (url: %s) " % (item['crawl_url']))
            else:
                # 下载成功图片  图片格式: (True/False, {'url','path','checksum'})
                item['image_info'] = [image for ok, image in results if ok]
                # 内容中的<img>标签更新 
                content = item['content']
                for image in item['image_info']:
                    url = re.sub("\?", "\?", image['url'])
                    # <img!>为一个标记标签，不会被误删
                    try:
                        content = re.sub("<img[^<>]*?src=\"{0}\"[^<>]*?>".format(url),"<img!>", content)
                    except Exception, e:
                        logger.warning("#ImagePipeline##item_completed##process content error##{0}##because of {1}##".format(item['crawl_url'], e))
                # 设置资讯配图字段 
                item['image'] = ','.join([image['path'] for image in item['image_info']]) 
                # 删除其他的<img>标签
                content = re.sub("<img[^!]*?>", "", content)
                # 换位标记位“>”
                content = re.sub("<img!", "<img", content)
                item['content'] = content
                return item


class IconPipeline(ImagesPipeline):
    """
    @summary: 资讯图标下载
    """
    def get_media_requests(self, item, info):
        if 'icon' in item and item['icon'] != '':
            yield Request(item['icon'])

    def item_completed(self, results, item, info):
        # 重定向已下载icon路径
        if 'icon' in item:
            image_path = [image['path'] for ok, image in results if ok]  # 取下载成功的图片
            if not image_path:
                for error in [errors for ok, errors in results if not ok]:
                    logger.warning("Download icon failed: {0} {1}".format(error.getErrorMessage(), item['crawl_url']))
                return item
            item['icon'] = image_path[0]
        return item
