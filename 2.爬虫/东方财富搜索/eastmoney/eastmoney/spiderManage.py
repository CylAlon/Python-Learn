import json
import scipy
import utils
from settings import r


class SpiderManagerJson():
    def __init__(self, **kwags):
        self.response = kwags['response']
        self.num = 0
        self.ago_time = utils.get_ago_timetemp()
        self.flag = True
        # self.items = kwags['items']
        self.name = kwags['name']

    # def get_json_list(self, json_data):
    #     """
    #     将数据转换为json类型的数据并返回,该方法需要重写
    #     """
    #     return '该方法需要重写'
    def get_data_list(self,num):
        # 该方法可被重写
        json_data = json.loads(self.response.text)
        return json_data

    def get_data_from_json(self, item, data):
        if self.num == 0:
            pass
        # return '该方法需要重写'
        return items

    def get_item_list(self, data):
        """
        获取json中的数据
        """
        items = {
            'index': 0,
            'name': '',
            'title': '',
            'time': '',
            'typ': '',
            'url': '',
            'date': ''
        }
        index = int(r.lindex('index', self.num))
        index += 1
        r.lset('index', self.num, index)
        items['index'] = index
        items['name'] = self.name
        items = self.get_data_from_json(items, data)

        items['time'],items['date'] = utils.tim_interconversion(tim=items['time'])
        return items

    def get_time_judge(self, tim):
        if tim < self.ago_time:
            self.flag = False
        else:
            self.flag = True
        return self.flag

    def set_num(self, num):
        self.num = num

    def set_page_flag(self, flag):
        self.flag = flag

    def get_page_flag(self):
        return self.flag



    def get_items(self, item, item_list):
        item['index'] = item_list['index']
        item['name'] = item_list['name']
        item['title'] = item_list['title']
        item['time'] = item_list['date']
        item['mtype'] = item_list['typ']
        item['url'] = item_list['url']
        return item


# 实例例子
"""
    
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
            
        return item

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
"""
