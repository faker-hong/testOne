import requests
from bs4 import BeautifulSoup


class QiuShiSpider(object):
    def __init__(self):
        self.url = "https://www.qiumeimei.com/text/page/{}"

    def get_url_list(self):
        url_list = [self.url.format(i) for i in range(1, 10)]
        return url_list

    def get_html_list(self, url_list):
        html_list = []
        for url in url_list:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            html_list.append(soup)
        return html_list

    def get_topics_url_list(self, html_list):
        topic_url_list = []
        for html in html_list:
            topics = html.find_all(class_='top clearfix')
            for topic in topics:
                topic_url = topic.a['href']
                topic_url_list.append(topic_url)
        return topic_url_list

    def get_topics_and_save(self, topics_url_list):
        for topic_url in topics_url_list[1:]:
            response = requests.get(topic_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.select(".main > h1")[0].text
            content = soup.select(".upload-txt > p")
            if not content:
                content = soup.select(".main > p")[0].text
            else:
                content = soup.select(".upload-txt > p")[0].text
            self.save(title, content)
            print("topic saved")

    def save(self, title, content):
        with open('./糗事热点.txt','a', encoding='utf-8') as f:
            f.write(title)
            f.write('\n')
            f.write(content)
            f.write('\n\n')

    def run(self):
        url_list = self.get_url_list()
        html_list = self.get_html_list(url_list)
        topics_url_list = self.get_topics_url_list(html_list)
        self.get_topics_and_save(topics_url_list)


if __name__ == '__main__':
    qiushi = QiuShiSpider()
    qiushi.run()