class Xiyi():
    def wash(self):  # self 是调用该类的对象
        print('sffsa')
        print(self)

    def pri(self):
        print(f'+++{self.wigth}')
        print(f'+++{self.height}')


he = Xiyi()
# print(he)
# he.wash()  # he的地址和改方法的self是同一个东西

# 添加和获取对象属性

he.wigth = 400
he.height = 600  # 在类外边添加变量
print(f'{he.height} {he.wigth}')
he.pri()
# class Hebx():


"""
    魔法方法
    __xx__()的函数叫魔法方法 值具有特殊功能的函数  
"""


# 1 __init__() 初始化对象
class Myqs():
    def __init__(self):
        self.width = 500
        self.height = 600

    def pri(self):
        print(f"--{self.width} {self.height}")


cy = Myqs()
cy.pri()


# 带参数的__init__() 魔法方法
class Myqs2():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def pri(self):
        print(f"****{self.width} {self.height}")


cy = Myqs2(700, 800)
cy.pri()


# 2 __str__()魔法方法  当使用print输出对象的时候默认打印内存的对象地址
#  如果定义了改魔法方法则打印这个方法中retern的数据
class Myqs3():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "寝室类"

    def pri(self):
        print(f"Myqs3****{self.width} {self.height}")


cy = Myqs3(700, 800)
print(cy)


# 3 __del__() 当删除对象时，python解释器也会默认调用__del__()方法
class Myqs4():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return ''+str(self.width)+' '+str(self.height)

    def __del__(self):  # 不写也会自动调用
        print("删除成功")

    def pri(self):
        print(f"Myqs3****{self.width} {self.height}")


print('wwwwwww')
cy = Myqs4(700, 800)
print(cy)

del cy
# sorted()