"""
    配合网络调试助手使用
"""
# 引入包
import socket

# 创建对象 套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据
udp_socket.sendto("你好".encode('gbk'), ("192.168.125.1", 8080))
# 接收数据 （二进制）
udp_get_date = udp_socket.recvfrom(1024)  # 该方法会造成程序阻塞 即一直等待 当接收到数据 则接触阻塞

# 解码数据 得到字符串 decode
udp_get_typ = udp_get_date[0].decode(encoding="utf-8",errors="ignore")  # ignere 忽略出错 strict严格执行
'''
    这样解码会有问题 出现UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbd in position 0: invalid start byte
    计算机上发送的是     网络助手是发送GBK  
    需要加一个gbk
'''
# 显示
print(udp_get_typ)
# 关闭套接字
udp_socket.close()
