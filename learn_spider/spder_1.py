import sys
import requests
from bs4 import BeautifulSoup
import lxml

resp = requests.get("https://www.baidu.com")     # 请求百度首页
# print(resp)
# print(resp.content)

bsobj = BeautifulSoup(resp.content, 'lxml')     # 将网页源码构造成BS对象，使用BeautifulSoup+lxml解析请求到的网页源码。
a_list = bsobj.find_all('a')     # 获取网页中的所有a标签对象
print(a_list)
text = ''
for a in a_list:
    href = a.get('href')
    text += href+'\n'
    print(a.get('href'))    # 打印a标签对象的href属性，即这个对象指向的链接地址

with open('url.txt','w') as f:
    f.write(text)