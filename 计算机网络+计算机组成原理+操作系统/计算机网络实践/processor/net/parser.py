import socket
import struct


class IPParser:
    IP_HEADER_LENGTH = 20

    @classmethod
    def parse_ip_header(cls, ip_header):
        """
        IP 报文格式：
            1. 4位IP版本， 4位IP头长度， 8位服务类型， 16为总长度
            2. 16位标识符，3位标记位，3位片偏移
            3. 8位TTL，8位协议，16位IP头校验和
            4. 32位源IP地址
            5. 32位目的IP地址
        """
        line1 = struct.unpack('>BBH', ip_header[:4])
        # 右移4位获得IP版本 11110000 => 1111
        ip_version = line1[0] >> 4
        # 15的比特位是00001111，进行与运算后，可以屏蔽前四位，获得后四位
        iph_length = line1[0] & 15 * 4
        packet_length = line1[2]

        line3 = struct.unpack('>BBH', ip_header[8:12])
        TTL = line3[0]
        protocol = line3[1]
        iph_checksum = line3[2]

        line4 = struct.unpack('>4s', ip_header[12:16])
        src_ip = socket.inet_ntoa(line4[0])

        line5 = struct.unpack('>4s', ip_header[16:20])
        dst_ip = socket.inet_ntoa(line5[0])

        return {
            'ip_version': ip_version,
            'iph_length': iph_length,
            'packet_length': packet_length,
            'TTL': TTL,
            'protocol': protocol,
            'iph_checksum': iph_checksum,
            'src_ip': src_ip,
            'dst_ip': dst_ip
        }

    @classmethod
    def parse(cls, packet):
        ip_header = packet[:20]
        return cls.parse_ip_header(ip_header)
