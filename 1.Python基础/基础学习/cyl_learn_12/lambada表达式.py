""""
    如果一个函数自由一个返回值 且只有一句代码 就可以使用lambada表达式简化
    语法： lambada 参数列表：表达式
    注意：参数可有可无   能接受任何数量的参数 但是只能返回一个表达式的值
    lambda表达式还有个名字娇函数别名

"""

# 函数法
def fn1():
    return 200
print(fn1())

# lambada 法
fin2=lambda :100
print(fin2)
print(fin2())

# 计算a+b
def js(a,b):
    return a+b

print(js(5,6))

js2=lambda a,b:a+b

print(js2(7,8))

# lamdba表达式默认参数
fin3=lambda a,b,c=100:a+b+c
print(fin3(1,2))

# lamdba 表达式的可边参数
fin4=lambda *args:args
print(fin4(1,2))
fin5=lambda **kargs:kargs
print(fin5(name='cyl'))

# lambda 带判断if

fin6=lambda a,b:a if a>b else b

print(fin6(10,50))

# 字典key排序
student=[
    {'name':'cyl','age':18},
    {'name':'cyl1','age':20}
]

student.sort(key=lambda a : a['age'])
print(student)




















