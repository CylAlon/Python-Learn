
# 查
list1 = ['cyl','nihao','cqkj']
print(list1[0])
print(list1[2])
print(list1)

# 查找函数  index()  count() 与字符串一样

# len 返回看i额表长度
print(len(list1))
# 判断某个数据是否存在 in  not in
print('cyl' in list1)
print('cyl1' in list1)
print('cyl1' not in list1)

# 增加数据 列表序列.append(数据) 在末尾添加数据
list2 = ["s","sd"]
list1.append("xiaoing")
print(list1)
list1.append(list2)
print(list1)
# 增加数据 列表序列.extend() 如果是一个序列 则逐一添加(如果被添加的是一个列表，则将列表中的值每一个提出来添加到首列表中)
list3 = ["s","sd"]
list4 = ["55","464"]
list3.extend("xiaoing")  # 字符串也是一个序列
print(list3)
list3.extend(["xiaoing","xiaohong"])  # 字符串也是一个序列
print(list3)
list3.extend(list4)
print(list3)

# 新增数据 列表序列.insert(下标位置，数据)
list5 = ["顺风顺水","胜丰是"]
list5.insert(1,"sfs")
print(list5)

#  删除 del 目标 ;  列表序列.pop()伤处指定下标（默认最后）返回被删除的元素
# remove() 移除列表中某个数据的第一个匹配值  列表序列.remove(数据)
# clear() 清空列表
'''
del list3
print(list3)
'''
del list5[0]
print(list5)
list6 = ['sdfsa','adfs','safsfs','afsdfa','afsf']
print(list6.pop())
print(list6.pop(0))

list6.remove('adfs')
print(list6)

list7 = [1,5,9,2,7,6,4]
# 列表修改
list7[6]=3
print(list7)
# 列表倒叙 revrrse()
list7.reverse()
print(list7)
# 列表排序 列表序列.sort(key=None,reverse=Flase)
#  reverse表示排列规则 True 降序 Flase升序(默认）
list7.sort(reverse=True)  # 默认升序
print(list7)

# 列表复制 copy()

# 列表的循环遍历 while  for (我自己建议使用for(应位不用创建索引))
# 一般使用for循环

# 列表嵌套 获取值和数组类似



