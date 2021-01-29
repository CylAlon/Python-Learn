
"""
    导入模块
    创建套接字
    绑定端口
    设置监听 设置套接字位被动
    接收客户端文件名
    接收客户端文件名
    接收文件名读取文件内容
    把数据内容发送给客户端
    关闭套接字

"""
# 导入模块
import socket
# 创建套接字
tcp_socler=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口
tcp_socler.bind(("",8080))
# 设置监听
tcp_socler.listen(128)
# 设置套接字位被动
new_client_socket,new_client_ip=tcp_socler.accept()
print("欢迎新客户端")
# 接收客户端文件名
fill_name=new_client_socket.recv(1024).decode('gbk')
print(fill_name)
# 接收文件名读取文件内容
try:
    fil=open("de/"+fill_name,'rb')
    while True:
        fil_dat=fil.read(1024)
        if fil_dat:
            # 把数据内容发送给客户端
            new_client_socket.send(fil_dat)
        else:
            new_client_socket.close()
            fil.close()
            break
    # 关闭套接字
except Exception:
    print("下载文件出错")
    tcp_socler.close()












