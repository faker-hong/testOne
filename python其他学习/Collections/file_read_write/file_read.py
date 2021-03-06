import os


f = open("文件地址", '读写的模式')  # 读写的模式可以为r只读，w写，r+读写，a追加等
f.tell()  #  告诉文件目前指针位置
f.seek(1, os.SEEK_SET)
# 第一个参数为偏移量，偏移量可为负数
# 第二个参数为文件指针位置，
# SEEK.CUR为当前指针位置
# SEEK.END为文件末尾
# SEEK.SET为文件开始

f = open("sss", 'w')
f.close()
"""
    文件在写入，会先写入缓存，缓存满了之后再写入磁盘，
    所以调用flush或close方法后，才会把剩下的内容写入磁盘，不然查看文件会少在缓存中的内容
"""
iter_list = iter(f)  # 使用迭代器来读取文件，避免文件内容太大造成内存溢出