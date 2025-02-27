'''
Numbers ( int, float, complex)
strings - any text in prgramming language
lsit - list of items
Dictionary --- Key values like Age, 
Set
Tuple  looks like list but can't be modified it is immutable 
Set  -- dosen't allow duplicates {} removes duplicates 

print (20, type(20))
print (20.1, type (20.1))
print (str(10), type (str(10)))

#string can be a single or triple comment
print ('Yonas annual income is ' + str ('2,500,00') + ' and he is super rich')
'''
'''
#dictionary
{
    ''
}
'''
from datetime import datetime, timedelta

def date_check(getedate):
    if getedate > 30:
        print('Date is greater than 30')
    elif getedate <= 10:
        print('Date check correctly updated the date and time value')
    else:
        print('Date is between 11 and 30')

# Get the current day of the month
current_date = datetime.now().day
date_minus_5 = current_date - timedelta(days=5)
print(f"Current day of the month: {current_date}")

# Pass the current day to the function
date_check(current_date)


