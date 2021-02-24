# -*- coding:utf-8 -*-

from scrapy import cmdline
from settings import r
import redis



find_name = input('请输入你需要查找的内容: ')
# find_id = input('请输入你需要查找内容的代码编号: ')
# find_name ='中国平安'
# find_id = 'SH601318'
print(f'你要查找的信息是:{find_name}')
r.set('find_name',find_name)

# print(f'你要查找信息的代码编号是:{find_id}')
# r.set('find_id',find_id)

print(f'{find_name}--{1}--正在爬取数据.....')
# 雪球爬虫
cmdline.execute(('scrapy crawl bilibili --nolog').split())










