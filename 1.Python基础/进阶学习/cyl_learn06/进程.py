# -*- coding: utf-8 -*-
# @Author  : Cyl
# @Time    : 2021/1/3 3:01
# @File    : 进程.py
# @Software: PyCharm
"""
FileSpec:

"""

import multiprocessing
import time

def task1():
    for i in range(10):
        print(1)
        time.sleep(0.5)

def task2():
    for i in range(10):
        print(2)
        time.sleep(0.3)




if __name__ == "__main__":

    p1 = multiprocessing.Process(target = task1())
    p2 = multiprocessing.Process(target = task2())
    p1.start()
    p2.start()