#--*--coding:gbk--*--
import urllib

# url="http://www.iplaypython.com/"

# html=urllib.urlopen(url).read()# ��������

# print html

# ��ѧ�����õ�����ֵ



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
# ���Ļ����,���쿴
# ��gbk��û����= =
