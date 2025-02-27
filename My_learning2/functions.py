def my_fun(name):
    print (f'hello {name}')
my_fun ('Yonas')



d  = 4 % 5
if d == 0:
    print ('this is odd')
else:
    print ('this is even')
    

work_hour = [('Yonas', 400), ('B', 599), ('c', 600)]
print(work_hour)
      
def employee_of_the_month (work_hours):
    currmax = 0
    employee_of_the_month = ''
    
    for employee, hour in work_hours:
        if hour >currmax:
            hour = currmax
            employee_of_the_month = employee
        else:
            pass
    return (employee, hour)
