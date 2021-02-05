# -*- coding:utf-8 -*-
'''
Descripttion: 微博爬虫
Author: Cyl
Date: 2021-02-05 11:06:13
'''
import scrapy
from search.settings import COOKIE,pool
import redis
import re
from search.items import SearchItem
import time
import datetime

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['https://s.weibo.com/']
    r = redis.Redis(connection_pool=pool, decode_responses=True)
    find_name = r.get('find_name')
    atime = 7
    cookies = {}
    url1 = {}

    def start_requests(self):
        temp = COOKIE
        ur = self.start_urls[0]
        today = datetime.date.today()
        # 昨天时间
        yesterday = today - datetime.timedelta(days=self.atime)
        star = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))

        times = datetime.datetime.fromtimestamp(star)
        tims = str(times)
        sy = tims.split(' ')[0]

        article = ['article','&Refer=weibo_article'] # 文章
        video = ['weibo','&xsort=hot&suball=1&timescope=custom:'+sy+':&Refer=g'] #视频

        self.url1 = {
            'article':ur+article[0]+'?q='+self.find_name+article[1],
            'video':ur+video[0]+'?q='+self.find_name+video[1],
            # 'topic':ur+topic[0]+'?q='+self.find_name+topic[1],
        }
        self.cookies = {data.split('=')[0]:data.split('=')[-1] for data in temp.split(';')}
        li0 = []
        for ui in self.url1:
            li0.append(ui)
        yield scrapy.Request(url=self.url1['article'],callback=self.parse,cookies=self.cookies,meta={'tag':li0,'num_flag':0})

    def parse(self, response): # 处理并转换文章
        try:
            item = SearchItem()
            tag = response.meta['tag']
            num_flag = response.meta['num_flag']
            tag_fl = tag[num_flag]
            card=''
            card = response.xpath('//*[@class="card-wrap"]/div')
            if tag_fl==tag[1]:
                card = response.xpath('//*[@action-type="feed_list_item"]')
            # print(f'当前页数量: {len(card)}')
            for hr in card:
                # /div/div[1]/div[2]/p[1]/a[last()]
                card_url = ''
                bas = ['','','']
                if tag_fl == tag[0]:
                    card_url = hr.xpath('./div/h3/a/@href').extract_first()
                    bas[2] = '文章类型'
                    bas[1] = hr.xpath('./div/div/div[2]/div/div/span[2]/text()').extract_first() 
                    
                    bas[0] = hr.xpath('./div/h3/a/@title').extract_first() 
                    
                elif tag_fl == tag[1]:
                    card_url = hr.xpath('.//p[@class="from"]/a[1]/@href').extract_first() 
                    tm = hr.xpath('.//p[@class="from"]/a[1]/text()').extract_first()
                    
                    tt = re.findall(r'\w+',str(tm))
                    u = ''
                    for p in tt:
                        u = u + p+'-'
                    bas[1] = u

                    card_url = 'https:'+card_url
                    zw = hr.xpath('./div/div/div[2]/p[1]/text()').extract()
                    zw = re.findall(r'\w+',str(zw))
                    zw = zw[1:len(zw)-1]
                    c = ''
                    for s in zw:
                        c = c+s
                    bas[0] = c
                    bas[2] = '基本类型'

                # print(tag_fl,'--------',card_url,'-------',num_flag)
                item['name'] = self.find_name
                item['url'] = card_url

                item['title'] = bas[0]
                item['time'] = bas[1]
                item['mtype'] = bas[2]
                # print(item)
                yield item
            # # 翻页
            pag = response.xpath('//*[@class="s-scroll"]/li')
            moment= response.xpath('//*[@class="cur"]/a/text()').re('第(.*?)页')[0]

            if int(moment)<len(pag):
                ur = response.xpath('//*[@class="cur"]/a/@href').extract_first()
                d = re.compile('/(.*?)page=.*?').findall(ur)
                nuu = int(moment)+1
                url = self.start_urls[0]+d[0]+'page='+str(nuu)
                # print(f'----------下一页{nuu}------{url}')
                # yield tag
                yield scrapy.Request(url=url,callback=self.parse,cookies=self.cookies,meta={'tag':tag,'num_flag':num_flag})
            else:
                try:
                    no = tag[num_flag+1]
                    # print('*************-------------',no,self.url1[no])
                    yield scrapy.Request(url=self.url1[no],callback=self.parse,cookies=self.cookies,meta={'tag':tag,'num_flag':num_flag+1})
                except  Exception as e:
                    print('爬虫即将结束')
        except Exception as ex:
            print('哎呀!!!好像获取内容无法访问,请重新允许代码')
            self.crawler.engine.close_spider(self, '退出爬虫')


