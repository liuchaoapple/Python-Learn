from datetime import datetime
#datetime是Python处理日期和时间的标准库

now = datetime.now()
print(now)
print(type(now))

#datetime转换为timestamp
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())

#timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))