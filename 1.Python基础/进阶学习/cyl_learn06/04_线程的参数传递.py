import time
import threading
def sing(a,b,c):
    print(f'{a}{b}{c}')
    for i in range(5):

        print("正在唱歌")
        time.sleep(0.5)
def dance(a,b,c):
    print(f'{a}{b}{c}')
    for i in range(5):

        print("正在跳舞........")
        time.sleep(0.5)
def swing(a,b,c):
    print(f'{a}{b}{c}')
    for i in range(5):
        print("正在洗澡........")
        time.sleep(0.5)
if __name__=="__main__":

    # 获取线程名称
    thre1=threading.current_thread()
    print(thre1)

    # 线程的参数传递三种方法
    # 方法一 使用元组传递

    thred1=threading.Thread(target=sing,args=(100,1000,10000))
    thred2=threading.Thread(target=dance,kwargs={'a':41,'b':41,'c':41})
    thred3 = threading.Thread(target=swing, kwargs={'a': 454, 'b': 453},args=(100))
    thred1.start()
    thred2.start()
    # 获取线程数量
    lis=threading.enumerate()
    print(f"当前线程数量{lis}")














