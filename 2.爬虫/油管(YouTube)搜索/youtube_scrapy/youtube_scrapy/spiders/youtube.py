import scrapy
import json
import time
import utils
import random
import re
from items import YoutubeScrapyItem
from spiderManage import SpiderManagerJson

class YoutubeSpider(scrapy.Spider):
    name = 'youtube'
    allowed_domains = ['www.youtube.com']
    find_name = utils.getFindName()
    start_urls = [f'https://www.youtube.com/results?search_query={find_name}&sp=EgQIAhAB']
    index = 0
    def parse(self, response):
        item = YoutubeScrapyItem()
        data = response.xpath('//*[@id="contents"]/ytd-video-renderer')
        for dat in data:
            item['title'] = dat.xpath('./div/div/div[1]/div/h3/a/@title').extract_first()
            item['url'] = 'https://'+self.allowed_domains[0]+dat.xpath('./div/div/div[1]/div/h3/a/@href').extract_first()

            if dat.xpath('./div/div[1]/ytd-badge-supported-renderer/div[1]/span[1]/text()').extract_first() == '正在直播':
                item['time'] = '正在直播'
            else:
                item['time'] = dat.xpath('./div/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]/text()').extract_first()
            item['name'] = self.find_name
            item['mtype'] = 'youtube-viedo'
            self.index+=1
            item['index'] = self.index
            # print(item)
            yield item
