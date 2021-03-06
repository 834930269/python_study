s='ABC\\-001'#对应正则表达式字符串为'ABC\-001'
#因为python本身需要转义,但用 r 前缀的话,就可以忽略转义字符了
s=r'ABC\-001'
import re
print('成功的匹配:')
print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
print('失败的匹配:')
print(re.match(r'^\d{3}\-\d{3,8}$','010 12345'))

test='用户输入的字符串'
if re.match(r'正则表达式',test):
    print('ok')
else:
    print('failed')

#切分字符串
#用正则表达式切分字符串比用固定的字符更灵活,
print('a b   c'.split(' '))
#['a', 'b', '', '', 'c'],无法识别连续的空格
#用正则表达式试试
print(re.split(r'\s+','a b   c'))
#['a', 'b', 'c']
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
#['a', 'b', 'c', 'd']

#分组
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m)
print('m.group(0): ',m.group(0),'\nm.group(1): ',m.group(1),'\nm.group(2): ',m.group(2))

'''
^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从
匹配的字符串中提取出区号和本地号码

如果正则表达式中定义了组，就可以在Match对象上用
group()方法提取出子串来。
'''
#提取时间
t='19:05:30'
m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
print(m.groups())

#这样可以直接匹配出合法时间,但有些时候,正则也无法完全验证,这时候就要配合程序了

#贪婪匹配
#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print(re.match(r'^(\d+)(0*)$', '102300').groups())
#Out[]:('102300', '')
#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。

#必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，
#加个?就可以让\d+采用非贪婪匹配：

#尽可能少 匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
#out[]:('1023', '00')

#编译
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：

    编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

    用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预
编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups()
      )
