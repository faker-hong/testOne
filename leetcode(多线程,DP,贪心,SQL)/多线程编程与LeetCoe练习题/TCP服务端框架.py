'''
1.导入模块
2.创建套接字
3.设置地址可以重用
4.绑定端口
5.设置监听，套接字由主动设置为被动
6.接受客户端连接
7.接受客户端发送的信息
8.解码数据并进行输出
9.关闭和当前客户端的连接
'''


import socket
import threading


def recv_msg(new_client_socket, ip_port):
    while True:
        # 接受客户端发送的信息
        recv_data = new_clinet_socket.recv(1024)
        if recv_data:
            # 解码数据并进行输出
            recv_text = recv_data.decode("GBK")
            print("收到{}的信息{}".format(str(ip_port), recv_text))
        else:
            break
    # 关闭和当前客户端的连接
    new_clinet_socket.close()

# 创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置地址可以重用
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定端口
tcp_socket.bind(('', 8080))
# 设置监听，套接字由主动设置为被动
tcp_socket.listen(128)  # 最多允许128个连接
while True:
    # 接受客户端连接
    new_clinet_socket, ip_port = tcp_socket.accept()
    print("欢迎新用户上线：", new_clinet_socket)
    t1 = threading.Thread(target=recv_msg, args=(new_clinet_socket, ip_port))
    t1.setDaemon(True)
    t1.start()
