import json
import socket
from 线程实践.pool import ThreadPool
from 线程实践.task import AsyncTask

from 计算机网络实践.processor.net.parser import IPParser
from 计算机网络实践.processor.trans.parser import UDPParser, TCPParser


class ProcessTask(AsyncTask):
    def __init__(self, packet, *args, **kwargs):
        self.packet = packet
        super(ProcessTask, self).__init__(func=self.process, *args, **kwargs)

    def process(self):
        headers = {
            'network_header': None,
            'transport_header': None
        }
        ip_header = IPParser.parse(self.packet)
        headers['network_header'] = ip_header
        if ip_header['protocol'] == 17:
            udp_header = UDPParser.parser(self.packet)
            headers['transport_header'] = udp_header
        elif ip_header['protocol'] == 6:
            tcp_header = TCPParser.parser(self.packet)
            headers['transport_header'] = tcp_header
        return headers


class Server:
    def __init__(self):
        # 工作协议类型IPv4，套接字类型， 工作具体的协议 IP协议
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                  socket.IPPROTO_IP)
        self.ip = '192.168.31.79'
        self.port = 8888
        self.sock.bind((self.ip, self.port))

        # 设置为混杂模式，只要经过自己就接受。
        self.sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        self.pool = ThreadPool(10)
        self.pool.start()

    def loop_serve(self):
        while True:
            # 1.接受
            packet, addr = self.sock.recvfrom(65535)
            # 2.生成task
            task = ProcessTask(packet)
            # 3.提交
            self.pool.put(task)
            # 4.获取结果
            result = task.get_result()
            result = json.dumps(
                result,
                indent=4
            )
            print(result)


if __name__ == '__main__':
    server = Server()
    server.loop_serve()