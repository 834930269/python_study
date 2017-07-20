import re
'''
>>> 834930269@qq.com
ok!
'''
test=input('please enter:')
re_mode=re.compile(r'[0-9a-zA-Z._]*@\w+.com')
if re_mode.match(test):
    print('ok!')
else:
    print('failed!')
