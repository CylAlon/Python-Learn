"""
    单独使用可以结合网络助手
"""

# 建立连接
import socket

# 创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口 （该端口是客户端发送时的端口）
tcp_socket.bind(("", 49499))

# 监听 listen() 使套接字变为可以被动连接
# 这里的128是允许最大连接数 在windows下有效 在linux下无效
tcp_socket.listen(128)  # 此处程序阻塞不能发送数据


# 接收数据 recv(send)
while True:
    new_clcient_socket, new_clcient_ipcom = tcp_socket.accept()  # 开始接收客户端连接
    print(f"新客户端：{new_clcient_ipcom} 来了")

    while True:
        # 应答 accept() 自动解除阻塞 这里返回了一个新的套接字 即对象
        revc_date = new_clcient_socket.recv(1024)

        if revc_date:  # len(revc_date)!=0:
            print(f"来自客户端：{new_clcient_ipcom}的{revc_date.decode('gbk')}")
        # 关闭套接字
        else:
            print("断开连接")
            new_clcient_socket.close()
            break
tcp_socket.close()
