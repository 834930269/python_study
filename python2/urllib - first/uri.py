# -*-coding: utf-8 -*-

import urllib
url="http://www.163.com/"
print(help(urllib.urlopen))
html=urllib.urlopen(url)
# 更改编码为相应编码
# print(html.read().decode("gbk").encode("utf-8"))

# print html.info()
# 获取头部信息
print html.getcode()
# 获取网页状态码
"""
 只有状态码是200才可以抓取
 200表示可以正常访问
 301是重定向
 404是不存在
 403是禁止访问
 500状态
 HTTP权威指南,专门介绍http协议
 Web开发必备
"""
print html.geturl()


#网页抓取完,下载网页

urllib.urlretrieve(url,"C:\\Users\\Public\\Desktop\\abc.txt")

html.close()
