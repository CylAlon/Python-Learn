"""
    导入模块
    创建套接字
    设置地址重用
    绑定端口
    设置监听
    接收客户连接
    判断协议是否为空
    拼接报文
    关闭操作

"""
# 导入模块
import socket


def request_hander(new_client_socket):
    """接收信息 "并做出响应"""
    # 判断协议是否为空
    request_data = new_client_socket.recv(1024)
    if not request_data:
        print("客户端下线")
        new_client_socket.close()
        return

    response_line = "HTTP/1.1 200 OK\r\n"
    response_head = "Server:Pyrhon20ws/2.1\r\n"
    response_block = "\r\n"

    response_body = "hello"

    dat = response_line + response_head + response_block + response_body
    new_dat = dat.encode()
    new_client_socket.send(new_dat)
    new_client_socket.close()

    # 拼接报文
    # 关闭操作


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置地址重用
    #                               当前套接字           地址重用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    tcp_server_socket.bind(("", 8080))  # 172.21.78.149
    # 设置监听
    tcp_server_socket.listen(128)
    while True:
        # 接收客户连接
        new_client_socket, new_client_ip = tcp_server_socket.accept()
        # 判断协议是否为空
        # 拼接报文
        request_hander(new_client_socket)
        # 关闭操作
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
