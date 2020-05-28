import requests
from bs4 import BeautifulSoup
import urllib.request
import lxml

class Pictures(object):
    def get_pictures(self, url, num):
        index = 1
        for i in range(1, num+1):
            new_url = url + "&pager_offset=" + str(i)
            response = requests.get(new_url)
            soup = BeautifulSoup(response.content, 'lxml')
            print(soup)
            imgs = soup.find_all('img')
            for j in imgs:
                urllib.request.urlretrieve(j.attrs['src'], './pictrues/%s.jpg' % index)
                print("第%s张已经下载好" % index)
                index += 1


if __name__ == '__main__':
    p = Pictures()
    p.get_pictures("https://www.dbmeinv.com/index.htm?cid=5",5)