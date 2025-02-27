iterable = [1,2,3,4,5,6, 7, 8,9,10]
for it in iterable:
    #for even number %2==0
    #for odd number %%2==1
    if it %2==0:
     print (f'odd number: {it}')
    elif it %2==1: 
        print(f'even number: {it}. This is even number')
    else:
        print ('This is out of range');
        
list_sum = 100
 
for num in iterable:
     list_sum = list_sum + num
     
print (f' the total number of combined result is: {list_sum}'.upper())

letter = 'This is my worrld'
for ai in letter:
    print(ai.upper())
    
tup = [(1,2), (3,4), (5,6), (7,8)]
for item in tup:
    print (item)
    

tupp = [(1,2), (3,4), (5,6), (7,8)]

for a,b in tupp:
    print (b)
    
d = {'orage':21, 'apple':3}
for key,value in d.items():
    print (value)

