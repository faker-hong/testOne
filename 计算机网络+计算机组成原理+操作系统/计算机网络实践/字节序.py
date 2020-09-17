import struct


bin_str = b'ABCD1234'
print(bin_str)
result = struct.unpack('>BBBBBBBB', bin_str)    # >表示大段字节序，一个B表示一个字节
print(result)
result = struct.unpack('>HHHH', bin_str)    # 一个H表示2个字节
print(result)
result = struct.unpack('>LL', bin_str)      # 一个L表示4个字节
print(result)
result = struct.unpack('>8s', bin_str)      # s表示字符,这里8个字符
print(result)
result = struct.unpack('>BBHL', bin_str)    # 混合使用
print(result)