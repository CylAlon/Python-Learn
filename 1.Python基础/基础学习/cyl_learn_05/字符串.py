a = 'hello word!'
b = "hello python!"
print(type(a))
print(type(b))

c = '''你好吗'''
d = """
哈法按时
发士大     夫萨芬哈"""
print(type(c))
print(type(d))
print(d)

# 下标
str1="abcdefghijklmnopqrsv"
print(str1[0])
for i in str1:
    print(i,end='\t')
print('',end='\t')
print(str1[2:5])  # 结束的5索引位置不计算
print(str1[2:5:2])  # [开始索引：目标索引：步长]
print(str1[:5])  # 不屑开始默认从0开始
print(str1[:])  # 都不写 则选取所有
print(str1[::-1])  # 步长为负数 则倒叙 意思是倒叙步长为1
print(str1[-4:-1])  # 倒叙从下表为1-3
print(str1[-4:-1:1])  # 步长选取方向必须和选取方向一样

print("******************************")
"""
    字符串的方法
"""
st1 = "hello world and itcast and itheim and python"
# 查找下标  find
n1 = st1.find('and')  # 存在返回下标 不存在返回-1
print(n1)
# 查找下标 index()
n2 = st1.index('and')
print(n2)

# 查找出现次数

n2 = st1.count("and")
print(n2)
# rfind 和find一样 但是从右侧查询 rindex类似

# 字符串的修改
# 1、字符串序列.replace(就串，新串，替换次数) 替换
print(st1.replace('and','AND',2))  # 如果次数不写或者大于应有的次数 则全替换 返回新字符串 不改原来字符串

# 2、字符串.split(分割字符，次数) 会丢弃分割字符 不写次数或者大于次数则全分割
list1 = st1.split("and",2)
print(list1)
#splitline按行分割

# 3、字符串.join(多字符串组成的序列) 合并字符串为一个大字符串
liss = ['aa','bb','cc']
list2 = "...".join(liss)
print(list2)

# 大小写转换
zimu = "hello World UP data"
# 首字母大写
na = zimu.capitalize()
print(na)
# 小写转大写
ne = zimu.upper()
print(ne)
# 大写转小写
ne = zimu.lower()
print(ne)
# 删除首尾空白字符  lstrip() rstrip() strip()

ss = " hello wole "
print(ss)
print(ss.lstrip())
print(ss.rstrip())
print(ss.strip())

# 设置字符串对齐 ljust(长度，填充字符) rjust() center()
tt = "hello wo"
print(tt.ljust(10,'.'))
print(tt.rjust(10,'.'))
print(tt.center(10,'.'))
print(len(tt))  # 返回长度
print('wo' in tt)  # 查看wo是否在tt内
print('wo1' not in tt)

#startswith()判断是否以指定字符串开头
#endswith
