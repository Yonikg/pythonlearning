def convert_celsius_to_fahrenheit (degree):
   celcus = 25
   fahrenite = (celcus * 9/5) + 32.
   return fahrenite

print (convert_celsius_to_fahrenheit(20))

#temp_f = convert_celsius_to_fahrenheit


def change (distance):
    km = distance/1000
    return km
print (round(change(4311),2 ))



def metertokm (convertvalue):
    km = convertvalue /100
    return km
print (round(metertokm(40),1))


def season(month):
    
    if month in ['December', 'January', 'February']:
        return 'It is a winter season'
    elif month in ['March', 'April', 'May']:
        return 'It is spring season'
    elif month in ['June', 'July', 'August']:
        return 'It is summer baby, go on vacation'
    elif month in ['September', 'October', 'November']:
        return 'It is autumn season, prepare for winter'
    else:
        return 'Invalid season'

print(season('march').lower())  # Convert result to lowercase

    


