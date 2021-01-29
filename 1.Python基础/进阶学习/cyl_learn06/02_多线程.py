
import time
import threading
"""
    使用threading.Trrea()
    指定子线程
"""
def saysorry():
    print("你好")
    time.sleep(0.5)


if __name__=='__main__':
    for i in range(5):
        # target=函数名，
        thread=threading.Thread(target=saysorry)  # 绑定函数名
        thread.start() # 开启线程
    print("sssss")








