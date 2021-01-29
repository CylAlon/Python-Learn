age = 18
name = "cyl"
weight = 100.0
number = 1
# 1、今年我的年龄是x岁 --%d
print("今年我的年龄是%d岁" % age)
# 2、我的名字是x
print("我的名字是%s" % name)
# 3、我的体重是x公斤
print("我的体重是%.2f公斤" % weight)  # %.2f保留两位小数
# 4、我的学号是x
print("我的学号是%03d" % number)  # 在前面补0
# 5、我的名字是x，今年x岁了
print("我的名字是%s，今年%d岁了" % (name, age))
# 6、我的名字是x，今年x岁了，体重是x公斤，学号是x
print("我的名字是%s，今年%d岁了，体重是%.2f公斤，学号是%03d" % (name, age,weight, number))

# f表达式  语法： f'{表达式}' 更高效
print(f'我的名字是{name}，今年{age}岁了，体重是{weight}公斤，学号是{number}')




