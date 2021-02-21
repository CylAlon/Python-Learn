# -*- coding:utf-8 -*-
'''
Descripttion: 
Author: Cyl
Date: 2021-02-20 20:45:37
'''

"""
i: 猫
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16138249171105
sign: 48157a923c10d143bf6c24b1ece359c2
lts: 1613824917110
bv: 51c157d16589f89e7109f585b4553d23
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION

i: 狗
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb

salt: 16138251640838
sign: e4df44fea6595c058283d76e83596351
lts: 1613825164083

bv: 51c157d16589f89e7109f585b4553d23
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME

经过分析 salt和lts类似时间戳，故唯一需要解密的时sign
"""

import random
import time
from hashlib import md5
import requests
import json


if __name__ == '__main__':
    e = input('请输入你需要查询的单词:')
    rand = random.randint(0,9)
    timetemp = int(time.time()*1000)
    r = str(timetemp) #'%.0f'%(timetemp*1000)
    i = r+str(rand)
    
    salt = i
    lts = r
    
    mdstr = "fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@"
    md = md5()
    md.update(mdstr.encode())
    sign = md.hexdigest()
    params = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': '51c157d16589f89e7109f585b4553d23',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-300475610@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=237575440.3607396; JSESSIONID=aaaDlcawqJMr-4zhBD-Ex; ___rl__test__cookies=1613831752729',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    }
    response = requests.post(url,headers=headers,data=params)
    json_data = response.json()
    print('翻译结果为：',json_data['translateResult'][0][0]['tgt'])

