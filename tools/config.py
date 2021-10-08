import time
import datetime
import os

timestamp = 1619343283773

# 转换成localtime
time_local = time.localtime(timestamp / 1000)
# 转换成新的时间格式(精确到秒)
dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
print(dt)  # 2019-10-11 14:15:56

d = datetime.datetime.fromtimestamp(timestamp / 1000)
# 精确到毫秒
str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
print(str1)  # 2019-10-11 14:15:56.514000


