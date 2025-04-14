from datetime import datetime
from datetime import timedelta
import schedule
import time

today = datetime.now()
fromatedtime = today.strftime ('%d')
print (fromatedtime)


print ('Do something')

schedule.every().day.at("11:02").do(task1)

# If you only want it to run once, then no loop is required
# Else if you want it to run once per day then add the while True loop
schedule.run_pending()
time.sleep(1)