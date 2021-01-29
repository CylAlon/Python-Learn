
# 需要使用类对象（如访问私有类属性时）类方法和类属性一起使用

class Dog():
    __tooth=10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

w=Dog()
print(w.get_tooth())








