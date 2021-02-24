# -*- coding:utf-8 -*-


from scrapy import cmdline
from search.settings import pool 
import redis

log = ''
fl = input('你要打日志吗(打印输入1,不打印输入0): ')
if fl=='0':
    log = '--nolog'
r = redis.Redis(connection_pool=pool, decode_responses=True)

find_name = input('请输入你需要查找的内容: ')

r.set('find_name',find_name)


# 微博爬虫
cmdline.execute(('scrapy crawl weibo '+log).split())