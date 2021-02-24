# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubeScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    index = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    mtype = scrapy.Field()
