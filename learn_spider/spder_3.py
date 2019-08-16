from urllib import request

import requests
from bs4 import BeautifulSoup
import lxml


class ReadNovel(object):
    def __init__(self, url):
        self.url = url

    def get_urls(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'lxml')
        urls = soup.select(".book-mulu > ul > li > a")
        return urls

    def get_title_text(self, url):
        new_url = "http://www.shicimingju.com"+url.attrs["href"]
        response = requests.get(new_url)
        soup = BeautifulSoup(response.content, 'lxml')
        title = soup.find('title').text
        text = soup.find_all('p')
        title += '\n'
        for i in text:
            title += i.text
            title += '\n'
        with open('儒林外史.txt', 'a', encoding='utf-8') as f:
            f.write(title)
            f.write('\n')


if __name__ == '__main__':
    url = "http://www.shicimingju.com/book/rulinwaishi.html"
    read_novel = ReadNovel(url)
    urls = read_novel.get_urls()
    print(urls)
    for url in urls:
        read_novel.get_title_text(url)