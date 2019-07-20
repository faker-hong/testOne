from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')   
parser.add_argument('-o', '--output')  #'-'为可选参数
parser.add_argument('--width', type=int, default=50)
parser.add_argument('--height', type=int, default=50)

#获取参数
args = parser.parse_args()

input_file = args.file
output_file = args.output
width = args.width
height = args.height

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    #计算灰度值
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    length = len(ascii_char)

    #映射到ascii_char的位置
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
        print("无写入文件的地址")
