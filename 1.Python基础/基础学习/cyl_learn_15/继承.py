
# 继承
class A(object):
    def __init__(self):
        self.num=5
    def pri(self):
        print(f"----{self.num}")
class B(A):
    pass  # pass 是空语句，是为了保持程序结构的完整性。 pass 不做任何事情，一般用做占位语句。
b=B()
b.pri()

# 单继承 一个师傅类 一个徒弟类
class Master(object):  # 师傅类
    def __init__(self):
        self.gongfu='[配方]'
    def cake(self):
        print(f"运用{self.gongfu}配药")

class Student(Master):  # 徒弟类
    pass
st=Student()
st.cake()

# 多继承 一个徒弟 多个师傅

class Master2(object):  # 师傅1类
    def __init__(self):
        self.gongfu='[煎饼馃配方]'
    def cake(self):
        print(f"1 运用{self.gongfu}")
class Master3(object):  # 师傅2类
    def __init__(self):
        self.gongfu='[糖果馃配方]'
    def cake(self):
        print(f"2 运用{self.gongfu}")


class Student2(Master2,Master3):  # 徒弟类
    pass
st=Student2()  # 由于两个父类方法名一样 优先继承第一个
st.cake()

# 重写

class Student3(Master2,Master3):  # 徒弟类
    def __init__(self):
        self.gongfu='[麦芽糖馃配方]'
    def cake(self):
        print(f"3 运用{self.gongfu}")

st=Student3()  # 由于两个父类方法名一样 优先继承第一个
st.cake()

print(Student3.__mro__)  # 可以打印父类的层级关系


# 调用父类的同名方法
class Master4(object):  # 师傅1类
    def __init__(self):
        self.gongfu='[煎饼馃配方]'
    def cake(self):
        print(f"4 运用{self.gongfu}")
class Master5(object):  # 师傅2类
    def __init__(self):
        self.gongfu='[糖果馃配方]'
    def cake(self):
        print(f"5 运用{self.gongfu}")


class Student4(Master4,Master5):  # 徒弟类
    def make_master4(self):
        Master4.__init__(self)
        Master4.cake(self)
    def make_master5(self):
        Master5.__init__(self)
        Master5.cake(self)
    pass
st=Student4()  # 由于两个父类方法名一样 优先继承第一个
st.make_master4()
st.make_master5()

# 多层继承
class Master6(object):  # 师傅1类
    def __init__(self):
        self.gongfu='[煎饼馃配方]'
    def cake(self):
        print(f"6 运用{self.gongfu}")
class Master7(object):  # 师傅2类
    def __init__(self):
        self.gongfu='[糖果馃配方]'
    def cake(self):
        print(f"7 运用{self.gongfu}")


class Student6(Master4,Master5):  # 徒弟类
    def make_master6(self):
        Master6.__init__(self)
        Master6.cake(self)
    def make_master7(self):
        Master7.__init__(self)
        Master7.cake(self)
    pass

class Tusun(Student6):
    pass

st=Tusun()  # 由于两个父类方法名一样 优先继承第一个
st.cake()
st.make_master6()
st.make_master7()

# super()调用父类的方法
class Master8(object):  # 师傅1类
    def __init__(self):
        self.gongfu='[煎饼馃配方]'
    def cake(self):
        print(f"8 运用{self.gongfu}")

class Student8(Master8):  # 徒弟类

    def make_master8(self):
        super().__init__()
        super().cake()
    pass

class Tusun8(Student8):
    def oldmake_master8(self):
        super().__init__()
        super().cake()
    pass

st=Tusun8()  # 由于两个父类方法名一样 优先继承第一个

st.oldmake_master8()

# 私有权限 在变量 或者方法前面添加__两杠
class Master10(object):  # 师傅1类
    def __init__(self):
        self.gongfu='[煎饼馃配方]'
        self.__priv=500
    def cake(self):
        print(f"10 运用{self.gongfu}")
    def __qq(self):
        print(f'{self.priv}')
ms=Master10()
ms.cake()
# 获取和修改是由值








