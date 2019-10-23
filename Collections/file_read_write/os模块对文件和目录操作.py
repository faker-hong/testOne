import os


fd = os.open("test.txt", os.O_CREAT | os.O_RDWR)
n = os.write(fd, '12sad3'.encode())  # 需要字节类型的，字符串需要先编码，返回长度
print(n)
l = os.lseek(fd, 0, os.SEEK_SET)   # 返回文件指针位置
print(l)
str = os.read(fd, 5)  # 读5个字节

#  os模块方法
os.access("文件名", os.R_OK)  # 文件是否有读权限
os.rename("旧名称", "新名称")
os.remove()
os.mkdir('')    # 创建文件


os.path.exists("sd")    # 路径是否存在
os.path.isdir()     # 是否是目录
os.path.isfile()    # 是否是文件