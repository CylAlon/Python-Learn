# -*- coding:utf-8 -*-
'''
Descripttion:
Author: Cyl
Date: 2021-02-08 10:40:12
'''
import scrapy
import utils
import json
import re
from items import XueqiuScrapyItem
from settings import HOUR,WEEK,MINUTE,SECOND,DAY
import time as te


class XuehuSpider(scrapy.Spider):
    name = 'xueqiu'
    allowed_domains = ['xueqiu.com','xueqiu.com','xueqiu.com']
    start_urls = ['https://xueqiu.com/','https://xueqiu.com/','https://xueqiu.com/']
    find_name = utils.getFindName()
    find_id = utils.getFindId()
    index = [0,0,0,0]
    ajax_index=[0,0]
    

    def start_requests(self):
        path = ['' for s in range(3)]
        url_list = self.start_urls[0]
        path[2] = utils.strJoin(url_list,'today')
        path[1] = utils.strJoin(url_list,'k?q=',self.find_name) #,'#/timeline'
        path[0] = utils.strJoin(url_list,'hq')
        # path[0] = utils.strJoin(url_list,'stock/search.json?code=',self.find_name)
        
        index_yiled ={'index':-1}
        for pa in path:
            index_yiled['index'] += 1
            yield scrapy.Request(url=pa,callback=self.parse,meta=index_yiled)

    def parse(self, response):
        index= response.meta['index']
        # print(f'index = {index}  url = {response.url}')
        if index ==0:
            ajax_url = utils.strJoin(self.start_urls[0],'S/',self.find_id)  #为了和其他两个匹配 这里多操作一步
            yield scrapy.Request(url=ajax_url,callback=self.get_id_parse,meta={'index':index,'flag':True})
        elif index ==1:
            ajax_url = self.getAjaxUrl(index=index,ajax_index=1)
            # print(ajax_url)
            yield scrapy.Request(url=ajax_url,callback=self.talk_parse,meta={'index':index})
            
        elif index ==2:
            ajax_url = self.getAjaxUrl(index=index,ajax_index=-1)
            yield scrapy.Request(url=ajax_url,callback=self.json_parse,meta={'index':index})
    def json_parse(self, response):
        flg = True
        item = XueqiuScrapyItem()
        index = response.meta['index']
        json_data = json.loads(response.body_as_unicode())
        # next_max_id = re.findall(r"'next_max_id':\s*(\d*),",json_data)
        # title = re.findall(r"'original_status'\s*:\s*{.*?'title'\s*:\s*(.*?)\s*,.*?}",json_data)
        # zhenwen = re.findall(r"'original_status'\s*:\s*{.*?'description'\s*:\s*(.*?)\s*,.*?}",json_data)
        next_max_id = json_data['next_max_id']
        it = json_data['items']
        for i in it:
            self.index[index] +=1
            it_data = str(i)
            # utils.testWriteFile(it_data)
            time = re.findall(r"'timeBefore'\s*:\s*'(.*?)'\s*,",it_data)[-1]
            time = time.split(' ')
            # print(time)
            if len(time)!=1:
                # if time[0]=='今天':
                time[0] = utils.getDate()
                time = utils.strJoin(time[0],' ',time[-1])
                # else:
                #     time[0] = '2021-'+time[0]
                #     time = utils.strJoin(time[0],' ',time[-1])
            else:
                mi = re.findall(r'\d+',str(time))[-1]
                
                time = utils.dateAgo(minute=int(mi))

            ago_time = utils.dateAgo(week=WEEK,day=DAY,hour=HOUR,minute=MINUTE,second=SECOND)
            if utils.compare(ago_time,time):
                flg=False
                break
            title = re.findall(r"'original_status'\s*:\s*{.*?'title'\s*:\s*'(.*?)'\s*,.*?}",it_data)[-1]
            if title=='':   
                title = re.findall(r"original_status'\s*:\s*{.*?'description'\s*:\s*'(.*?)'\s*,.*?}",it_data)[-1]
            url = re.findall(r"'target'\s*:\s*'/(.*?)'",it_data)[-1]
            item['index'] = self.index[index]
            item['name'] = self.find_name
            item['title'] = title
            item['time'] = time
            item['mtype'] = '雪球热帖'
            item['url'] =  self.start_urls[0]+url
            # utils.testWriteFile(str(item),False) #-----------------------------------------------------------------
            yield item

        if next_max_id>-1 and flg==True:
            ajxjzul = self.getAjaxUrl(index=index,ajax_index=next_max_id)
            yield scrapy.Request(url=ajxjzul,callback=self.json_parse,meta={'index':index})
        else:
            ajxjzul = self.getAjaxUrl(index=3,ajax_index=-1)
            yield scrapy.Request(url=ajxjzul,callback=self.x724_prase,meta={'index':3})
            
    def x724_prase(self, response):
        flg = True
        item = XueqiuScrapyItem()
        index = response.meta['index']
        str_data = response.body_as_unicode()
        next_max_id = int(re.findall(r'"next_max_id":(\d*)',str_data)[-1])
        json_data = json.loads(str_data)
        it = json_data['items']
        for i in it:
            self.index[index] +=1
            it_data = str(i)
            time = int(re.findall(r"'created_at':\s*(\d*),",it_data)[-1])/1000
            time_date = utils.timeTemp_to_date(tim=time)
            time = utils.dateAgo(week=WEEK,day=DAY,hour=HOUR,minute=MINUTE,second=SECOND)
    
            if utils.compare(time,time_date):
                flg = False
                break
            url = re.findall(r"'target':\s*'(.*?)',",it_data)[-1]
            title = re.findall(r"'text':\s*'(.*?)',",it_data)[-1]
            item['index'] = self.index[index]
            item['name'] = self.find_name
            item['title'] = title
            item['time'] = time_date
            item['mtype'] = '7x24快讯'
            item['url'] =  url
            # utils.testWriteFile(str(item),False) #-----------------------------------------------------------------
            yield item
        if next_max_id>-1 and flg==True:
            ajxjzul = self.getAjaxUrl(index=index,ajax_index=next_max_id)
            yield scrapy.Request(url=ajxjzul,callback=self.x724_prase,meta={'index':index})

    def talk_parse(self,response):
        flag = True #修改过
        page_flag = True
        tim_in = ['秒前','分钟前','今天']
        item = XueqiuScrapyItem()
        index = response.meta['index']
        str_data = response.text


        succ = re.findall(r'"success":(.*?)}',str_data)
        if len(succ)!=0:
            if succ[-1]=='false':
                ajax_url = response.url 
                yield  scrapy.Request(url=ajax_url,callback=self.talk_parse,meta={'index':index},dont_filter=True) # 重发
        # utils.testWriteFile(str(str_data),False)
        else:
            maxpage = re.findall(r'"maxPage":(\d+),',str_data)[-1]
            mpage = re.findall(r'"page":(\d+),',str_data)[-1]
            # it = re.findall(r'\[.*?\{([^{}])\},.*?\]',str_data)
            json_data = json.loads(str_data)
            tii = 0
            for i in json_data['list']:
                st_i = str(i)
                tim = re.findall(r"'timeBefore': '(.*?)',",st_i)[-1]
                flag = False
                for p in range(len(tim_in)):
                    if tim_in[p] in tim:
                        flag=True
                        num = re.findall(r'[\d]+',tim)[-1]
                        if p==0:
                            tii = te.time()-int(num)
                        elif p==1:
                            tii = te.time()-int(num)*60
                        elif p ==2:
                            nu = tim.split(' ')[-1]
                            ti = te.localtime()
                            da = te.strftime('%Y-%m-%d',ti)
                            date = str(da)+' '+nu
                            date = te.strptime(date,'%Y-%m-%d %H:%M')
                            tii = te.mktime(date)
                    else:
                        pass
                if flag!=True:
                    print('超过时间限制')
                    page_flag = False
                    break
                age_ti = utils.dateAgo(week=WEEK,day=DAY,hour=HOUR,minute=MINUTE,second=SECOND)
                age_ti = te.strptime(age_ti,'%Y-%m-%d %H:%M')
                age_ti = te.mktime(age_ti)
                if tii>age_ti:
                    try:
                        title = re.findall(r"'title': '(.*?)',",st_i)[-1]
                    except Exception as ex:
                        title=''
                    #---------------------------------------以下需要修改  
                    # text = re.findall(r"'text':.*?>(.*?)<.*?,",st_i)[-1]   #------------------需要修改
                    text = re.findall(r"'text':(.*?),",st_i)[-1] #------------------需要修改
                    text = re.compile('<[^>]+>').sub('',text)
                    
                    url = self.start_urls[0] +re.findall(r"""'target':\s*'/(.*?)',""",st_i)[-1]
                    self.index[index]+=1
                    item['index'] = self.index[index]
                    item['name'] = self.find_name
                    item['title'] = title+'\n'+text
                    item['time'] = tim
                    item['mtype'] = '讨论'
                    item['url'] =  url
                    # utils.testWriteFile(str(item),False)·
                    yield item
                else:
                    page_flag = False
            # item = XueqiuScrapyItem()

            if int(mpage)<int(maxpage) and page_flag!=False:
                pg = int(mpage)+1
                ajax_url = self.getAjaxUrl(index=index,ajax_index=pg)
                yield  scrapy.Request(url=ajax_url,callback=self.talk_parse,meta={'index':index}) 
    def get_id_parse(self, response):
        # article = response.xpath('//*[@id="app"]/div[2]/div[2]/div[9]/div[3]')
        # utils.testWriteFile(str(response.text),False,hz='html')
        # print(response.url)
        # print(len(article))
        # print(article)
        # https://xueqiu.com/statuses/search.json?count=10&comment=0&symbol=SH601318&hl=0&source=all&sort=time&page=1&q=&type=11
        index = response.meta['index']
        flg = response.meta['flag']
        flag = True
        page_flag = True
        tim_in = ['秒前','分钟前','今天']
        item = XueqiuScrapyItem()
        # print('---flg = ',flg)
        if flg==True:
            flg = False
            # print('重发-----------')
            ajax_url = self.getAjaxUrl(index=index,ajax_index=1)
            # print(ajax_url)
            yield scrapy.Request(url=ajax_url,callback=self.get_id_parse,meta={'index':index,'flag':flg})
        
        else:
            succ = re.findall(r'"success":(.*?)}',response.text)
            if len(succ)!=0:
                # print('获取失败')
                if succ[-1]=='false':
                    ajax_url = response.url 
                    yield  scrapy.Request(url=ajax_url,callback=self.get_id_parse,meta={'index':index,'flag':flg},dont_filter=True) # 重发
            else:
                str_data = response.text
                maxpage = re.findall(r'"maxPage":(\d+),',str_data)[-1]
                mpage = re.findall(r'"page":(\d+),',str_data)[-1]
                json_data = json.loads(str_data)
                tii = 0
                for i in json_data['list']:
                    st_i = str(i)
                    tim = re.findall(r"'timeBefore': '(.*?)',",st_i)[-1]
                    flag = False
                    for p in range(len(tim_in)):
                        if tim_in[p] in tim:
                            flag=True
                            num = re.findall(r'[\d]+',tim)[-1]
                            if p==0:
                                tii = te.time()-int(num)
                            elif p==1:
                                tii = te.time()-int(num)*60
                            elif p ==2:
                                nu = tim.split(' ')[-1]
                                ti = te.localtime()
                                da = te.strftime('%Y-%m-%d',ti)
                                date = str(da)+' '+nu
                                date = te.strptime(date,'%Y-%m-%d %H:%M')
                                tii = te.mktime(date)
                        else:
                            pass
                    if flag!=True:
                        print('超过时间限制')
                        page_flag = False
                        break
                    age_ti = utils.dateAgo(week=WEEK,day=DAY,hour=HOUR,minute=MINUTE,second=SECOND)
                    age_ti = te.strptime(age_ti,'%Y-%m-%d %H:%M')
                    age_ti = te.mktime(age_ti)
                    if tii>age_ti:
                        try:
                            title = re.findall(r"'title': '(.*?)',",st_i)[-1]
                        except Exception as ex:
                            title=''
                        text = re.findall(r"'text':(.*?),",st_i)[-1] #------------------需要修改
                        text = re.compile('<[^>]+>').sub('',text)
                        
                        url = self.start_urls[0] +re.findall(r"""'target':\s*'/(.*?)',""",st_i)[-1]
                        self.index[index]+=1
                        item['index'] = self.index[index]
                        item['name'] = self.find_name
                        item['title'] = title+'\n'+text
                        item['time'] = tim
                        item['mtype'] = '内部讨论'
                        item['url'] =  url
                        # utils.testWriteFile(str(item),False)
                        yield item
                    else:
                        page_flag = False
                # item = XueqiuScrapyItem()

                if int(mpage)<int(maxpage) and page_flag!=False:
                    pg = int(mpage)+1
                    ajax_url = self.getAjaxUrl(index=index,ajax_index=pg)
                    yield  scrapy.Request(url=ajax_url,callback=self.get_id_parse,meta={'index':index,'flag':flg}) 


    def getAjaxUrl(self,index,ajax_index=-1):
        url = ''
        if index == 0:
            url = f'{self.start_urls[0]}statuses/search.json?count=10&comment=0&symbol={self.find_id}&hl=0&source=all&sort=time&page={ajax_index}&q=&type=11'
        elif index ==1:
            url = f'{self.start_urls[0]}statuses/search.json?sort=time&source=all&q={self.find_name}&count=20&page={ajax_index}'
        elif index==2:
            url = f'{self.start_urls[0]}statuses/hot/listV2.json?since_id=-1&max_id={ajax_index}&size=15'
        elif index ==3:
            url = f'{self.start_urls[0]}statuses/livenews/list.json?since_id=-1&max_id={ajax_index}&size=15'

        return url


