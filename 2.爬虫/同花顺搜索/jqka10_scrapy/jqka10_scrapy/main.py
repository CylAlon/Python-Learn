# -*- coding:utf-8 -*-

from scrapy import cmdline
from settings import r
import redis



find_name = input('请输入你需要查找的内容: ')
# find_id = input('请输入你需要查找内容的代码编号: ')
# find_name ='中国平安'
# find_id = 'SH601318'

r.set('find_name',find_name)
# r.set('find_id',find_id)

print(f'{find_name}----正在爬取数据.....')
# 同花顺财经爬虫
cmdline.execute(('scrapy crawl jqka --nolog').split())










