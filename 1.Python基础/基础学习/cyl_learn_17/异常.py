"""
    try:
        可能出现错误的代码
    except:
        如果出现异常执行的代码
"""

try:
    f=open('txt.txt','r')
except:
    print("出现异常")


# 捕获指定异常

try:
    f=print(num)
except NameError:
    print("出现异常")
# 捕获多个异常

try:
    print(1/0)
except (NameError,ZeroDivisionError):
    print("有错误")

# 捕获异常描述信息
try:
    print(1/0)
except (NameError,ZeroDivisionError) as result:
    print(result)

# 捕获所有异常
try:
    print(1/0)
except Exception as result:
    print(result)


# 异常中的else
try:
    print(1/1)
except Exception as result:
    print(result)
else:
    print("没有异常 正常执行")


# 异常的finilly 无论是否异常都执行 常在关闭文件中使用



# 异常传递




