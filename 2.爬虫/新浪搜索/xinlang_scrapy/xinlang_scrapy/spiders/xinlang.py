# -*- coding:utf-8 -*-
'''
Descripttion: 新浪爬虫
Author: Cyl
Date: 2021-02-06 17:35:42
'''
import scrapy
import utils
import re
from items import XinlangScrapyItem
class XinlangSpider(scrapy.Spider):
    name = 'xinlang'
    allowed_domains = ['search.sina.com.cn','biz.finance.sina.com.cn']
    start_urls = ['https://search.sina.com.cn/','https://biz.finance.sina.com.cn/']
    findname = utils.getFindName()
    index1 = 0
    index2 = 0
    # https://search.sina.com.cn/?q=%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1&c=news&from=index
    # https://search.sina.com.cn/?q=%e4%b8%ad%e5%9b%bd%e7%94%b5%e4%bf%a1&c=news&from=index&col=&range=all&source=&country=&size=10&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page=3
    # https://search.sina.com.cn/?q=%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1&c=news&page=4

    # https://stock.finance.sina.com.cn/hkstock/quotes/02318.html
    # https://biz.finance.sina.com.cn/suggest/lookup_n.php?&q=中国移动

    def start_requests(self):
        path= ['','']
        io = [0,1]
        path[0] = utils.strJoin(self.start_urls[0],'?q=',self.findname,'&c=news&sort=time')
        path[1] = utils.strJoin(self.start_urls[1],'suggest/lookup_n.php?&q='+self.findname)
        index = 0
        for pa in path:
            index = index +1
            yield scrapy.Request(url=pa,callback=self.parse,meta={'index':index})


    def parse(self, response):
        item = XinlangScrapyItem()
        index = response.meta.get('index')
        # print('--------------------------------------')
        if index==1:
            # //*[@id="result"]/div[4]
            nod = response.xpath('//*[@id="result"]/div[@class="box-result clearfix"]')
            for ch in nod:
                str_re= ''
                time = ch.xpath('./h2/span').re('<span .*?>(.*?)</span>')
                if len(time)==0:
                    str_re = 'div/'
                    time = ch.xpath('./'+str_re+'h2/span').re('<span .*?>(.*?)</span>')
                    

                title = ch.xpath('./'+str_re+'h2/a').re('<a .*?>(.*?)<font .*?>(.*?)</font>(.*?)</a>')
                url = ch.xpath('./'+str_re+'h2/a/@href').extract_first()
                title = utils.strJoin(other=title,stype='other')
            
                # time = re.findall(r'[^\u4e00-\u9fa5]+',time[0])[0]
                time = time[0].split(' ')[1]
                self.index1+=1
                item['index'] = self.index1
                item['name'] = self.findname
                item['title'] = title
                item['time'] = time
                item['mtype'] = '新闻类型'
                item['url'] = url
                # print(item)
                yield item
                
                # //*[@id="result"]/div[4]/h2/span

            page_url = response.xpath('//*[@id="_function_code_page"]/a[last()]/@href').extract_first()
            if page_url!=None:
                # self.fl +=1
                page_url = utils.strJoin(self.start_urls[0],page_url)
                # print(self.fl)
                # print(page_url)
                yield scrapy.Request(url=page_url,callback=self.parse,meta={'index':index})
            
        elif index==2:
            # https://biz.finance.sina.com.cn/suggest/lookup_n.php?country=&q=中国平安=中国平安&t=keyword&c=all&k=中国平安&range=all&col=1_7&from=channel&ie=utf-8
            # print(f'------1------{response.url}')
            elm = response.xpath('/html/body/div[4]/div/label/a')
            # print(len(elm))
            for e in elm:
                url = e.xpath('./@href').extract_first()
                title = e.xpath('.//text()').extract()
                title = utils.strJoin(stype='other',other=title)
                self.index2+=1
                item['index'] = self.index2
                item['name'] = self.findname
                item['title'] = title
                item['time'] = None
                item['mtype'] = '股票类型'
                item['url'] = url
                yield item

            
            


        
        







# ['_DEFAULT_ENCODING', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_auto_detect_fun', '_body', '_body_declared_encoding', '_body_inferred_encoding', '_cached_benc', '_cached_decoded_json', '_cached_selector', '_cached_ubody', '_declared_encoding', '_encoding', '_get_body', '_get_url', '_headers_encoding', '_set_body', '_set_url', '_url', 'body', 'body_as_unicode', 'cb_kwargs', 'certificate', 'copy', 'css', 'encoding', 'flags', 'follow', 'follow_all', 'headers', 'ip_address', 'json', 'meta', 'replace', 'request', 'selector', 'status', 'text', 'url', 'urljoin', 'xpath']

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']