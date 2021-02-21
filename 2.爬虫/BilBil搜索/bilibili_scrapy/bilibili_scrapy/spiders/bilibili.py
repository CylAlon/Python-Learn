import scrapy
import utils
import re
from settings import WEEK,DAY,HOUR,MINUTE,SECOND
from items import BilibiliScrapyItem

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    find_name = utils.getFindName()
    start_urls = [f'https://search.bilibili.com/all?keyword={find_name}&from_source=nav_search_new&order=pubdate&duration=0&tids_1=0']
    index = 0
    page = 1
    def parse(self, response):
        flag = True
        item = BilibiliScrapyItem()
        str_data = response.xpath('//*[@id="all-list"]/div[1]/ul/li')
        for da in str_data:
            title = da.xpath('./a/@title').extract_first()
            if self.find_name not in title:
                continue
            tim = da.xpath('./div/div[3]/span[3]/text()').extract_first()
            tim = re.findall('\d+-\d+-\d+',tim)[0]
            agotim = utils.dateAgo(week=WEEK,day=DAY,hour=HOUR,minute=MINUTE,second=SECOND)
            
            agotimetemp,_ = utils.tim_interconversion(agotim)
            sstimetemp,_ = utils.tim_interconversion(tim)
            self.index += 1
            if sstimetemp<agotimetemp:
                flag=False
                break
            url = da.xpath('./a/@href').extract_first()
            item['index'] = self.index
            item['name'] = self.find_name
            item['title'] = title
            item['time'] = tim
            item['mtype'] = '视频类型'
            item['url'] = url
            # item = BilibiliScrapyItem(index=self.index,name=self.find_name,title=title,mtype='视频类型',url=url)
            # utils.testWriteFile(str(item),False)
            yield item
        if flag: # 由于获得的信息远小于页数 故这里不需要判断
            self.page +=1
            urld = f'https://search.bilibili.com/all?keyword={self.find_name}&from_source=nav_search_new&order=pubdate&duration=0&tids_1=0&page={self.page}'
           
            yield scrapy.Request(url=urld,callback=self.parse,dont_filter=True)

        
