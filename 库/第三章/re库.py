import re
# re.search是全文匹配
# re.match是从开始
match=re.search(r'[1-9]\d{5}','BIT 100081')
print(match)

match=re.match(r'[1-9]\d{5}','BIT 100081')
print(match)

#findall 返回全文能匹配的子串
#split 将一个字符串按照正则表达式进行分割

m=re.search(r'[1-9]\d{5}','BIT100081 TSU100084')
print(m.string,m.re,m.pos,m.endpos,m.span)

match=re.search(r'PY.*N','PYANBNCNDN')
print(match.group(0))
#正则采用贪婪匹配,即匹配最长的
'''
?:最小匹配
*? 前一个字符0次或无限次扩展

'''
