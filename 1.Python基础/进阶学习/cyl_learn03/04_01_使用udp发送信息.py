
"""
    ��������������ʹ��
"""
# �����
import socket

# �����׽���
udp_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# �������� socket.sendto(Ҫ�������ݵĶ����Ƹ�ʽ���Է���Ip�Ͷ˿ں�)
# �ַ���.encode() ���ַ���ת������
# ip�Ͷ˿ں� ʹ��Ԫ��
udp_send.sendto("���".encode(), ("192.168.125.1", 8080))
# �ر��׽���
udp_send.close()
