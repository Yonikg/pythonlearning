#my_list = [1,2,3]

for num in range (4,10,2):
    print (num)

index_count = 0

for letter in 'abcdef':
    print (f' an index {index_count} the letter {letter} ')# .format(letter, index_count))
    #index_count +=1
    index_count = index_count + 1 
    
word = 'abcd'
for item in enumerate (word):
    print (item)

#zip function
my_list1 = [1,2,3]
my_list2 = ['a','b', 'c']

for item in zip (my_list1, my_list2):
    print(item)
    
