# -*- coding:utf-8 -*-
'''
Descripttion:
Author: Cyl
Date: 2021-02-08 10:35:28
'''
from scrapy import cmdline
from settings import r
import redis



find_name = input('请输入你需要查找的内容: ')
find_id = input('请输入你需要查找内容的代码编号: ')
# find_name ='中国平安'
# find_id = 'SH601318'

r.set('find_name',find_name)
r.set('find_id',find_id)

print(f'{find_name}--{find_id}--正在爬取数据.....')
# 老虎爬虫
cmdline.execute(('scrapy crawl itiger --nolog').split())










