'''
# -*- coding:utf-8 -*-: 
Descripttion: 
Author: Cyl
Date: 2021-02-05 11:03:45
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    mtype = scrapy.Field()
