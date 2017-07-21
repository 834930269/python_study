
# coding: utf-8

# In[ ]:

#!/usr/bin/env python3

# Author: Lxy
# Filename: register_login.py

import hashlib

db = {}

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    passwd = db.get(username, -1)
    print(username)
    if passwd == -1:
        db[username] = get_md5(password + username + 'the-Salt')#加盐,即使简单的密码也会被加密的很复杂
        print('注册成功！')
    else:
        print('用户已存在！')

def login(username, password):
    passwd = db.get(username, -1)
    if passwd == -1:
        print('用户名不存在！')
    elif get_md5(password + username + 'the-Salt') != passwd:
        print('密码不正确！')
    else:
        print('欢迎您，%s' % username) 

print('register:')
user = input('user:')
password = input('password:')
register(user, password)
print('login:')
user = input('user:')
password = input('password:')
login(user, password)


# In[ ]:



