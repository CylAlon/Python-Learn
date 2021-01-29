
"""
    配合网络调试助手使用
"""
# 导入包
import socket

# 创建套接字
udp_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据 socket.sendto(要发送数据的二进制格式，对方的Ip和端口号)
# 字符串.encode() 把字符串转二进制
# ip和端口号 使用元组
udp_send.sendto("你好".encode(), ("192.168.125.1", 8080))
# 关闭套接字
udp_send.close()
