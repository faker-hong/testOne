import socket
import threading


def send_msg(udp_socket):
    # 定义变量接收用户与输入的接收方的ip
    ipaddress = input("请输入接收方的ip地址：\n")
    # 判断是否需要默认：
    if len(ipaddress) == 0:
        ipaddress = '192.168.31.79'
        print("默认接收方ip{}".format(ipaddress))
    # 定义变量接受用户与输出的接收方的端口号
    port = input("输入接收方端口号：\n")
    if len(port) == 0:
        port = '8080'
        print("默认端口号为{}".format(port))
    # 定义变量接收用户与输入的接收方内容
    content = input("要发送的内容：\n")
    udp_socket.sendto(content.encode(), (ipaddress, int(port)))


def recv_msg(udp_socket):
    while True:
        # 使用socket接收信息
        recv_data, ip_port = udp_socket.recvfrom(1024)
        # 解码输出
        recv_text = recv_data.decode()
        # 输出显示
        print("接受到{}的信息：{}".format(str(ip_port), recv_text))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(('', 8080))

    # 创建接受信息线程
    t1 = threading.Thread(target=recv_msg, args=(udp_socket, ))
    # 守护线程
    t1.setDaemon(True)
    t1.start()

    while True:
        # 打印菜单
        print("\n\n********************")
        print("**********  1.发送信息  **********")
        print("**********  2.退出系统  **********")
        # 接受用户输入的选项
        sel = int(input("请输入选项：\n"))
        # 判断用户的选择
        if sel == 1:
            send_msg(udp_socket)
        elif sel == 2:
            print("系统正在退出")
            print("系统退出完成")
            break
    udp_socket.close()


if __name__ == '__main__':
    main()