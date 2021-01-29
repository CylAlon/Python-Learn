
__all__=['add']  # 加上这句 外部使用from make_mode import * 也智能导入add方法

def add(a,b):
    print(a+b)

mul=lambda a,b:print(a*b)


def fdfd(a,b):
    x = a+b
    return x


# 测试信息
if __name__=='__main__':  # 在当前文件是才执行
    add(10,2)
    mul(10,3)