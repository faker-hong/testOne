import time
import urllib
from json import loads
from urllib.parse import urlencode
from 穷游网.item import BeautyItem
import scrapy
from bs4 import BeautifulSoup
import requests
import re


base_url = "http://search.qyer.com/newHotel?"
param = {
            "ajaxID": "5bf3bad67b20e5c1476b7187",
            "tab": "hotel",
            "keyword": "广州",
            "page": "4",
        }
for i in range(1, 3):
    param["page"] = i
    full_url = base_url + urlencode(param)
    response = requests.get(full_url)
    model_dict = loads(response.text)
    hotels = model_dict['data']['place_hotel']['data']['list']
    # print(hotels)
    for item in hotels:
        urllib.request.urlretrieve(item['photo'], filename='./photos/' + item['py_name'] + '.png')
        print(item['photo'])

