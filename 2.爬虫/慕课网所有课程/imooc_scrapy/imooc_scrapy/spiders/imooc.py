import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import ImoocScrapyItem
import re

class ImoocSpider(CrawlSpider):
    name = 'imooc'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.imooc.com/course/list','https://coding.imooc.com/','https://class.imooc.com/']
    # start_urls = ['https://class.imooc.com/']

    rules = (
        Rule(LinkExtractor(allow=r'course/list\?page=\d+'), callback='parse_item1', follow=True),
        Rule(LinkExtractor(allow=r'sort=0&unlearn=0&page=\d+'), callback='parse_item2', follow=True),
        Rule(LinkExtractor(allow=r'class.imooc.com/sale/\w'), callback='parse_mess', follow=True),
    )
    index = 0
    def parse_item2(self, response):
        
        data = response.xpath('/html/body/div[4]/div[1]/ul/li')
        for da in data:
            url = 'https://coding.imooc.com'+da.xpath('./a/@href').extract_first()
            yield scrapy.Request(url,callback=self.parse_mess,meta={'num':2})
    def parse_item1(self, response):
    
        data = response.xpath('//*[@id="main"]/div[3]/div[1]/a')
        for da in data:
            url = 'https:'+da.xpath('./@href').extract_first()
            yield scrapy.Request(url,callback=self.parse_mess,meta={'num':1})

    def parse_mess(self, response):
        item = ImoocScrapyItem()
        self.index +=1
        num=0
        try:
            num = response.meta['num']
        except Exception as e:
            num = 0
        
        if num == 0:
            item['id'] = self.index
            na = response.xpath('/html/body/div[5]/div[2]/div[1]/text()').extract_first()
            name = ''
            na = re.findall("[^\s\\n]",na)
            for n in na:
                name = name + n
            item['course_name'] = name
            item['cover_img_address'] = response.url
            dur = ''
            dur1 = str(response.xpath('/html/body/div[5]/div[3]/div[1]/div[2]/span[1]').get('data'))
            dur1 = re.findall('[\d\u4e00-\u9fa5]',dur1)
            for du in dur1:
                dur = dur + du
            item['course_duration'] = dur
            item['course_price'] = response.xpath('//*[@id="commonfixnav"]/div[2]/div/p[1]/span[1]/em/text()').extract_first()
            info = response.xpath('/html/body/div[5]/div[2]/div[2]/text()').extract()
            inn = ''
            for inf in info:
                inn = inn + inf
            item['course_information']=inn
            item['course_teacher'] = 'null'
            item['course_video_address'] = 'null'
            yield item
            
        elif num == 1:
            item['id'] = self.index
            item['course_name'] = response.xpath('//*[@id="main"]/div[1]/div[1]/div[2]/h2/text()').extract_first()
            item['cover_img_address'] = response.url
            item['course_duration'] = response.xpath('//*[@id="main"]/div[1]/div[1]/div[3]/div[3]/span[2]/text()').extract_first()
            item['course_price'] = '免费'
            info = response.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[1]/text()').extract_first()
            inf = ''
            try:
                infp = re.findall("[^\s\\n']+",info)
                
                for inn in infp:
                    inf = inf + inn
            except Exception as er:
                print(price,'   ',response.url,str(price))
                inf = ''
            item['course_information']=inf
            item['course_teacher'] = response.xpath('//*[@id="main"]/div[1]/div[1]/div[3]/div[1]/span[1]/a/text()').extract_first()
            item['course_video_address'] = 'https://www.imooc.com'+response.xpath('//*[@id="main"]/div[3]/div[1]/div[2]/div[1]/div[1]/a/@href').extract_first()
            yield item
        if num ==2:
            item['id'] = self.index
            item['course_name'] = response.xpath('/html/body/div[3]/div[1]/div[3]/h1/text()').extract_first()
            item['cover_img_address'] = response.url
            item['course_duration'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/span[4]/text()').extract_first()
            price  = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/text()').extract_first()
            if price is None:
                price = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/text()').extract_first()
                if price is None:
                    price = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/div/text()').extract_first()
            
            try:
                price = re.findall('￥\d+.\d+',price)[-1]
            except Exception as es:
                print(price,'   ',response.url,str(price))
                price = 'null'
            item['course_price'] = price
            inf = ''
            info = response.xpath('/html/body/div[3]/div[1]/div[1]/span/text()').extract_first()
            try:
                infp = re.findall("[^\s\\n']+",info)
                
                for inn in infp:
                    inf = inf + inn
            except Exception as ee:
                print(info,'   ',response.url,str(info))
                inf = 'null'
            item['course_information']=inf
            item['course_teacher'] = 'null'
            item['course_video_address'] = 'null'
            yield item






   