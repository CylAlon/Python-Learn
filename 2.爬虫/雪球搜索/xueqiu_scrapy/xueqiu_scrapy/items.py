# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XueqiuScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    index = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    mtype = scrapy.Field()
    # content = scrapy.Field()
    """
    item['index'] = 
    item['name'] = self.findname
    item['title'] = title
    item['time'] = time
    item['mtype'] = '新闻类型'
    item['url'] = url

    """
