# 绝对值
print(abs(-5))
# 四舍五入
print(round(10.5))

def add_num(a,b):
    return abs(a)+abs(b)

print(add_num(-1,2))
# 一下 高阶函数

def ad(a,b,c):
    return c(a)+c(b)

print(ad(-1,3,abs))
print(ad(0.1,56,round))

def ccc(a,b,c):
    return c(a,b)
print(ccc(2,2,pow))


# 内置高阶函数

# 1 map(fun,lst) 将传入的函数变量作用到lst变量的每个元素中，将结果组成迭代器返回
# 计算list1中每一个值的**2
list1=[1,2,3,4,5,6,7,8,9,10]
fun1=lambda x:x**2
print(list(map(fun1,list1)))

# 2 reduce(func(x,y),lst)  func必须是两个参数 每次func计算结果和下一个元素做累积计算
# 计算list1数字累加和 (1+2+3+4)
import functools
fun2=lambda a,b:a+b
print(functools.reduce(fun2,list1))

# 3 filter(func,lst) 过滤掉不满足的元素 返回fiter对象 可以使用list()转换
fun3=lambda x:x%2==0
print(list(filter(fun3,list1)))











