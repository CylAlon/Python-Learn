"""
    发送信息
    接收信息
    退出程序

    框架
        发送信息 send_msg()
        接收消息 recv_msg()
        程序运行是启动聊天器

    实现步骤
        定义变量接受收ip 端口号 内容
        发送信息

        接收数据
        输出显示

        主入口main()
            创建套接字
            绑定端口
            打印菜单
            接收用户的选项
            判断用户的选项 并且执行
            关闭套接字
"""
import socket
def send_msg(udp_socket):
    """发送信息"""
    input_ip=input("请输入ip")
    input_com=input("请输入端口号")
    input_typ=input("请输入内容")
    udp_socket.sendto(input_typ.encode('gbk'),(input_ip,int(input_com)))
    pass


def recv_msg(udp_socket):
    """接收信息"""
    udp_get_date = udp_socket.recvfrom(1024)
    udp_get_typ = udp_get_date[0].decode("gbk")
    print(udp_get_typ)
    pass

def main():
    while True:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(("", 8085)) # 8085是绑定的是对方接收端 即对方发送端口
        print("\n****************************")
        print("****   1、发送信息    ******")
        print("****   2、接收信息    ******")
        print("****   3、退出系统    ******")
        print("****************************")
        num = int(input("请输入操作数字："))
        if num == 1:
            send_msg(udp_socket)
        elif num == 2:

            recv_msg(udp_socket)
        elif num == 3:
            print("退出系统")
            break
        udp_socket.close()

if __name__=='__main__':
    main()




