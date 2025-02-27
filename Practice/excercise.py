sentences = [
    "  Python is amazing!  ",
    "I love coding in Python.",
    "Loops, strings, and lists are powerful in Python.",
    "Python is fun!"
]


allwords = []
for sentence in sentences:
    words=  sentence.lower().strip().replace('!', '').replace('.', '').replace (',', '').split()
    allwords.extend(words) 
print (allwords)
print (len(allwords))

unique_words = set(allwords)
print (unique_words)
print (len(unique_words))

lexical_variety = len(unique_words) / len (allwords) * 100
print (lexical_variety)  



"""
1. Sum of Even Numbers
Write a Python program that takes a list of numbers and prints the sum of all even numbers using a for loop.

numbers = [12, 7, 9, 14, 22, 5, 8, 13]
Expected Output: Sum of even numbers: 56

"""

numbers = [12, 7, 9, 14, 22, 5, 8, 13]

total = 0
for num in numbers:
    if num % 2 == 0:
        total = total + num
print (total)
        
'''
    2. Remove Duplicates from a List
Write a program that removes duplicates from a given list and prints the unique values.

items = [2, 5, 7, 2, 8, 9, 5, 8, 10]
Expected Output: [2, 5, 7, 8, 9, 10]

'''
    
items = [2, 5, 7, 2, 8, 9, 5, 8, 10]
unique_items = list(set(items))
print(unique_items)


'''
Write a program that finds and prints the maximum and minimum numbers from a list without using the built-in max() and min() functions.

numbers = [12, 45, 2, 67, 34, 89, 1, 23]
Expected Output:

Maximum: 89  
Minimum: 1  



def min_func():
    numbers = [12, 45, 2, 67, 34, 89, 1, 23]
    for num in numbers:
        if num <= x:
         return num
     
print (min_func)


def nax_fun (lst)
    for num in lst:
        if num > max:
          max = num
    rerurn max




4. Reverse a List Without Using [::-1]
Write a program to reverse a given list manually using a loop.

numbers = [1, 2, 3, 4, 5]
Expected Output: [5, 4, 3, 2, 1]



'''

numbers = [1, 2, 3, 4, 5]
new_lst = []
for i in range(4, -1, -1):
    new_lst.append(numbers[i])
print(new_lst, numbers[::-1])

nums_copied = numbers.copy()
nums_copied.reverse()
print(nums_copied)