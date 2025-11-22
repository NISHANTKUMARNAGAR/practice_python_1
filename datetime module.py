#---------------------date class
"""from datetime import date
d=date(2000,12,29)
print(d)
#for today's date
t=date.today()
print(t)
print(t.day)
print(t.year)
print(t.month)
#for date from timestamp 1887639468
from datetime import datetime
ts=datetime.fromtimestamp(1887639468)
print(ts)
print(ts.date())
#can also convert date to string
t=date.today()
tstr=t.isoformat()
print(tstr)
print(type(tstr))"""

#-----------------------time class
"""from datetime import time
t=time(14,30,0)
print(t)"""

#--------------------------datetime class
"""from datetime import datetime
a=datetime(1999,12,12)
print(a)
b=datetime(1999,12,12,14,30,12,324569)
print(b)
#to print its specifics
print(b.year)
print(b.month)
print(b.hour)
print(b.minute)
#for timestamp from unix epoch
print(b.timestamp())
#for current date,time
t=datetime.now()
print(t)
#to convert datetime to string
tstr=datetime.isoformat(t)
print(type(t))
print(type(tstr))
#to convert datetime object to formatted string
n=datetime.now()
formatted=n.strftime("%y-%m-%d %H:%M:%S")
print(formatted)
#to convert from string to datetime object
datestr=formatted
dt=datetime.strptime(datestr,"%y-%m-%d %H:%M:%S")
print(dt)
print(type(dt))"""

#--------------------------timedelta class
"""from datetime import timedelta,datetime
n=datetime.now()
print(n)
newn=n+timedelta(days=2) #add 2 days
print(newn)
secnewn=n+timedelta(days=730) #add 2 years
print(secnewn)
#to find difference
print("time difference: ",newn-n)
td=newn-n
print(td)
#time difference in seconds
print(td.total_seconds())"""
# - is normally subtract but here its behaving like a dunder
# method its altered by operator overloading