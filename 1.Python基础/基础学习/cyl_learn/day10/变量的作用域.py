
a=1

def ss():
    b=2
    print(b+a)


ss()


def dd():
    print(a)

def gg():
    a=2   # 在方法体里面就算是a 但是这个a还是局部变量
    print(a)

print("------")
print(a)

dd()
gg()

def qq():
    global a  # 这里声明a是全局变量
    a=3
    print(a)
qq()

def wz(na,nb,nc):
    print(f'{na}+{nb}+{nc}')

wz(10,20,30)

wz(na=10,nc=20,nb=30)
wz('xiaom',nc=20,nb=30)


def ws(na,nb='10',nc=20):  # 缺省参数
    print(f'{na}+{nb}+{nc}')
ws(10,20,30)
ws(2)


# 不定长的参数 *args  **args  会形成一个元组
def mo(*args):  # 位置定义法
    print(args)

mo(6,7)

def mr(**kwargs): # 关键字定义法 返回一个字典
    print(kwargs)

mr(name='tom')


#  拆包
# 元组拆包 函数返回的元素 将其拆包
def re():
    return 100,200

print(re())
rul1,rul2=re()  # 拆包
print(f'{rul1},{rul2}')
# 字典拆包
def zd():
    return {'nome':'cyl','age':18}

print(zd())
r3,r4=zd()  # 获得的是key值
print(f'{r3},{r4}')
print(zd()[r3])
print(zd()[r4])


# 交换变量
# 方法1 借助第三个变量 此处略
# 方法2
a,b=1,2  # 定义两个变量 并赋值
a,b=b,a  # 赋值
print(f'a={a} b={b}')


# 引用  值都是靠传递来引用的 id()方法可以看两个变量是否为同一个值的引用
a=10
b=10
print(id(a))
print(id(b))
b=20
print(id(a))
print(id(b))
b=a
print(id(a))
print(id(b))

aa=[10,20]
bb=aa
print(id(aa))
print(id(bb))

aa=(10,20)
bb=aa
print(id(aa))
print(id(bb))

s=100
print(id(s))
s+=1  # 修改值后地址发生变化 因为100是一个不可变的 100 101会按照两个地址存 但是列表就不一样了
print(id(s))

# 列表 字典 集合 可变类型  整型 浮点 字符串 元组类型不可变类型

num = 0

def up():
    global num
    num = 2

def do():
    print(f'do{num}')


up()

do()






