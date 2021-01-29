import time
import threading


def work1():
    for i in range(10):
        print("正在执行work")
        time.sleep(0.5)


if __name__ == "__main__":
    thread_worl = threading.Thread(target=work1)
    # 子线程守护主线程 主线程死亡子线程也死亡
    thread_worl.setDaemon(True)
    thread_worl.start()
    time.sleep(2)
    print("Game over")
    exit()
