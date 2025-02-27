def calculate_rectangle_area  (length, width):
    area = length * width
    return area

print (calculate_rectangle_area(50,10))


def volume_of_prisim (length, width, height):
    volume = length * width * height
    return volume

print (volume_of_prisim (10,10,10))

def xyz(*a):
    print(a)
xyz(7,9,1,1,1,1, 90)

xyz()
def zzz (**a):
    print (a)
zzz(name = 'yoni', age = 25, nationality = 'Ethiopia')

# 1 * is tuple and 2 is dict  --- To pack and unpack

def edu_lv (a,b):
    return (ed )