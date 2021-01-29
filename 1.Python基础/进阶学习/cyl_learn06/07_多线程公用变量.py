
import time
import threading
# 多个进程修改同一个变量时会出现资源竞争

g_num=0

def work1():
    # 声明g_num是全局变量
    global g_num

    for i in range(1000000):
        g_num+=1
    print(g_num)


def woek2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print(g_num)

if __name__=="__main__":
    t1=threading.Thread(target=work1)
    t2=threading.Thread(target=woek2)
    t1.start()
    t1.join() # 让某一个线程执行完
    t2.start()
    while len(threading.enumerate())!=1:
        print("fsas")
    print("结束",g_num)



