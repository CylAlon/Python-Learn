# -*- coding: utf-8 -*-
from faker import Faker
from settings import r
import os
import time

def getFindName():
    """返回需要查找的名字

    Returns:
        find_name: 需要查找的名字
    """
    return r.get('find_name')


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
    path = os.getcwd()
    file_path = path+'/file/'+getFindName()+'_'+spidername+'.html'
    with open(path+'/template.html','r') as f:
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
        week (int, optional): [description]. Defaults to 0.
        day (int, optional): [description]. Defaults to 0.
        hour (int, optional): [description]. Defaults to 0.
        minute (int, optional): [description]. Defaults to 0.
        second (int, optional): [description]. Defaults to 0.

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
    date_age = str(time.strftime('%Y-%m-%d',agotime))
    return date_age


def compare(date1,date2):
    """比较日期的大小

    Args:
        date1 ([type]): [description]
        date2 ([type]): [description]

    Returns:
        bool: [description]
    """
    st = time.strptime(date1,'%Y-%m-%d')
    sjc1 = time.mktime(st)
    st = time.strptime(date2,'%Y-%m-%d')
    sjc2 = time.mktime(st)
    return sjc1>sjc2#int(sjc1)>int(sjc2)

# if __name__ == '__main__':
    # p = compare('2021-2-3','2021-2-5')
    # print(p)
    # print(getDate())
    # z=dateAgo(day=1)
    # # print(z)
    # x = time.localtime()
    # y = time.strftime('%Y-%m-%d',x)
    # z = time.strptime(y,'%Y-%m-%d')
    # c = time.mktime(z)
    # print(x)
    # print(y)
    # print(z)
    # print(c)

#     z = strJoin(stype='other',other={'1','2','3'})
#     print(z)
    # 测试
    # userGentRandom()
    
    # path = writeFile('xinlang')
    # file = addFile(path,'hahahahahaha\n')

    # closeFile(file)
