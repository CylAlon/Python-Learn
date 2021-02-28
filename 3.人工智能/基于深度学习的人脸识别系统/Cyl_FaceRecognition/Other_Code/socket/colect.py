#!/usr/bin/python
#-*-coding:utf-8 -*-
import socket
import cv2
import numpy as np

host_port = ('192.168.43.227',8080)
capture_frame_width = 640
capture_frame_height = 480
class ClientSocket(object):
    def __init__(self):
        # socket.AF_INET用于服务器与服务器之间的网络通信
        # socket.SOCK_STREAM代表基于TCP的流式socket通信
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client_socket.connect(host_port) #链接服务器
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, capture_frame_width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, capture_frame_height)
        self.encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]  #设置编码参数
    def run(self):
        #从摄像头获取图片
        ret , frame = self.capture.read()
        while ret:
            # 首先对图片进行编码，因为socket不支持直接发送图片
            result, imgencode = cv2.imencode('.jpg', frame)
            data = np.array(imgencode)
            stringData = data.tostring()
            # 首先发送图片编码后的长度
            self.client_socket.send(str(len(stringData)).ljust(16))
            # 然后一个字节一个字节发送编码的内容
            # 如果是python对python那么可以一次性发送，如果发给c++的server则必须分开发因为编码里面有字符串结束标志位，c++会截断
            for i in range (0,len(stringData)):
                self.client_socket.send(stringData[i])
            ret, frame = self.capture.read()
            #cv2.imshow('CLIENT',frame)
            # if cv2.waitKey(10) == 27:
            #     break
            # 接收server发送的返回信息
            data_r = self.client_socket.recv(50)
            print (data_r)
        self.client_socket.close()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    s = ClientSocket()
    s.run()
