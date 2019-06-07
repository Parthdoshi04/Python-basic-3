from datetime import date
from datetime import time
from datetime import datetime
today = datetime.now()
t=datetime.time(datetime.now())
print("Today is: ",today)
print("Time now is: ",t)
print("Today's weekday: ",today.weekday())

wd = date.weekday(today)
days=["Mon","Tues","Wed","Thur","Fri","Sat","Sun"]
print("Todays is day number %d" %wd)
print("which is a "+days[wd])
print(today.strftime("%Y %y %a %A %b %B %d"))
print(today.strftime("%a,%d %B'%y"))
print(today.strftime("%c"))
print(today.strftime("%x"))
print(today.strftime("%X"))
print(today.strftime("%H:%M"))

