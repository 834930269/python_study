# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import time
'''
r=requests.get("http://www.baidu.com")
print(r.status_code)#200成功
print(type(r))
print(r.headers)
#print(r.content)#HTTP响应的二进制形式
print(r.encoding,'    ',r.apparent_encoding)
#encoding:猜测的响应内容编码方式
#apparent_encoding:分析出的
#如果header中不存在charset,认为是ISO-8859-1
'''
#爬取网页的通用代码框架
def getHTMLText(url):
    try:
        kv={'user-agent','Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status() #如果状态不是200,引发HTTPError
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '爬取失败'
if __name__ == '__main__':
    url='http://www.baidu.com'
    t1=0.0
    for i in range(100):
        t2=time.time()
        getHTMLText(url)
        t3=time.time()
        t1+=(t3-t2)
    print('总时间:',t1)
