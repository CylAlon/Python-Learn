# -*- coding:utf-8 -*-
'''
Descripttion: 
Author: Cyl
Date: 2021-02-06 17:55:18
'''
import scrapy


class XinlangScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    index = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    mtype = scrapy.Field()
