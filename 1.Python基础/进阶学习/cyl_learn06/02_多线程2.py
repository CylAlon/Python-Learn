import time
import threading
def sing():
    for i in range(5):
        print("正在唱歌")
        time.sleep(0.5)
def dance():
    for i in range(5):
        print("正在跳舞........")
        time.sleep(0.5)

if __name__=="__main__":
    thred1=threading.Thread(target=sing)
    thred2=threading.Thread(target=dance)
    thred1.start()
    thred2.start()















