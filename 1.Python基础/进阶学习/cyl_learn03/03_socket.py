# 导入 socket模块
import socket
# 创建套接字使用 ipv4 udp方式
# 两个参数 协议参数 传输方式
#           AF_INET ipv4 AF_INET ipv4
#           SOCK_DGRAM UDP方式  SOCK_STREAM TCP方式
udp_socke= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 数据的传递

# 关闭套接字
udp_socke.close()








