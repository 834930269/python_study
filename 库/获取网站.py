import requests
r=requests.get('http://python123.io/ws/demo.html')
#print(r.text)
demo=r.text
from bs4 import BeautifulSoup#后面的是类
soup=BeautifulSoup(demo,'html.parser')#第一个参宿是信息,解释器html.parse
#print(soup.prettify())
1#BeautifulSoup库是解析、遍历、维护、"标签树"的功能库.
#名称 Name 属性 Attributes
#四种解释器
'''
1.html.parse
2.lxml
3.xml
4.html5lib
'''
#元素
'''
1.Tag 标签<>
2.Name 标签的名字<p>=p
3.Attributes 标签的属性 字典形式组织,格式 <tag>.Attributes
4.NavigableString 标签内费属性字符串 <p>...(中间这部分)...</p>格式<tag>.string
5.Comment 标签内字符串注释部分 一种特殊的Commnet类型
'''
print(soup.title)
print(soup.a.name)
print(soup.a.parent.parent.name)#父亲的父亲
print(soup.a.attrs)
print(soup.a.attrs['class'],type(soup.a.attrs))
print(soup.a.string),print(soup.p.string)
'''
标签树的下行遍历
.contents 子节点的列表,将<tag>所有儿子节点存入列表
.children 子节点的迭代类型,与.contents类似,用于循环遍历儿子节点
.descendants 子孙节点的迭代类型,包含所有子孙节点,用于循环遍历
'''
print(soup.head)
print(soup.head.contents)
print(soup.body.contents,'\n'),print('len: ',len(soup.body.contents))
'''
上行遍历
.parent 节点的父亲标签
.parents 返回节点的先辈标签
'''
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
'''
平行遍历
.next_sibling 返回按照HTML文本顺序的下一个平行节点标签
.previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
.next_siblings 迭代类型,返回按照HTML文本顺序的后续所有平行节点标签
.previous_siblings 迭代类型,返回按照HTML文本顺序的前序所有平行结点标签
'''