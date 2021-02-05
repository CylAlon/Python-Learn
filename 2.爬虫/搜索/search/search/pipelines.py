'''
# -*- coding:utf-8 -*-: 
Descripttion: 
Author: Cyl
Date: 2021-02-05 11:03:45
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os
import redis
from search.settings import pool

class SearchPipeline:
    def __init__(self):
        self.r = redis.Redis(connection_pool=pool, decode_responses=True)
        self.find_name = self.r.get('find_name')
        self.path = root = os.getcwd()
        self.file = open(self.path+'/search/file/'+self.find_name+'.json', 'w')

    def process_item(self, item, spider):
        file = item['name']
        item = dict(item)
        
        json_data = json.dumps(item,ensure_ascii=False)+',\n'
        self.file.write(json_data)
        return item
    def __del__(self):
        self.file.close()

