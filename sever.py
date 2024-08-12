# coding = utf-8
from socket import *

s = socket(AF_INET, SOCK_DGRAM)  # AF_INET:ipv4, SOCK_DGRAM:UDP
s.bind(("127.0.0.1", 80))  # 绑定地址和端口
print('等待接收数据...')  # 接收数据
while True:
    recv_data = s.recvfrom(1024)  # 接收数据，1024表示接收的最大数据量
    recv_content = recv_data[0].decode('gbk')
    print(f"接收到的数据是：{recv_data[0].decode('gbk')},from {recv_data[1]}")
    s.sendto(recv_content.encode('gbk'), recv_data[1])  # 发送数据
    if recv_content == 'exit':
        print('客户端退出')
        break
s.close()