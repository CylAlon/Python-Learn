"""
1、不同的变量存不同的数据
2、验证这些数据十什么类型---检查数据类型方法--type(数据)
"""
num1 = 1
print(type(num1))
num2 = 2.1
print(type(num2))
num3 = "字符串"
print(type(num3))
num4 = True
print(type(num4))
num5 = [10, 20, 30]  # 列表list
print(type(num5))
num5 = (10, 20, 30)  # 元组tuple
print(type(num5))
num6 = {10, 20, 30}  # 集合set
print(type(num6))
num7 = {'name': 'cyl', 'age': 18}  # 字典dict--键值对
print(type(num7))

# startwith 是否以某个字符串开头
# isalpha 是否都为字母构成
# isdigit 是否全为数字
# isalnum 数字或字母或字母数字组合
# isspace 是否全为空白

