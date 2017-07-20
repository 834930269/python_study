import re
Email=input('please enter the Email:')
re_mode=re.compile(r'<([a-zA-Z]* [a-zA-Z]*)> [\w.]*@\w+.[a-z]*')
we=re_mode.match(Email)
if we:
    print(we.groups())
else:
    print('failed!')
