def main():
    f = None
    try:
        f = open("d:/��дtest.txt", 'r')
        print(f.read())
        f = open("d:/��дtest.txt", 'w')
        txt = "��Һ�"
        poem = '��ǰ���¹⣬���ǵ���˪����ͷ�����£���ͷ˼���硣'
        f.write(txt)
        f = open("d:/��дtest.txt", 'a')
        f.write(poem)
        f = open("d:/��дtest.txt", 'r')
        print(f.read())
    except FileNotFoundError:
        print("�Ҳ����ļ�")
    except LookupError:
        print("ָ����δ֪�ı���")
    except UnicodeDecodeError:
        print("��ȡ�ļ�ʱ�������")
    finally:
        if f:
            f.close()
if __name__ == '__main__':
    main()