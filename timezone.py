import pytz
from datetime import datetime
from datetime import time
x=pytz.timezone('Asia/Kolkata')
now=datetime.now()
y=now.astimezone(x)
print(y)
