#-*-coding:utf-8-*-
import requests
import re

def getHTMLtext(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("")
        

def parsePage(til,text):
    try:
        r1=re.compile(r'"view_price":"[\d.]*"')
        r2=re.compile(r'"raw_title":".*?"')
        lip=re.findall(r1,text)
        lit=re.findall(r2,text)
        for i in range(len(lip)):
            price=eval(lip[i].split(':')[1])
            title=eval(lit[i].split(':')[1])
            til.append([price,title])
    except:
        print('')

def printResult(lis):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format('序号','价格','商品名称'))
    for i in range(len(lis)):
        print(tplt.format(i+1,lis[i][0],lis[i][1]))
        if lis[i][0]=='89.00':
            print('===============')

def main():
    goods='书包'
    deepth=3
    infolist=[]
    start_url='https://s.taobao.com/search?q=书包'
    for i in range(deepth):
        try:
            url=start_url+'&s='+str(i*44)
            text=getHTMLtext(url)
            parsePage(infolist,text)
        except:
            continue
    printResult(infolist)
    
main()
    