"""
    根据爬取到的歌手id来爬取歌手的专辑id
"""
import requests
from bs4 import BeautifulSoup
from 网易云爬虫 import sql
import time


class Album(object):
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

    def save_albums(self, artist_id):
        # params= {
        #     "artist_id": artist_id,
        #     "limit": '200'
        # }
        url = "https://music.163.com/artist/album?id="+artist_id+"&limit=200"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup)
        albums = soup.find_all('a', attrs={'class': 'msk'})
        for album in albums:
            album_id = album["href"].replace("/album?id=", "")
            print(album_id)
            print(artist_id)
            sql.insert_album(album_id, artist_id)


if __name__ == '__main__':
    artists = sql.get_all_artist()
    my_album = Album()
    for i in artists:
        print(type(i[0]))
        try:
            my_album.save_albums(str(i[0]))
        except Exception as e:
            print(str(i) + ':' + str(e))
            time.sleep(5)