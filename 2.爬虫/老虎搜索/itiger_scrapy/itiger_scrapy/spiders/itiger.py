import re

import scrapy
import json
import time
import utils
from items import ItigerScrapyItem
from settings import DAY, HOUR, MINUTE, SECOND, WEEK


class ItigerSpider(scrapy.Spider):
    name = 'itiger'
    allowed_domains = ['www.laohu8.com']
    find_name = utils.getFindName()
    find_id = utils.getFindId()
    u1 = f'https://www.laohu8.com/search?word={find_name}'
    ui = re.findall("\d+",find_id)[-1]
    u2 = f'https://www.laohu8.com/stock/{ui}'
    start_urls = [u1,u2]
    page = 0
    flag = True
    index = 0
# https://www.laohu8.com/search?word=中国平安&page=all
# https://www.laohu8.com/proxy/oldCommunity/search/v5/general?word=中国平安&pageCount=1
    def parse(self, response):
        ur = response.url
        if 'stock' in ur:
            item = ItigerScrapyItem()
            item['index'] = 1
            item['name'] = self.find_name
            item['title'] = self.find_id+' '+self.find_name
            item['time'] = '实时股票'
            item['mtype'] = '股票类型'
            item['url'] = ur
            # print(item)
            yield item
        else:
            if not self.flag:
                item = ItigerScrapyItem()
                json_data = json.loads(response.text)
                contentList = json_data['data']['contentList']
                for lp in contentList:
                    timm = lp['gmtCreate']
                    tim = timm/1000
                    ago_time = utils.dateAgo(week=WEEK,day=DAY,hour=HOUR,minute=MINUTE,second=SECOND)
                    tempago,_ = utils.tim_interconversion(ago_time)
                    # tempmoment,date = utils.tim_interconversion(tim)
                    ti = time.localtime(tim)
                    ti = time.strftime('%Y-%m-%d %H:%M:%S',ti)
                    if timm>tempago:

                        cont = lp['entity']
                        title = ''
                        try:
                            title = cont['title']
                        except Exception as e:
                            title = cont['listText']
                            try:
                                title = title[:200]
                            except Exception as ex:
                                pass
                        url = lp['objectId']
                        
                        self.index +=1
                        item['index'] = self.index
                        item['name'] = self.find_name
                        item['title'] = title
                        item['time'] = ti
                        item['mtype'] = '综合类型'
                        item['url'] = 'https://'+self.allowed_domains[0]+'/post/'+str(url)
                        yield item
                    
            if self.page<15: # 由于页面时间混乱
                self.page +=1
                url = f'https://www.laohu8.com/proxy/oldCommunity/search/v5/general?word={self.find_name}&pageCount={self.page}'
                
                yield scrapy.Request(url = url ,callback=self.parse)
                self.flag = False



