# -*- coding:utf-8 -*-
'''
# -*- coding:utf-8 -*-: 
Descripttion: 
Author: Cyl
Date: 2021-02-03 08:51:52
'''
import scrapy
import re
from belle.settings import CATALOGUE,CATALOGUE_PATH
from belle.items import BelleItem

class BellSpider(scrapy.Spider):
    name = 'bell'
    allowed_domains = ['tujigu.com']
    start_urls = ['https://www.tujigu.com/']
    cont = ['中国','日本','韩国','泰国']
    namli = []
    tag = ''
    sh = 0

    def parse(self, response):
        
        url_list = response.xpath("""/html/body/div[1]/div[2]""")

        name_catche =url_list.re('<a href="'+self.start_urls[0]+'(.*?)">(.*?)</a>')
        
        for di in range(4,len(name_catche)-2,2):
            CATALOGUE[name_catche[di+1]] = name_catche[di]

        for va in CATALOGUE:
            print(va,end=',')
        print('')
        inpt = input('请输入你要下载图片的类型：')
        lis = []
        while True:
            inpt = inpt.split('，')
            for li in inpt:
                if (li not in CATALOGUE) and (li != ''):
                    inpt = input('目标不存在，请重新输入你要下载图片的类型:')
                    lis.clear()
                    break
                lis.append(li)
            else:
                break
        print('正在下载......')
        if lis[0]=='':
            lis = list(CATALOGUE.keys())
        
        for x in lis:
            CATALOGUE_PATH[x] = self.start_urls[0]+CATALOGUE[x]
        ur = CATALOGUE_PATH[lis[0]]
        yield scrapy.Request(url=ur,callback=self.access_parse,meta={'lis':lis,'num':0})
        
    def access_parse(self,response):
        
        lis = response.meta['lis']
        num = response.meta['num']
        li = response.xpath('//*[@class="hezi"]/ul/li')
        self.tag = lis[num]
        
        for p in li:
            url = p.xpath('./a[1]/@href').extract_first()
            name = p.xpath('./p[2]/a/text()').extract_first()
            self.namli.append(name)
            # gro['url'] = url
            yield scrapy.Request(url=url,callback=self.open_parse)
        # 翻页
        
        url_page=''
        if tag in self.cont:
            # 选择国家的情况
            moment = response.xpath('//*[@id="pages"]/span/text()').extract_first()
            end = response.xpath('//*[@id="pages"]/a[last()-1]/text()').extract_first()
            if end>moment:
                url_page = response.xpath('//*[@id="pages"]/a[last()]/@href').extract_first()
                url_page =  'https://www.tujigu.com'+url_page
        else:
            # 选择类型
            lashrf = response.xpath('//*[@id="pages"]/a[last()]/@href').extract_first()
            url_page =  'https://www.tujigu.com'+lashrf
        day = {
            'lis':lis,
            'num':num+1,
        }
        yield scrapy.Request(url=url_page,callback=self.access_parse,meta=day)  


    def open_parse(self,response):
        self.sh=self.sh+1
        item = BelleItem()
        item['name']=self.namli[self.sh-1]
        item['tag'] = self.tag
        
        img_url = response.xpath('//*[@class="content"]/img/@src').extract()
        
        for u in img_url:
            item['url'] = u
            yield  item
        
        moment = response.xpath('//*[@id="pages"]/span/text()').extract_first()
        end = response.xpath('//*[@id="pages"]/a[last()-1]/text()').extract_first()
        if end>moment:
            url_page = response.xpath('//*[@id="pages"]/a[last()]/@href').extract_first()
            url_page =  url_page
            yield scrapy.Request(url=url_page,callback=self.open_parse)  