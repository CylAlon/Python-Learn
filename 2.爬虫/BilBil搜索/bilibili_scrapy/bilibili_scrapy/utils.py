# -*- coding: utf-8 -*-
'''
Descripttion:
Author: Cyl
'''
from faker import Faker
from settings import r,COOKIES
import os
import time

def getFindName():
    """返回需要查找的名字

    Returns:
        find_name: 需要查找的名字
    """
    return r.get('find_name')
def getFindId():
    """返回需要查找id

    Returns:
        find_name: 需要查找的id
    """
    return r.get('find_id')
def getCookie(cookie = COOKIES):
    return {data.split('=')[0]:data.split('=')[-1] for data in cookie.split(';')}

def userGentRandom():
    """随机生成user_agent

    Returns:
        [type]: str
    """
    fk = Faker()
    return fk.firefox()

def writeFile(spidername = ''):
    """将模版html写入新的文件中

    Args:
        spidername (str, 爬虫名): [description]. Defaults to ''.

    Returns:
        _io.TextIOWrapper: 文件类型
    """
    ht = ''
    pa = os.getcwd()
    path = pa + '/file'
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = path+'/'+getFindName()+'_'+spidername+'.html'
    with open(pa+'/template.html','r') as f:
            ht = f.read()
    with open(file_path,'w') as f:
        f.write(ht)
    nfile = open(file_path,'a+')
    return nfile

def addFile(file,item):
    """对文件追加信息

    Args:
        path (str): 文件路径   
        item (disc, optional): 文件内容. Defaults to ''.
    """
    content = f"\
        <tr class='tx'>\n\
            <td>{item['index']}</th>\n\
            <td>{item['name']}</th>\n\
            <td>{item['title']}</th>\n\
            <td>{item['time']}</th>\n\
            <td>{item['mtype']}</th>\n\
            <td><a href={item['url']}>点击</a></th>\n\
        </tr>\n\
        "
    
    file.write(content)
    # return file


def closeFile(file,content='\
    </table>\n\
</body>\n\
</html>'):
    """关闭打开的文件,并将末尾字符串补齐

    Args:
        file (io.TextIOWrapper): 文件对象
        content (str): 需要输入的内容
    """
    file.write(content)
    file.close()

def strJoin(*args,stype='args',other=[]):
    """字符串连接

    Returns:
        str: 连接完成的字符串
    """
    result = ''
    otype = args
    if stype == 'other':
        otype = other
    for st in otype:
        result = result +st
        
    return result

def getDate():
    """返回当前日期

    Returns:
        str: [description]
    """
    ti = time.localtime()
    return time.strftime('%Y-%m-%d',ti)


def dateAgo(week=0,day=0,hour=0,minute=0,second=0):
    """返回多少时间之前

    Args:
        TIME_LISTS = {
            'week':0,
            'day':0,
            'hour':10,
            'minute':0,
            'seconds':0
        }
    Returns:
        str: 返回日期
    """
    moment_time = time.time()
    second_num = second
    minute_num = minute*60
    hour_num = hour*60*60
    day_num = day*60*60*24
    week_num = week*60*60*24*7
    all_time = second_num+minute_num+hour_num+day_num+week_num
    time_ago = moment_time-all_time
    agotime = time.localtime(time_ago)
    date_age = str(time.strftime('%Y-%m-%d %H:%M',agotime))
    return date_age


def compare(date1,date2):
    """比较日期的大小

    Args:
        date1 ([type]): [description]
        date2 ([type]): [description]

    Returns:
        bool: [description]
    """
    formate1='%Y-%m-%d %H:%M'
    formate2='%Y-%m-%d'
    st = ''
    try:
        st = time.strptime(date1,formate1)
    except Exception as e1:
        st = time.strptime(date1,formate2)

    sjc1 = time.mktime(st)
    try:
        st = time.strptime(date2,formate1)
    except Exception as e1:
        st = time.strptime(date2,formate2)
    sjc2 = time.mktime(st)
    return sjc1>sjc2#int(sjc1)>int(sjc2)

def timeTemp_to_date(formate = '%Y-%m-%d %H:%M',tim=time.time()):
    lo = time.localtime(tim)
    return time.strftime(formate,lo)



def match_double_out_layer_len(st,format):
    """匹配成对的字符 返回最外层括号或者引号的对数

    Args:
        st (str): 需要匹配的字符串
        format (str): 需要匹配的符号

    Returns:
        int: 返回成对的数量
    """
    index = 0
    fmt = ['()','（）','[]','{}',"''",'""','‘’','“”']

    fstr = '(['+format+'])+'

    li = re.findall(fstr,st)

    if format in fmt:
        inn = [] # 创建栈
        
        inn.append(li.pop()) # 将传进来的数据出栈在入栈inn

        while len(li)>0:
            li_pop = li.pop()
            if format.index(li_pop)==0:
                inn_pop = inn.pop() 
            else:
                inn.append(li_pop)
            if len((inn))==0:
                index += 1
    return index
            
