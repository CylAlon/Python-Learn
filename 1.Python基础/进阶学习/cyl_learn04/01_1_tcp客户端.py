"""
    单独使用可以结合网络助手
"""
# 导入模块
import socket

# 创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接 socket.connect(address) 主动初始化tcp服务器连接
tcp_socket.connect(("192.168.2.13", 8080))

# 发送数据 socket.send(要发送的数据)
tcp_socket.send("约吗".encode('gbk'))

# 接收消息 socket.recv(缓冲区大小)
tcp_dat = tcp_socket.recv(1024)
print(tcp_dat.decode('gbk'))
# 关闭套接字
tcp_socket.close()
