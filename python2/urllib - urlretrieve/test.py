#--*--coding:gbk--*--
import urllib

# url="http://www.iplaypython.com/"

# html=urllib.urlopen(url).read()# 方法连用

# print html

# 初学建议用单步赋值



html2=urllib.urlopen(url2)
'''
content=html2.read().decode('gbk','ignore').encode("utf-8")
print content
'''
code=html2.getcode()

print type(code)
if code == 200:
    print html2.read()
    print html2.info()
else:
    print "404"
# 中文会出错,明天看
# 用gbk就没错了= =
