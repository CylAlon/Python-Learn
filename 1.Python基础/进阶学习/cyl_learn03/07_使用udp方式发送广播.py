import socket

# 创建套接字
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 设置广播权限

'''
    udp_socket.sendto("哈哈 打不过我把".encode('gbk'),("255.255.255.255",8080))
    这样会出错 OSError: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。
需要开启相关权限 udp_sockt(套接字，属性，属性值)
'''
udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)

# 发送数据 xxx.xxx.xxx.255
udp_socket.sendto("哈哈 打不过我把".encode('gbk'),("255.255.255.255",8080))



# 关闭
udp_socket.close()































