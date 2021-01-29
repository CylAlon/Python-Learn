

# 创建互斥锁


# 锁定资源



# 释放锁


import time
import threading
# 多个进程修改同一个变量时会出现资源竞争

g_num=0
lock1=threading.Lock()
def work1():
    # 声明g_num是全局变量
    global g_num

    for i in range(1000000):
        # 上锁
        lock1.acquire()
        g_num+=1
        lock1.release()
    print("woek1",g_num)


def woek2():
    global g_num
    for i in range(1000000):
        lock1.acquire()
        g_num += 1
        lock1.release()
    print("woek2",g_num)

if __name__=="__main__":

    # 创建一把互斥锁



    t1=threading.Thread(target=work1)
    t2=threading.Thread(target=woek2)
    t1.start()
    t2.start()
    while len(threading.enumerate())==1:
        print("fsas")
    print("结束",g_num)




