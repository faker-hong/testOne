import requests
"""
    人人网模拟登陆
"""


def login_test():
    # 创建session对象，可以保存Cookie值
    sesion = requests.session()

    # 处理 headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # 3需要登录的用户名和密码
    data = {"email": "18757179539", "password": "*******"}

    # 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
    sesion.post("http://www.renren.com/PLogin.do", data=data)

    #  ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
    response = sesion.get("http://www.renren.com/410049765/profile")

    # 打印响应内容
    print(response.text)


def login_test_two():
    # 如果时间长了，cookie就会失效，导致无法正常访问
    # 改方法需要先登陆获取cookie
    url = "http://www.renren.com/410049765/profile"
    headers = {
        "Cookie": 'anonymid=jzchpbo4-gaqcak; depovince=ZJ; _r01_=1; JSESSIONID=abcjxPyBjwn7dbwA1OuYw; ick_login=946b6291-900d-4d76-827b-e4ce65478181; ick=9a10c89e-7139-47fa-ba2a-6c98c55de653; XNESSESSIONID=af74aef82a28; jebe_key=ae779ae5-90f3-41a7-a2fc-9818ea42fd95%7Cdf0c8a8ca9140b68d62c2102d53ae3d2%7C1565862004632%7C1%7C1565862005733; jebe_key=ae779ae5-90f3-41a7-a2fc-9818ea42fd95%7Cdf0c8a8ca9140b68d62c2102d53ae3d2%7C1565862004632%7C1%7C1565862005736; first_login_flag=1; ln_uact=18757179539; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; wp_fold=0; jebecookies=2ff064b5-38e8-4a1f-ba40-554e427251f0|||||; _de=24854B8B741EB76D2F050BDC90D8E8AF; p=7167dc5c64a1eba9e3a985a8597868cb1; t=56410f63dc18317b19e83790392ea6d91; societyguester=56410f63dc18317b19e83790392ea6d91; id=971928831; xnsid=67dad13b; loginfrom=syshome'
    }

    response = requests.get(url, headers=headers)
    print(response.text)


if __name__ == '__main__':
    login_test()
