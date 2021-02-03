# -*- coding:utf-8 -*-
'''
# -*- coding:utf-8 -*-: 
Descripttion: 
Author: Cyl
Date: 2021-02-03 08:51:52
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import scrapy
import hashlib
from scrapy.utils.python import to_bytes
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

class BellePipeline:
    def process_item(self, item, spider):
        return item

class dowimgPipline(ImagesPipeline):
    item ={}
    ni = 0
    def get_media_requests(self, item, info):
        # 1 获取图片链接
        self.item = item
        url = item["url"]
        yield scrapy.Request(url=url)

        
    def file_path(self, request, response=None, info=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        foder_tag = self.item['tag']
        foder_name = self.item['name']

        return foder_tag+'/'+foder_name + '/%s.jpg' % (image_guid)
        
