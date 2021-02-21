import scrapy
import json
import time
import utils
import random
import re
from items import EastmoneyItem
from spiderManage import SpiderManagerJson
from settings import r

class EastMoneySpider(scrapy.Spider):
    name = 'east_money'
    allowed_domains = ['so.eastmoney.com']
    start_urls = ['http://so.eastmoney.com/']
    find_name = utils.getFindName()
    utils.set_index(3)
    page = [1,1,1]
    def parse(self, response):
        url = [
            self.get_urls(0,page=1),
            self.get_urls(1,page=1),
            self.get_urls(2,page=1)
        ]
        for i in range(len(url)):
            yield scrapy.Request(url=url[i],callback=self.manage_parse,dont_filter=True,meta={'num':i})

    def manage_parse(self,response):
        num = response.meta['num']
        item = EastmoneyItem()
        sp = dfcfspider(response=response,name=self.find_name)
        if num == 0:
            sp.set_num(num)
            json_data,_ = sp.get_data_list()
            for da in json_data:
                item_list = sp.get_item_list(da)
                if not sp.get_time_judge(item_list['time']):
                    break
                yield sp.get_items(item,item_list)
            if sp.get_page_flag():
                self.page[num] += 1
                url = self.get_urls(num,page=self.page[num])
                yield scrapy.Request(url=url,callback=self.manage_parse,dont_filter=True,meta={'num':num})
        elif num == 1:
            pass
            sp.set_num(num)
            json_data,_ = sp.get_data_list()
            for da in json_data:
                item_list = sp.get_item_list(da)
                if not sp.get_time_judge(item_list['time']):
                    break
                yield sp.get_items(item,item_list)
            if sp.get_page_flag():
                self.page[num] += 1
                url = self.get_urls(num,page=self.page[num])
                yield scrapy.Request(url=url,callback=self.manage_parse,dont_filter=True,meta={'num':num})
        elif num == 2:
            sp.set_num(num)
            json_data,_ = sp.get_data_list()
            for da in json_data:
                item_list = sp.get_item_list(da)
                if not sp.get_time_judge(item_list['time']):
                    break
                yield sp.get_items(item,item_list)
            if sp.get_page_flag():
                self.page[num] += 1
                url = self.get_urls(num,page=self.page[num])
                yield scrapy.Request(url=url,callback=self.manage_parse,dont_filter=True,meta={'num':num})

    def get_urls(self,num,**kwags):
        page = kwags['page']
        cb = self.get_js()
        ti = time.time()*1000
        ti = '%.0f'%ti
        if num==0:
            url = f'http://searchapi.eastmoney.com//bussiness/Web/GetCMSSearchList?type=8196&pageindex={page}&pagesize=10&keyword={self.find_name}&name=zixun&cb={cb}&_={ti}'
        elif num==1:
            url = f'http://searchapi.eastmoney.com/bussiness/Web/GetSearchList?type=8224&pageindex={page}&pagesize=10&keyword={self.find_name}&name=caifuhaowenzhang&cb={cb}&_={ti}'
        elif num==2:
            url = f'http://searchapi.eastmoney.com/bussiness/Web/GetSearchList?type=202&pageindex={page}&pagesize=10&keyword={self.find_name}&name=normal&cb={cb}&_={ti}'
        return url

    def get_js(self):
        ret = 'jQuery'
        m = "1.12.4"
        fm = m + str(random.random())
        fmt = re.findall('\d+',fm)
        for i in fmt:
            ret = ret+i
        ti = (time.time()*1000)+2
        ti = '%.0f'%ti
        ret = ret+'_'+str(ti)
        return ret

class dfcfspider(SpiderManagerJson):
    def __init__(self,**kwags):
        super(dfcfspider, self).__init__(**kwags)
    def get_data_list(self):
        json_data,other_data='',''
        data = re.findall('\((.*)\)',self.response.text)[-1]
        data = json.loads(data)
        if self.num==0:
            json_data = data['Data']
        elif self.num==1:
            json_data = data['Data']
        elif self.num==2:
            json_data = data['Data']
        return json_data,other_data
    

    def get_data_from_json(self,item,data):
        if self.num==0:
            item['title'] = data['Art_Title']
            item['time'] = data['Art_CreateTime']
            item['url'] = data['Art_Url']
            item['typ'] = '资讯'
        elif self.num==1:
            item['title'] = data['Title']
            item['time'] = data['ShowTime']
            item['url'] = data['ArticleUrl']
            item['typ'] = '财富文章'
        elif self.num==2:
            item['title'] = data['Title']
            item['time'] = data['CreateTime']
            item['url'] = data['Url']
            item['typ'] = '博客'
            
        return item

