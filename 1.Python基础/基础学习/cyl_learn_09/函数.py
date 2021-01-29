

# 函数先定义后使用
def da_yin(valie):
    """
    打印函数
    :param valie:
    :return: 字段
    """
    # 上面 方法名下第一行是函数说明
    v = valie
    print(v)
    return {"d":v}

def ff(v1,v2):
    print(v1)
    print(v2)



da_yin(10)
da_yin(valie='10')
print(da_yin(100))

ff(10,10)
ff(v1=100,v2=None)


help(len)  # 解释说明函数信息
help(da_yin)

def hans():  # 函数嵌套
    ff(100,200)

hans()








