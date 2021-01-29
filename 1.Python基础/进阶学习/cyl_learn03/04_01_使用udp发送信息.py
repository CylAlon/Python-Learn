

import socket


udp_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_send.sendto("".encode(), ("192.168.168.1", 8080))

udp_send.close()
