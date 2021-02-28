# -*- coding: UTF-8 -*-
import socket, os, struct
import time
# from picamera import  PiCamera
import cv2
"""set ip address"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.123.174', 8000))

"""set camera"""
camera = cv2.VideoCapture(0)
camera.resolution = (1920,1080)
camera.framerate = 60

"""get opencv-classifier"""
face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.3.0/data/lbpcascades/lbpcascade_frontalface.xml' )

while True:
    camera.capture('/home/pi/class/0.jpg')
    filepath = '/home/pi/class/0.jpg'
    image = cv2.imread(filepath)
    gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
    faces = face_cascade.detectMultiScale( gray )
    if os.path.isfile(filepath) and len(faces):
        fileinfo_size = struct.calcsize('128sl')  # 定义打包规则
        # 定义文件头信息，包含文件名和文件大小
        fhead = struct.pack('128sl', os.path.basename(filepath), os.stat(filepath).st_size)
        s.send(fhead)
        print('client filepath: ', os.path.basename(filepath), os.stat(filepath).st_size)

        # with open(filepath,'rb') as fo: 这样发送文件有问题，发送完成后还会发一些东西过去
        fo = open(filepath, 'rb')
        while True:
            filedata = fo.read(1024)
            if not filedata:
                break
            s.send(filedata)
        #time.sleep(0.5)
        fo.close()
        print('send over...')
    #time.sleep(0.5)
        # s.close()