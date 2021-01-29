# input接受的数据都为字符串

a = int(input("input:"))
print(type(a))
a = str(a)
print(type(a))

b = 1.1
c = '1.1'
d = [1, 2, 3]
print(tuple(d))

# eval计算字符穿中有效Python表达式，并返回一个对象
str1 = '1'
str2 = '101'
str3 = '(100,200,300)'
str4 = "[1000,2000,3000]"
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
