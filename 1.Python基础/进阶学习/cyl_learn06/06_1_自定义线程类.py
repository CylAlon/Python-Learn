"""
    自定义类机场threading.Thread类
    重写run方法
    通过创建子类对象.start启动
"""
import threading
import time
# 自定义线程类
class MyThead(threading.Thread):
    """重写父类run方法"""
    def __init__(self,num):
        # 先调用父类的imit
        super().__init__()
        self.num=num
    def run(self):
        for i in range(5):
            print("正在执行子线程run方法...",i,self.name,self.num)
            time.sleep(0.5)

if __name__=="__main__":
    mythread=MyThead(10)
    mythread.start()
    print("xxxxx")

















