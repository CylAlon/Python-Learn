import json
import scipy
import utils
from settings import r

class SpiderManagerJson():
    def __init__(self,**kwags):
        self.response = kwags['response']
        self.num = 0
        self.ago_time = utils.get_ago_timetemp()
        self.flag = True
        self.items = kwags['items']
        self.name = kwags['name']
    def get_json_list(self,json_data):
        """
        将数据转换为json类型的数据并返回,该方法需要重写
        """
        return '该方法需要重写'
    def get_data_from_json(self,items,data):
        if self.num==0:
            pass
        # return '该方法需要重写'
        return items
    def get_item_list(self,data):
        """
        获取json中的数据
        """
        items = {
            'index':0, 
            'name':'', 
            'title':'',
            'time':'',
            'typ':'',
            'url':'',
            'date':''
        }
        items['name']=self.name
        items = self.get_data_from_json(items,data)
        
        items['date'] = utils.timeTemp_to_date(tim=items['time'])
        return items 
    
    def get_time_judge(self,tim):
        if tim<self.ago_time:
            self.flag = False
        else:
            self.flag = True
        return self.flag
    def set_num(self,num):
        self.num = num
    def set_page_flag(self,flag):
        self.flag = flag
    def get_page_flag(self):
        return self.flag
    def get_data_list(self):
        json_data = json.loads(self.response.text)
        return self.get_json_list(json_data)

    def get_items(self,item,item_list):
        # item['index'] = item_list['index']
        index = int(r.lindex('index',self.num))
        index +=1
        r.lset('index',self.num,index)
        item['index']=index
        item['name'] = item_list['name']
        item['title'] = item_list['title']
        item['time'] = item_list['date']
        item['mtype'] = item_list['typ']
        item['url'] = item_list['url']
        return item



# 实例例子
"""
    
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

"""
