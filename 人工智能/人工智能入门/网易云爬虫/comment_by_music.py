"""
    根据根据的id获取评论
"""
import json
import threading
import time

import pymysql
import requests
from bs4 import BeautifulSoup
from 网易云爬虫 import sql


class Comment(object):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': "mail_psc_fingerprint=d9151ab49bbcf7550b4ed0dee38459d3; usertrack=CrHud1yI7o8Ts12MAwoaAg==; _iuqxldmzr_=32; _ntes_nnid=a2f82e806ee40acb8a45a26d85607821,1552477843293; _ntes_nuid=a2f82e806ee40acb8a45a26d85607821; WM_TID=Afu2aGkohp9EAUUEVQNpx2sp%2BR6529z%2F; vinfo_n_f_l_n3=87175a514966667b.1.0.1552738266033.0.1552738290223; nts_mail_user=hongcheng97@163.com:-1:1; _ga=GA1.2.2004149700.1565916852; P_INFO=hongcheng97@163.com|1565919570|0|mail163|00&99|zhj&1565852368&other#zhj&330100#10#0#0|&0|urs&mail163|hongcheng97@163.com; WM_NI=LytME3m4k2%2BTfw%2B41IIC2Sh24fO6X8EkLzPTe5SY0C%2BxzwAdZtjAe7LocuaNkRqiL4kdXXFjmapJCJ2j0IXQVSHUMoZUCiet%2FfUNm%2FpAArlic2GT4AcPH9lidROxKTppT3k%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccce73b2ec9f8cf05293b08aa2c44f938e8ebabc3fa1b4ba83bb21b0979898b42af0fea7c3b92a90a7bcaec839afeca5d3aa60a6a9e5d5b4438b9dfeb4eb3af8ba81d7db3487b5849bd360a7eb9dbab349e9a8b698c4709aaca6a2e83d90b1ad96e446a98ebf8acf40a9bc98b9c562afbfc0abc242f2b600aadb5b968d88b6d0659a8b8d8ae880edba9baff025b49f8f93ef63a1ee89b5b74ba19088daef63a88e8199ca60b4b09cd4ea37e2a3; ntes_kaola_ad=1; JSESSIONID-WYYY=Hm1zzqgod9fgF0YiZQSGrDiO7AJbza5Ur9IbEulDRhCVSPmGJUsNxFQP8Ey8%2B5ZVWBCh%2Bq6onmSYQZemA4TFGwd3EO4SRAQzd0GSE7JkkT9Q4r%2FQBOcOqpDYIGry%2FZSa2ZCKvFYiZiMK1lcO0xIv%2B54ix6fhaFlT8aUb%5CZXq%5C0zgxVsY%3A1566194448230",
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    params = {
        'csrf_token': ''
    }

    data = {
        'params': 'Ak2s0LoP1GRJYqE3XxJUZVYK9uPEXSTttmAS+8uVLnYRoUt/Xgqdrt/13nr6OYhi75QSTlQ9FcZaWElIwE+oz9qXAu87t2DHj6Auu+2yBJDr+arG+irBbjIvKJGfjgBac+kSm2ePwf4rfuHSKVgQu1cYMdqFVnB+ojBsWopHcexbvLylDIMPulPljAWK6MR8',
        'encSecKey': '8c85d1b6f53bfebaf5258d171f3526c06980cbcaf490d759eac82145ee27198297c152dd95e7ea0f08cfb7281588cdab305946e01b9d84f0b49700f9c2eb6eeced8624b16ce378bccd24341b1b5ad3d84ebd707dbbd18a4f01c2a007cd47de32f28ca395c9715afa134ed9ee321caa7f28ec82b94307d75144f6b5b134a9ce1a'
    }

    def get_comments(self, music_id, flag):
        self.headers['Referer'] = 'http://music.163.com/playlist?id=' + music_id
        if flag:
            r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + music_id,
                              headers=self.headers, params=self.params, data=self.data)
        else:
            r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + music_id,
                              headers=self.headers, params=self.params, data=self.data)
        return r.json()

    def get_comments_two(self,music_id, limit, offset):
        # 这个接口也能正常获取到数据， limit为每页的数量，offset为偏移量。
        # 0位置偏移offset，获取limit条数据
        url = "http://music.163.com/api/v1/resource/comments/R_SO_4_%s?limit=%s&offset=%s" % (music_id, limit, offset)
        response = requests.get(url, headers=self.headers)
        comment = json.loads(response.content)
        name = comment['comments'][0]['user']['nickname']  # 姓名
        content = comment['comments'][0]['content']        # 内容


if __name__ == '__main__':

    my_comment = Comment()

    def save_comments(musics, flag, connection0):
        for i in musics:
            my_music_id = i[0]
            # print(my_music_id)
            try:
                comments = my_comment.get_comments(my_music_id, flag)
                print(comments)
                if comments['total'] > 0:
                    sql.insert_comments(my_music_id, comments['total'], str(comments), connection0)
            except Exception as e:
                # 打印错误日志
                print(my_music_id)
                print(e)
                time.sleep(5)


    music_before = sql.get_before_music()
    music_after = sql.get_after_music()

    # pymysql 链接不是线程安全的
    connection1 = pymysql.connect(host='localhost',
                                  user='root',
                                  password='123456',
                                  db='xhx',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

    connection2 = pymysql.connect(host='localhost',
                                  user='root',
                                  password='123456',
                                  db='xhx',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

    t1 = threading.Thread(target=save_comments, args=(music_before, True, connection1))
    t2 = threading.Thread(target=save_comments, args=(music_after, False, connection2))
    t1.start()
    t2.start()