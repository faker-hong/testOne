from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#�����������������
parser = argparse.ArgumentParser()

parser.add_argument('file')   
parser.add_argument('-o', '--output')  #'-'Ϊ��ѡ����
parser.add_argument('--width', type=int, default=50)
parser.add_argument('--height', type=int, default=50)

#��ȡ����
args = parser.parse_args()

input_file = args.file
output_file = args.output
width = args.width
height = args.height

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    #����Ҷ�ֵ
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    length = len(ascii_char)

    #ӳ�䵽ascii_char��λ��
    position = int(gray / (256 + 1.0) * length)

    return ascii_char[position]

def write_file(ouput_file, content):
    with open(output_file, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    im = Image.open(input_file)
    im = im.resize((width, height), Image.NEAREST)
    txt = ''

    for i in range(width):
        for j in range(height):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)
    if output_file:
        write_file(output_file, txt)
    else:
        print("��д���ļ��ĵ�ַ")
