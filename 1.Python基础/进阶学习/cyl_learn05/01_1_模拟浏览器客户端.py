"""
    导入模块
    建立套接字
    拼接请求协议
    发送请求协议
    拼接服务器响应内容
    保存内容
    关闭连接

"""
# 导入模块
import socket
# 建立套接字
client_liulanqi=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 拼接请求协议
client_liulanqi.connect(("www.icoderi.com",80))
# 发送请求协议
# 请求行
request_line="GET / HTTP/1.1\r\n"
#  请求头
request_head="Host:www.icoderi.com\r\n"
# 请求空行
request_block="\r\n"
# 拼接服务器响应内容
request_data=request_line+request_head+request_block
# 发送协议f
client_liulanqi.send(request_data.encode())
# 保存内容
recv_dat=client_liulanqi.recv(4096)
recv_data=recv_dat.decode()
# print(recv_data)
num=recv_data.find("\r\n\r\n")+4
data=recv_data[num:]
# print(data)
fil=open("index.html","w")
fil.write(data)
# 关闭连接
client_liulanqi.close()










