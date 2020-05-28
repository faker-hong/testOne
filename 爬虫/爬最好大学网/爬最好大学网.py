import requests
from bs4 import BeautifulSoup
import bs4

# 通过修改2019的值，就可以获取到不同年份的大学排名
# url = requests.get("http://www.zuihaodaxue.com/ARWU2019.html")

'''
可以通过查看url.status_code判断是否访问成功，值为200则说明访问成功。

还需要检查一点是网页的编码url.encoding是否为utf-8，如果不是需要进行修改，保证获取到的数据不会发生乱码
'''

# url.encoding = url.apparent_encoding


# soup = BeautifulSoup(url.content, 'lxml')

# 获得以url为键，年份为值得字典
def get_all_year_url():
    urls = {}

    for year in range(2003, 2020):
        url = "http://www.zuihaodaxue.com/ARWU{}.html".format(year)
        urls[url] = year

    return urls


def get_all_rating_college():
    urls = get_all_year_url()
    for url, year in urls.items():
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.content, 'lxml')
        infos = []

        for tr in soup.find('tbody').children:
            # 判断tr是否为bsr.element.Tag标签类型的元素
            if isinstance(tr, bs4.element.Tag):
                tds = tr.find_all('td')
                rating = tds[0].string
                name = tds[1].string
                score = tds[4].string
                if score is None:
                    info = "{} {} 暂无评分".format(rating, name)
                else:
                    info = "{} {} {}".format(rating, name, score)
                infos.append(info)

        write_to_txt(year, infos)


def write_to_txt(year, infos):
    with open('rating_collage.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write('\n')
        f.write(str(year))
        f.write('\n')
        f.write('\n')
        for info in infos:
            f.write(info)
            f.write('\n')


if __name__ == '__main__':
    get_all_rating_college()
