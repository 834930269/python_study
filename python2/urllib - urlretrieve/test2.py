#--*--coding:gbk--*--

import urllib

def callback(a,b,c):
    '''
    @a �ǵ�ĿǰΪֹ���ݵ����ݿ�������
    @b ��ÿ�����ݿ�Ĵ�С,��λ��byte,�ֽڡ�
    @c Զ���ļ��Ĵ�С��(��ʱ��᷵��-1)
    '''
    down_progress = 100.0*a*b/c
        
    if down_progress>100:
        down_progress=100

    print "%.2f%%" % down_progress
    
'''
1.������ַ,��ַ������һ�����ַ���.

2.�����,���ص���ҳ����·��+�ļ���

3.һ�������ĵ��ã����ǿ������������������������Ϊ,��һ��Ҫ��֤�����������������

(1).��ĿǰΪֹ���ݵ����ݿ�������
(2).��ÿ�����ݿ�Ĵ�С,��λ��byte,�ֽڡ�
(3).Զ���ļ��Ĵ�С��(��ʱ��᷵��-1)
'''
url="http://www.iplaypython.com/"
url2="http://www.python.org"
url3="http://be-sunshine.cn"
local="L:\\Python����������Ƶ�̳��ļ���\\˹�ʹ�Python��������ץȡ��2����Ƶ�̳�(�Ѽ���)\\index.html"

urllib.urlretrieve(url2,local,callback)



