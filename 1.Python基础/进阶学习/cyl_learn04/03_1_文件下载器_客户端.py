"""
# 创建套接字

# 建立连接

# 接收用户输入的文件名

# 发送文件名到服务器

# 创建文件准备保存

# 接收服务器发送的数据 保存到本地

# 关闭套接字
"""

import socket

# 创建套接字
tcp_soclet=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
tcp_soclet.connect(("192.168.125.1",8080))

# 接收用户输入的文件名
fail_name=input("请输入需要下早的文件名：\n")
# 发送文件名到服务器
tcp_soclet.send(fail_name.encode('gbk'))
# 创建文件准备保存
fill=open("re/"+fail_name,"wb")
while True:
    # 接收服务器发送的数据 保存到本地
    fil=tcp_soclet.recv(1024)
    if fil:
        fill.write(fil)
    else:
        fill.close()
        break

# 关闭套接字
tcp_soclet.close()






















