#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-15 16:27
# Author:guqingqing
# @File:4.15.py
# @Software:PyCharm
import requests

#
#url = "http://127.0.0.1/Home/Goods/search.html?q=%E6%89%8B%E6%9C%BA"

url = "http://127.0.0.1/Home/Goods/search.html"

pama={
    "q":"%E6%89%8B%E6%9C%BA"
}

r = requests.get(url,params=pama)

print(r.text)