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
        self.index = 0
        self.r = redis.Redis(connection_pool=pool, decode_responses=True)
        self.find_name = self.r.get('find_name')
        self.path = os.getcwd()
        # pa = self.path+'/search/file/'+self.find_name+'_weibo.json'
        self.ht = ''
        with open(self.path+'/search/template.html','r') as f:
            self.ht = f.read()
        self.file = open(self.path+'/search/file/'+self.find_name+'_weibo.html', 'a+')
        self.file.write(self.ht)

    def process_item(self, item, spider):
        file = item['name']
        item = dict(item)
        self.index = self.index+1

        tr = f"\
        <tr class='tx'>\n\
            <td>{self.index}</th>\n\
            <td>{item['name']}</th>\n\
            <td>{item['title']}</th>\n\
            <td>{item['time']}</th>\n\
            <td>{item['mtype']}</th>\n\
            <td><a href={item['url']}>点击</a></th>\n\
        </tr>\n\
        "

    #    json_data = '<p>"1":"title": '+item["title"]+',<a href='+item['url']+'>点击</a>"time": '+item[time]+', "mtype": '+item['mtype']+'</p>''
        
        # json_data = json.dumps(item,ensure_ascii=False)+',\n'
        self.file.write(tr)
        return item
    def __del__(self):
        en = '    </table>\n\
            </body>\n\
        </html>'
        self.file.write(en)
        self.file.close()

