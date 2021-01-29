# 字典是键值对 没有下标
dict1 = {'name':'cyl','age':18,'num':'2018520653'}
print(type(dict1))
print(dict1)

# 建立空字典
dict2 = {}
print(dict2)
dict3 = dict()
print(dict3)

# 增
dict1['wei']=80  #增加
print(dict1)
# 修改
dict1['wei']=60  #修改
print(dict1)

# 删除字典 del  清空clear
dict4 = {'name':'cyl','age':18,'num':'2018520653'}
#del dict4
#print(dict4)
del dict4['name']
print(dict4)
dict4.clear()
print(dict4)

# 字典查找 key值查找  字典序列.get（key,默认值）查找
dict5 = {'name':'cyl','age':18,'num':'2018520653'}
print(dict5['name'])  # 如果不存在则报错
print(dict5.get('name'))
print(dict5.get('name1'))  # 如果不存在返回None
print(dict5.get('name1','sfsaf'))
# keys() 查找所有的key 返回可迭代的对象
print(dict5.keys())  # dict5.keys()这个可以使用for遍历

# values() 也返回可迭代的对象 所有的值
print(dict5.values())

# items() 返回键值对可迭代对象 里面的数据是元组
print(dict5.items())

# 字典遍历
# 遍历所有的key
dict6 = {'name':'cyl','age':18,'num':'2018520653'}
for i in dict6.keys():
    print(i,end='\t')
print('',end='\n')
for i in dict6.values():
    print(i,end='\t')
print('',end='\n')
for i in dict6.items():
    print(i,end='\t')
print('',end='\n')
# 遍历得到的数据后拆包
for i,m in dict6.items():
    print(f'第一个{i},第二个数据{m}',end='\t')
print('',end='\n')






