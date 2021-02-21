import re

import scrapy
import json
import time
import utils
from items import FutunnScraypItem
from spiderManage import SpiderManagerJson
from settings import r

class FutunnSpider(scrapy.Spider):
    name = 'futunn'
    allowed_domains = ['www.futunn.com']
    start_urls = ['http://www.futunn.com/']
    # flags =[True]
    page = [0,0,0,0]
    find_name = utils.getFindName()
    utils.set_index(4)
    index = [0,0,0,0]
    
    def parse(self, response):
        # https://news.futunn.com/main?lang=zh-cn
        # https://news.futunn.com/main/live?lang=zh-cn
        # https://q.futunn.com/nnq?lang=zh-cn
        # https://q.futunn.com/nnq?lang=zh-cn#popular
        # https://q.futunn.com/nnq?lang=zh-cn#essence

        # https://news.futunn.com/client/market-list?news_id=149765&lang=zh-cn
        url = [
            # 'https://news.futunn.com/main?lang=zh-cn',https://news.futunn.com/main/live-list?page=0&page_size=50&_=1613727064943
            self.get_url(0,-1),
            self.get_url(1,0),
            self.get_url(2,0,mark=0),
            self.get_url(3,0,mark=0)
            # 'https://q.futunn.com/nnq?lang=zh-cn'
        ]
        num = -1
        for u in url:
            num +=1
            yield scrapy.Request(url=u,callback=self.dis_parse,dont_filter=True,meta={'num':num})

    def dis_parse(self,response):
        num = response.meta['num']
        items = FutunnScraypItem()
        sp = jsonspider(response=response,items=items,name=self.find_name)
        
        if num == 0:
            sp.set_num(num)
            data_list,_ = sp.get_data_list()
            for da in data_list:
                item_list = sp.get_item_list(da)
                if not sp.get_time_judge(item_list['time']):
                    break
                if self.find_name not in item_list['abstract'] and self.find_name not in item_list['title']:
                    continue
                yield sp.get_items(items,item_list)
            if sp.get_page_flag():
                ur = self.get_url(num, sp.get_news_id())
                yield scrapy.Request(url=ur,callback=self.dis_parse,dont_filter=True,meta={'num':num})
            
        elif num ==1:
            sp.set_num(num)
            data_list,_ = sp.get_data_list()
            for da in data_list:
                item_list = sp.get_item_list(da)
                
                if not sp.get_time_judge(item_list['time']):
                    break
                if self.find_name not in item_list['title']:
                    continue
                yield sp.get_items(items,item_list)
            self.page[num]+=1
            if sp.get_page_flag() and self.page[num]<=20: # 时间混乱 查找前20页
                ur = self.get_url(num, self.page[num])
                yield scrapy.Request(url=ur,callback=self.dis_parse,dont_filter=True,meta={'num':num})
    
        elif num ==2:
            sp.set_num(num)
            data_list,other_data = sp.get_data_list()
            mark =other_data['more_mark']
            for da in data_list:
                item_list = sp.get_item_list(da)
                if not sp.get_time_judge(item_list['time']):
                    break
                if self.find_name not in item_list['title']:
                    continue
                yield sp.get_items(items,item_list)
            if sp.get_page_flag():
                ur = self.get_url(num,1,mark=mark)
                yield scrapy.Request(url=ur,callback=self.dis_parse,dont_filter=True,meta={'num':num})
        elif num  == 3:
            # print(response.text)
            sp.set_num(num)
            data_list,other_data = sp.get_data_list()
            mark =other_data['more_mark']
            for da in data_list:
                item_list = sp.get_item_list(da)
                if not sp.get_time_judge(item_list['time']):
                    break
                if self.find_name not in item_list['title']:
                    continue
                yield sp.get_items(items,item_list)
            self.page[num]+=1
            if self.page[num]<20: # 时间混乱 查找前20页
                ur = self.get_url(num,1,mark=mark)
                yield scrapy.Request(url=ur,callback=self.dis_parse,dont_filter=True,meta={'num':num})

    def get_url(self,num,page,**kwargs):
        if num == 0:
            url = f'https://news.futunn.com/client/market-list?news_id={page}&lang=zh-cn'
        elif num ==1:
            ti = time.time()
            ti = '%.0f'%ti
            url = f'https://news.futunn.com/main/live-list?page={page}&page_size=50&_={ti}'
        elif num ==2:
            ti = time.time()*1000
            ti = '%.0f'%ti
            mark = kwargs['mark']
            url = f'https://q.futunn.com/nnq/list-feed?relation_type=0&feed_mark={mark}&more_mark={mark}&refresh_type={page}&_={ti}'
        elif num ==3:
            ti = time.time()*1000
            ti = '%.0f'%ti
            mark = kwargs['mark']
            url = f'https://q.futunn.com/nnq/list-feed?relation_type=5&feed_mark={mark}&more_mark={mark}&refresh_type={page}&_={ti}'
        return url
    
class jsonspider(SpiderManagerJson):
    def __init__(self,**kwags):
        super(jsonspider, self).__init__(**kwags)
        self.news_id=0

    def get_json_list(self,json_data):
        if self.num ==0 or self.num ==1:
            json_dat = json_data['data']['list']
            other_data = ''
        elif self.num == 2 or self.num == 3:
            json_dat = json_data['data']['feed']
            other_data = json_data['data']
        return json_dat,other_data

    def get_data_from_json(self,items,data):
        if self.num==0:
            items['title'] = data['title']
            items['time'] = data['time']
            items['url'] = data['url']
            items['typ'] = '要闻类型'
            self.news_id = data['news_id']
            items['abstract']=data['abstract']
        elif self.num==1:
            items['title'] = data['content']
            ti = data['create_time_str']
            items['time'],_ = utils.tim_interconversion(ti)
            items['url'] = ''
            items['typ'] = '7X24'
        elif self.num==2:
            ti = data['common']['timestamp']
            if len(data['summary']['module_content'])==0:
                items['time']= 0
                items['url'] = ''
                items['typ'] = ''
                items['title'] = ''
                return items
            data = data['summary']['module_content'][0]['original']
            try:
                items['title'] = data['title']
            except Exception as e:
                items['title'] = data['text']
            items['time']= int(ti)
            items['url'] = data['url']
            items['typ'] = '牛圈'
        elif self.num ==3:
            ti = data['common']['timestamp']
            feed_id = data['common']['feed_id']
            data = data['summary']
            da = data['title']
            if da is None:
                da = data['rich_text'][0]['text']
                # da = data['text']
            items['title'] = da
            items['time']= int(ti)
            ur = f'https://q.futunn.com/feed/{feed_id}'
            items['url'] = ur
            items['typ'] = '热门'
        return items

    def get_news_id(self):
        return self.news_id
    