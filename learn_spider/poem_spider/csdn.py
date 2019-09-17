from bs4 import BeautifulSoup
import requests
import re


class Poem(object):
    def __init__(self, url):
        self.url = url
        self.hot_author = {}    # 推荐作者
        self.es_author = {}     # 作者合称
        self.title_author = {}  # 作者称号
        self.sort_poem = {}     # 诗类别
        self.history = {}       # 史书典籍

    # 存放所有类别的链接
    def get_all_author(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        # 作者称号的链接
        title_authors = soup.find_all(class_="index-li")[2].find_all('a')
        for i in title_authors:
            self.title_author[i.text] = i['href']

        # 推荐作者的链接
        hot_authors = soup.find_all(class_="index-li")[0].find_all('a')
        for i in hot_authors:
            self.hot_author[i.text] = i['href']

        # 作者合称的链接
        es_authors = soup.find_all(class_="index-li")[1].find_all('a')
        for i in es_authors:
            self.es_author[i.text] = i['href']

        # 诗类别的链接
        sort_poems = soup.find_all(class_="index-li")[3].find_all('a')
        for i in sort_poems:
            self.sort_poem[i.text] = i['href']

        # 史书典籍的链接
        historys = soup.find_all(class_="index-li")[4].find_all('a')
        for i in historys:
            self.history[i.text] = i['href']

    def get_author_poem_url(self, author):
        url1 = self.title_author[author]
        url2 = self.url
        new_url = url2+url1
        response = requests.get(new_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # 计算出总共有多少页
        patter = re.compile(r'\((.*?)首\)')
        num = patter.findall(soup.find('h1').text)
        pages = int(num[0]) // 40 + 1
        # 基础url，方便下面的url拼接
        basic_url = new_url[:-5]

        for j in range(2, pages+1):
            poems = soup.select("h3 > a")
            with open('./' + author + '', 'a', encoding='utf-8') as f:
                for i in poems:
                    newUrl = url2 + i['href']
                    poem = self.save_poem(newUrl, author)
                    f.write('\n\n')
            # 诗句所在的url
            new_url = basic_url + '_' + str(j) + '.html'
            print(new_url)
            response = requests.get(new_url)
            soup = BeautifulSoup(response.content, 'html.parser')

    def save_poem(self, url, author):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 诗名
        title = soup.find('h1')
        # 诗句内容
        content = soup.find(class_='shici-content')
        # 根据诗句的。？！进行分割
        contents = re.split("[。？！]", content.text)

        with open('./'+author+'', 'a', encoding='utf-8') as f:
            f.write(title.text)
            f.write('\n\n')
            for con in contents:
                f.write(con.strip())
                f.write('\n')
            f.write('\n')

    def save_poem_index(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        titles = soup.find_all('h3')
        authors = soup.find_all(class_='index-li')

        with open('./诗词名句首页', 'w', encoding='utf-8') as f:
            for i in range(len(titles)-1):
                f.write('\n\n')
                f.write(titles[i].text)
                f.write('\n\n')
                abc = authors[i].find_all('a')
                i = 0
                for j in range(len(abc)):
                    i += 1
                    f.write(abc[j].text)
                    f.write(' ')
                    # 每隔10个换行
                    if i % 10 == 0:
                        f.write('\n')


if __name__ == '__main__':
    url = "http://www.shicimingju.com"
    p = Poem(url)
    p.save_poem_index()
    p.get_all_author()
    p.get_author_poem_url('王维（诗佛）')
