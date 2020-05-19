"""
    获取所有歌手的信息
"""
import requests
from bs4 import BeautifulSoup
from 网易云爬虫 import sql

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "cookie": "mail_psc_fingerprint=d9151ab49bbcf7550b4ed0dee38459d3; usertrack=CrHud1yI7o8Ts12MAwoaAg==; _iuqxldmzr_=32; _ntes_nnid=a2f82e806ee40acb8a45a26d85607821,1552477843293; _ntes_nuid=a2f82e806ee40acb8a45a26d85607821; WM_TID=Afu2aGkohp9EAUUEVQNpx2sp%2BR6529z%2F; vinfo_n_f_l_n3=87175a514966667b.1.0.1552738266033.0.1552738290223; nts_mail_user=hongcheng97@163.com:-1:1; _ga=GA1.2.2004149700.1565916852; P_INFO=hongcheng97@163.com|1565919570|0|mail163|00&99|zhj&1565852368&other#zhj&330100#10#0#0|&0|urs&mail163|hongcheng97@163.com; WM_NI=LytME3m4k2%2BTfw%2B41IIC2Sh24fO6X8EkLzPTe5SY0C%2BxzwAdZtjAe7LocuaNkRqiL4kdXXFjmapJCJ2j0IXQVSHUMoZUCiet%2FfUNm%2FpAArlic2GT4AcPH9lidROxKTppT3k%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccce73b2ec9f8cf05293b08aa2c44f938e8ebabc3fa1b4ba83bb21b0979898b42af0fea7c3b92a90a7bcaec839afeca5d3aa60a6a9e5d5b4438b9dfeb4eb3af8ba81d7db3487b5849bd360a7eb9dbab349e9a8b698c4709aaca6a2e83d90b1ad96e446a98ebf8acf40a9bc98b9c562afbfc0abc242f2b600aadb5b968d88b6d0659a8b8d8ae880edba9baff025b49f8f93ef63a1ee89b5b74ba19088daef63a88e8199ca60b4b09cd4ea37e2a3; ntes_kaola_ad=1; __remember_me=true; JSESSIONID-WYYY=jUUfrUwZvcf7hGo4aAcMYxVd%2BXJ6lhIcAoD2sxWtMSQefYO7YepwIW%2FHFI%2Bjss3UK6YcHatZ7DnhWDhr3j1c368lONdHV7k0xj7%2FJ7FUrV3V6Q59VjkXm3BmtOC30uHVMX%2BQqB4U6VGPprK%5CRgWNwV5Hdh%2BuZhvjePAJcOGPlUyTtaZB%3A1566190966603; MUSIC_U=9de0b492647e4661271b0758c4e7f5050e77f31bf7d22dae5026dc5e303f5035161d822c4e27a4eb30ca6eaa84c92beaeb8d631e679e0f7255e1e919a41e6d837955a739ab43dce1; __csrf=e3e443dbed5c72f4aff1a2c22cf6affe"
}


def save_artist(group_id, initial):
    params = {
        "id": group_id,
        "initial": initial
    }
    response = requests.get("https://music.163.com/discover/artist/cat", params=params)
    soup = BeautifulSoup(response.content, "html.parser")

    hot_artists = soup.find_all('a', attrs={"class": "msk"})
    artists = soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    for artist in hot_artists:
        artist_id = artist["href"].replace("/artist?id=", "").strip()
        artist_name = artist["title"].replace("的音乐", "").strip()
        try:
            sql.insert_artist(artist_id, artist_name)
        except Exception as e:
            # 打印错误日志
            print(e)

    for artist in artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            sql.insert_artist(artist_id, artist_name)
        except Exception as e:
            # 打印错误日志
            print(e)

gg = 4003

save_artist(gg, 0)
for i in range(65, 91):
    save_artist(gg, i)