def tim_interconversion(tim):
    """对传入的时间处理

    Args:
        tim (str): 日期
            2020-01-01 18:12:13
            2020/01/01 18:12:13
            2020,01,01 18:12:13
            2020.01.01 18:12:13
            2020年01月01日 18:12:13

            2020-01-01 18时12分13秒
            2020/01/01 18时12分13秒
            2020,01,01 18时12分13秒
            2020.01.01 18时12分13秒
            2020年01月01日 18时12分13秒

            2020-01-01 18:12
            2020/01/01 18:12
            2020,01,01 18:12
            2020.01.01 18:12
            2020年01月01日 18:12

            2020-01-01 18时12分
            2020/01/01 18时12分
            2020,01,01 18时12分
            2020.01.01 18时12分
            2020年01月01日 18时12分

            今天12:10:11
            今天 12:10:11
            今天12:10
            今天 12:10
            2秒钟前
            2秒前
            2 秒钟前
            2 秒前
            2分钟前
            2分前
            2 分钟前
            2 分前
            2小时前
            2 小时前

    Returns:
        int str: 返回时间戳和日期
    """


    format = [
        '%Y-%m-%d %H:%M:%S',
        '%Y/%m/%d %H:%M:%S',
        '%Y,%m,%d %H:%M:%S',
        '%Y.%m.%d %H:%M:%S',
        '%Y年%m月%d日 %H:%M:%S',

        '%Y-%m-%d %H时%M分%S秒',
        '%Y/%m/%d %H时%M分%S秒',
        '%Y,%m,%d %H时%M分%S秒',
        '%Y.%m.%d %H时%M分%S秒',
        '%Y年%m月%d日 %H时%M分%S秒',

        '%Y-%m-%d %H:%M',
        '%Y/%m/%d %H:%M',
        '%Y,%m,%d %H:%M',
        '%Y.%m.%d %H:%M',
        '%Y年%m月%d日 %H:%M',

        '%Y-%m-%d %H时%M分',
        '%Y/%m/%d %H时%M分',
        '%Y,%m,%d %H时%M分',
        '%Y.%m.%d %H时%M分',
        '%Y年%m月%d日 %H时%M分',

        '%Y-%m-%d',
        '%Y/%m/%d',
        '%Y,%m,%d',
        '%Y.%m.%d',
        '%Y年%m月%d日'
    ]
    strformat = [
        '今天',
        '今日',
        '秒钟前',
        '秒前',
        '分钟前',
        '分前',
        '小时前',
    ]
    struct_time = ''
    flag = False
    for fmt in format:
        try:
            struct_time = time.strptime(tim,fmt)
            flag = True
            break
        except Exception as e:
            flag = False
    if not flag:
        for sfmt in strformat:
            fl = True
            if sfmt in tim:
                flag=True
                if sfmt=='今天' or sfmt=='今日':
                    sy = re.findall('\d+:\d+:\d+|\d+:\d+|\d+',tim)
                    t =''
                    for s in range(len(sy)):
                        t = t+sy[s]
                        if s!=len(sy)-1:
                            t = t+':'
                    ts = time.localtime(time.time())
                    stau_time = time.strftime('%Y-%m-%d',ts)+' '+t
                    fl = ['%Y-%m-%d %H:%M:%S','%Y-%m-%d %H:%M','%Y-%m-%d %H']
                    for iu in range(3):
                        try:
                            struct_time = time.strptime(stau_time,fl[iu])
                            break
                        except Exception as ex:
                            pass
                            # print('tim_interconversion方法时间错误')

                elif sfmt=='秒钟前':
                    temp = time.time()-int(re.findall('\d+',tim)[-1])
                    struct_time = time.localtime(temp)
                elif sfmt=='秒前':
                    temp = time.time()-int(re.findall('\d+',tim)[-1])
                    struct_time = time.localtime(temp)
                elif sfmt=='分钟前':
                    temp = time.time()-int(re.findall('\d+',tim)[-1])*60
                    struct_time = time.localtime(temp)
                elif sfmt=='分前':
                    temp = time.time()-int(re.findall('\d+',tim)[-1])*60
                    struct_time = time.localtime(temp)
                elif sfmt=='小时前':
                    temp = time.time()-int(re.findall('\d+',tim)[-1])*60*60
                    struct_time = time.localtime(temp)
                else:
                    flag=False
                    fl = False
                
            else:
                flag=False
                fl = False
            if fl:
                break
    if flag:
        timestamp = time.mktime(struct_time)
        date = time.strftime('%Y-%m-%d %H:%M:%S',struct_time)
        return timestamp,date

    return None,None












def testWriteFile(file,flag = True,hz='json'):
    """测试使用

    Args:
        file ([type]): [description]
    """
    if flag == True:
        with open('test.json','w') as f:
            f.write(file)
    else:
        with open(f'test.{hz}','a+') as f:
            f.write(file)


