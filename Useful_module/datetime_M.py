from datetime import datetime
now=datetime.now()
print(now)
print(type(now))

#创建时间
dt=datetime(2015,4,19,12,20)
print(dt)

#转换成timestamp
print(dt.timestamp())

#timestamp转换成datetime
t=dt.timestamp()
print(datetime.fromtimestamp(t))#转换到本地时间

print(datetime.utcfromtimestamp(t))#UTC时间

#str转datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

print(cday)

#datetime转str
print(now.strftime('%a, %b %d %H:%M'))

from datetime import timedelta

print(now+timedelta(hours=10))

print(now - timedelta(days=1))

print(now + timedelta(days=2, hours=12))

'''
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
加减可以直接用+和-运算符，不过需要导入timedelta这个类：
'''
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
#datetime.datetime(2015, 5, 18, 17, 2, 10, 871012)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

