import sys
import time
import requests
from bs4 import BeautifulSoup
import json
import re

index_url = 'https://www.biquge5200.cc/14_14621/'


def get_text_url(url):
    response = requests.get(url)
    result = response.text
    text_url = re.findall(r'<dd><a href="(.*?)">.*?</a></dd>', result)
    return text_url


def get_title_text(url):
    response = requests.get(url)
    result = response.text
    title = re.findall(r'<title>(.*?)</title>', result)
    text = re.findall(r'<div id="content">([\s\S]*?)</div>', result)
    sentence_list = []
    if title:
        title = title[0]
        if '_斗神狂飙_笔趣阁' in title:
            title = title.replace('_斗神狂飙_笔趣阁', '')
    if text:
        text = text[0]
        text = text.split("</p><p>")
    for sentence in text:
        if '..访问下载txt小说' in sentence:
            sentence.replace('..访问下载txt小说', '')
        if '阅读本书最新章节请到' in sentence:
            continue
        sentence_list.append(sentence)
    return title, sentence_list


if __name__ == '__main__':
    for url in get_text_url(index_url):
        time.sleep(1)
        data = get_title_text(url)
        with open('斗神狂飙.txt', 'a') as f:
            f.write(data[0])
            f.write('\n')
            f.write('\n')
            for sentence in data[1]:
                f.write(sentence)
                f.write('\n')
        print(data[0]+'已完成')
    print('下载完毕')