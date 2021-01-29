
# + 合并
str1=[0,1,2,3]
str2=[4,5,6,7]
tuple1=(0,1,2,3)
tuple2=(4,5,6,7)
dict1={'name':'das'}
dict2={'age':18}
print(str1+str2)
print(tuple1+tuple2)
# print(dict1+dict2)  # 字典不允许合并

# * 复制 字典不能复制
print(str1*5)

# len()元素个数 del del() 删除 max() 最大值 min()最小值 range(start,end,step) enumerate()
# enumerate(课遍历的对象，start=0)  start可以不写
list1 =['a','b','c','d','e']
for i in enumerate(list1):
    print(i)
for index,char in enumerate(list1,start=1):
    print(f'下表是{index},对应的字符是{char}')

# 容器类型转换
list2=[10,20]
set2={100,200}
tu=(40,50)

#print(type(tuple(list2)))
#print(type(list(set2)))
#print(type(tuple(set2)))

# 列表 字典 集合 的推导式

# while 循环实现
# 0 需求 获得0 1 2 3 4 的一个列表
# 1 准备一个空列表
lis1=[]
# 2 将有规律的数据写到列表中
#   1 while 实现
i=0
while i<10:
    lis1.append(i)
    i+=1
print(lis1)

#   2 for实现
lis1.clear()
for i in range(10):
    lis1.append(i)
print(lis1)
#  列表表达式写法-----------------------
lis1.clear()
lis1=[i for i in range(10)]  # 这里[]里面是for循环后返回i 获得的i在左边
print(lis1)
#  带if的列表推导式
#  若创建偶数列表 1.方法1写步长为2 2.方法2 for+if
lis1.clear()
lis1=[i for i in range(0,10,2)]  # 方法1
print(lis1)

lis1=[i for i in range(10) if i % 2 == 0]
print(lis1)
# 多for推导式和for循环嵌套类似 改写就完成了

# 字典推导式
li1=['name','age','gender']
li2=['cyl',18,'man']
# 将上面两个列表合并为一个字典
# 使用for循环
dic3={li1[i]:li2[i] for i in range(len(li1)) }
print(dic3)

# 提取字典中的目标数据
dict5 = {'xm':89,'zs':90,'ls':46}
di5={key:value for key,value in dict5.items() if value>80}
print(di5)
