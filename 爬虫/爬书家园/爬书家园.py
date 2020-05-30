import requests
import os
from bs4 import BeautifulSoup
import re

url = "https://www.shujy.com/paihangbang/"


# 得到每一个模块小说排行榜的大title
def get_titles():
    r = requests.get("https://www.shujy.com/paihangbang/")
    soup = BeautifulSoup(r.content, 'lxml')
    titles = []
    for title in soup.find_all('h3'):
        titles.append(title.string)
    return titles


# 获取玄幻小说排行榜小说名和urls
def get_magic_novel(url):
    r = requests.get(url)
    new_url = "https://www.shujy.com"
    soup = BeautifulSoup(r.content, 'lxml')
    b1 = soup.select_one("div[class='box b1']")
    b1 = b1.select_one('ul')
    b1_a = b1.find_all("a")[3:-1]
    b1_p = b1.find_all('li')[1:-1]
    names = []
    urls = []
    for a, p in zip(b1_a, b1_p):
        urls.append(new_url + a.get('href'))
        names.append(p.text)

    return names, urls


# 获取详细章节 https://www.shujy.com/5200/15704/
def get_chapter(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    chapters = soup.select("dl>dd>a")
    chapter_names = []
    chapter_urls = []
    for item in chapters:
        chapter_names.append(item.text)
        chapter_urls.append(url+item.get('href'))

    return chapter_names, chapter_urls


# 获取篇章详细内容
def get_chapter_detail(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    contents = soup.select('#content')
    detali = []
    for content in contents:
        detali.append(str(content))

    return detali


if __name__ == '__main__':
    names, urls = get_magic_novel(url)
    print(1)
    print(names, urls)
    print(2)
    for url in urls:
        print(3)
        print(url)
        chapter_names, chapter_urls = get_chapter(url)
        print(chapter_names, chapter_urls)
        print(4)
        for index, chapter_url in enumerate(chapter_urls):
            print(5)
            contents = get_chapter_detail(chapter_url)
            with open('magic_noval.txt', 'a', encoding='utf-8') as f:
                f.write(str(chapter_names[index]))
                f.write('\n\n')
                for content in contents:
                    f.write(content)
                    f.write('\n')
