#--*--coding:gbk--*--

import urllib

def callback(a,b,c):
    '''
    @a 是到目前为止传递的数据块数量。
    @b 是每个数据块的大小,单位的byte,字节。
    @c 远程文件的大小。(有时候会返回-1)
    '''
    down_progress = 100.0*a*b/c
        
    if down_progress>100:
        down_progress=100

    print "%.2f%%" % down_progress
    
'''
1.传入网址,网址的类型一定是字符串.

2.传入的,本地的网页保存路径+文件名

3.一个函数的调用，我们可以任意来定义这个函数的行为,但一定要保证这个参数有三个参数

(1).到目前为止传递的数据块数量。
(2).是每个数据块的大小,单位的byte,字节。
(3).远程文件的大小。(有时候会返回-1)
'''
url="http://www.iplaypython.com/"
url2="http://www.python.org"
url3="http://be-sunshine.cn"
local="L:\\Python搜索爬虫视频教程文件夹\\斯巴达Python搜索爬虫抓取第2期视频教程(已加密)\\index.html"

urllib.urlretrieve(url2,local,callback)



