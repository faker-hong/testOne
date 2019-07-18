def main():
    f = None
    try:
        f = open("d:/读写test.txt", 'r')
        print(f.read())
        f = open("d:/读写test.txt", 'w')
        txt = "大家好"
        poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
        f.write(txt)
        f = open("d:/读写test.txt", 'a')
        f.write(poem)
        f = open("d:/读写test.txt", 'r')
        print(f.read())
    except FileNotFoundError:
        print("找不到文件")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")
    finally:
        if f:
            f.close()
if __name__ == '__main__':
    main()