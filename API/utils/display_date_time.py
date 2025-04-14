from datetime import datetime
def concate_zero(value):
    if value < 10:
        return '0' + str(value)
    else:
        return value

days = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def display_date_time(format = 'EU', length = 'short'):
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day 
    hour  = now. hour
    minute = now.minute
    second = now.second

    month = concate_zero(month)
    day = concate_zero(day)
    hour = concate_zero(hour)
    minute = concate_zero(minute)
    second = concate_zero(second)


    if format.lower() == 'eu':
        time_format_eu = f'{day}/{month}/{year}'
        if length == 'short':
            return time_format_eu
        elif length == 'long':
            return f'{time_format_eu} {hour}:{minute}:{second}'
    elif format.lower() == 'us':
        time_format_us = f'{month}/{day}/{year}'
        if length == 'short':
            return time_format_us
        elif length == 'long':
            return f'{time_format_us} {hour}:{minute}:{second}'

print(display_date_time())
print(display_date_time('us'))
print(display_date_time('us', 'long'))
print(display_date_time('Eu', 'long'))