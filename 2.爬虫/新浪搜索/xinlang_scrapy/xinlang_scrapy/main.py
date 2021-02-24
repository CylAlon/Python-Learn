# -*- coding:utf-8 -*-

from scrapy import cmdline
from settings import r
import redis

log = ''
fl = input('你要打日志吗(打印输入1,不打印输入0): ')
if fl=='0':
    log = '--nolog'

find_name = input('请输入你需要查找的内容: ')

r.set('find_name',find_name)

print('正在爬取数据.....')
# 新浪爬虫
cmdline.execute(('scrapy crawl xinlang '+log).split())










