
# coding: utf-8

# In[5]:



import base64

def safe_base64_decode(s):
    return base64.b64decode( s + b'=' * (( 4 - len(s) % 4 ) % 4) )
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
print(safe_base64_decode(b'YWJjZA=='),safe_base64_decode(b'YWJjZA'))


# In[218]:

import re
t='545345235'
m=re.match('^([0-13-9][0-9]*|23[3]{1,}[^3]\d*|2[^3][0-9]{0,}|2(?!3))',t)
print(m)


# In[ ]:




# In[ ]:



