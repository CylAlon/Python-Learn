# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImoocScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    course_name = scrapy.Field()
    cover_img_address= scrapy.Field()
    course_duration = scrapy.Field()
    course_price = scrapy.Field()
    course_information = scrapy.Field()
    course_teacher = scrapy.Field()
    course_video_address = scrapy.Field()
