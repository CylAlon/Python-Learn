import scrapy
import json
import time
import utils
import random
import re
from items import Jqka10ScrapyItem
from spiderManage import SpiderManagerJson


class JqkaSpider(scrapy.Spider):
    name = 'jqka'
    allowed_domains = [
        't.10jqka.com.cn',
        'news.10jqka.com.cn',
        'stock.10jqka.com.cn',
        'stock.10jqka.com.cn'
        ]
    start_urls = [
        'http://t.10jqka.com.cn/',
        'http://news.10jqka.com.cn/',
        'http://stock.10jqka.com.cn/usstock/',
        'http://stock.10jqka.com.cn/hks/'
    ]
    joinurl = [
        [''],
        ['today_list','cjzx_list','cjkx_list','guojicj_list','jrsc_list','fssgsxw_list','region_list','fortune_list','cjrw_list'],
        ['mgyw_list','mggsxw_list','gjgs_list','zggxw_list','mgcbsj_list','mgscfx_list','mgxg_list','mgxt_list'],
        ['hknews_list','ggfx_list','ggydg_list','ggdt_list','ggyj_list','ggxg_list','ahdt_list','wlzx_list','ggmj_list']
    ]
    nov_flag = True
    index = [
        [0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]
    ty = [
        ['同花顺子'],
        ['财经要闻','宏观经济','产经新闻','国际财经','金融市场','公司新闻','区域经济','财经评论','财经人物'],
        ['美股要闻','美股公司新闻','国际股市动态','中概股新闻','美股财报数据','美股市场分析','美股新股','美股学堂'],
        ['要闻','盘面','异动股','公司新闻','研究','新股','AB股','权证','名家']
        ]
    page = [
        [1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],
    ]
    
    find_name = utils.getFindName()
    ago_time = utils.get_ago_timetemp()
        
    def start_requests(self):
        ur = [
            self.get_url(0), 
            self.get_url(1,page=1,joinstr=self.joinurl[1][0]), 
            self.get_url(2,page=1,joinstr=self.joinurl[2][0]), 
            self.get_url(3,page=1,joinstr=self.joinurl[3][0])
        ]
        for i in range(len(ur)):
            yield scrapy.Request(url=ur[i],callback=self.parse,meta={'num':i,'flg':0})

    def parse(self, response):
        item = Jqka10ScrapyItem()
        num = response.meta['num']
        
        if num == 0:
            if self.nov_flag:
                self.nov_flag = False
                self.index[num][0] +=1
                nev = response.xpath('//*[@class="new-notice"]')
                item['index'] = self.index[num][0]
                item['name'] = self.find_name
                item['title'] = nev.xpath('./div/span/text()').extract_first()
                item['time'] = '热点'
                item['mtype'] = '同花顺子热点'
                item['url'] = nev.xpath('./div/@data-link').extract_first()
                yield  item
            data_list = response.xpath('//*[@class="feed-data"]/ul/li')
            for da in data_list:
                
                item['name'] = self.find_name
                tit = da.xpath('./div[2]/div/div[2]/div/div[1]/div').extract_first()
                item['title'] = tit
                ti = da.xpath('./div[1]/div[3]/text()').extract_first()
                ti = re.findall('\d+:\d+',ti)[-1]
                timp,date = utils.tim_interconversion(ti)
                if self.find_name not in item['title']:
                    continue
                self.index[num][0] +=1
                item['index'] = self.index[num][0]
                item['time'] = date
                item['mtype'] = '同花顺子'
                item['url'] = ''
                yield  item
        elif num==1 or num==2 or num==3:
            data_list = response.xpath('//*[@class="list-con"]/ul/li')
            flg = response.meta['flg']
            for da in data_list:
                
                item['time'] = da.xpath('./span/span/text()').extract_first()
                item['title'] = da.xpath('./span/a/@title').extract_first()
                if self.find_name not in item['title']:
                    continue
                self.index[num][flg]+=1
                item['index'] = self.index[num][flg]
                item['name'] = self.find_name
                item['mtype'] = self.ty[num][flg]
                item['url'] = da.xpath('./span/a/@href').extract_first()
                yield item
            self.page[num][flg]+=1
            if self.page[num][flg]<=10:
                url = self.get_url(num,page=self.page[num][flg],joinstr=self.joinurl[num][flg])
                yield scrapy.Request(url=url,callback=self.parse,dont_filter=True,meta={'num':num,'flg':flg})
            else:
                flg = flg+1
                if flg<len(self.joinurl[num]):
                    url = self.get_url(num,page=self.page[num][flg],joinstr=self.joinurl[num][flg])
                    yield scrapy.Request(url=url,callback=self.parse,dont_filter=True,meta={'num':num,'flg':flg})
            

    def get_url(self,num,**kwags):
        url = ''
        if num == 0:
            url = 'http://t.10jqka.com.cn/'
        elif num == 1 or num==2 or num==3:
            joinstr = kwags['joinstr']
            page = kwags['page']
            start_ur = self.start_urls[num]
            url = f'{start_ur}{joinstr}/index_{page}.shtml'
        return url


