# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
r=requests.get('https://www.amazon.cn/gp/product/B01M8L5Z3Y')
print(r.status_code)
print(r.headers)
#因为是python直接传递的参数发送的请求,所以肯定是爬虫
#模拟浏览器
kv={'user-agent':'Mozilla/5.0'}
url='https://www.amazon.cn/gp/product/B01M8L5Z3Y'
r=requests.get(url,headers=kv)
print(r.status_code)
print(r.request.headers)