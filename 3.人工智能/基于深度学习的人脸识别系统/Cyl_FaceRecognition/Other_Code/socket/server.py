#!/usr/bin/python
# -*-coding:utf-8 -*-
import socket
import cv2
import numpy

address = ('', 8080)  # 设置地址与端口，如果是接收任意ip对本服务器的连接，地址栏可空，但端口必须设置


class ServerSocket(object):
    def __init__(self):
        # socket.AF_INET用于服务器与服务器之间的网络通信
        # socket.SOCK_STREAM代表基于TCP的流式socket通信
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(address)  # 将Socket（套接字）绑定到地址
        self.server_socket.listen(True)  # 开始监听TCP传入连接
        print('Waiting for images...')

    # 接受图片大小的信息
    def recv_size(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    # 接收图片
    def recv_all(self, sock, count):
        buf = ''
        while count:
            # 这里每次只接收一个字节的原因是增强python与C++的兼容性
            # python可以发送任意的字符串，包括乱码，但C++发送的字符中不能包含'\0'，也就是字符串结束标志位
            newbuf = sock.recv(1)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def run(self):

        # 接受TCP链接并返回（conn, addr），其中conn是新的套接字对象，可以用来接收和发送数据，addr是链接客户端的地址。
        conn, addr = self.server_socket.accept()
        while True:
            length = self.recv_size(conn, 16)  # 首先接收来自客户端发送的大小信息
            if isinstance(length, str):  # 若成功接收到大小信息，进一步再接收整张图片
                stringData = self.recv_all(conn, int(length))
                data = numpy.fromstring(stringData, dtype='uint8')
                decimg = cv2.imdecode(data, 1)  # 解码处理，返回mat图片
                cv2.imshow('SERVER', decimg)
                if cv2.waitKey(10) == 27:
                    break
                print('Image recieved successfully!')
                conn.send("Server has recieved messages!")
            if cv2.waitKey(10) == 27:
                break

        self.server_socket.close()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    s = ServerSocket()
    s.run()
