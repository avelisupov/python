import os.path
from time import strptime
import time
import datetime
import shutil  
from datetime import timedelta 
from time import mktime
from datetime import datetime



def time_check():
    src = ('C:/Users/avel isupov/Desktop/A/Test.txt')
    des = ('C:/Users/avel isupov/Desktop/B')
    mod = timedelta(days=1)
    check_time = (time.ctime(os.path.getmtime(src)))
    convert1 = time.strptime(check_time,"%a %b %d %H:%M:%S %Y")
    convert2 = (datetime.fromtimestamp(mktime(convert1))) 
    back = datetime.today() - timedelta(days=1)
    if convert2 <= back:
        shutil.copy(src,des) 
        print ("yes")
    print (back,convert2)

time_check()
