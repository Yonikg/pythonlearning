#1
'''

def lesser_of_the_two (a,b):
    if a % 2 ==0 and b % 2 == 0:
        return min (a,b)
    else:
        return max (a,b)

result = (lesser_of_the_two (10,20))
print (result)


def animal_crackers (text):
    #wordlist = text.split()
    for item in animal_crackers:
        if range (animal_crackers , [0] == 'L')
            print ('True')
        else:
            print ('False')
            
print (animal_crackers('Lelvelhead Lima'))

def animal_crackers(text):
    if text[0].lower() == 'l':  # Check if the first character is 'L' (case-insensitive)
        return True
    else:
        return False

# Example usage:
print(animal_crackers('levelhead lima'))  # True
print(animal_crackers('Crazy Kangaroo'))  # False
print(animal_crackers('lion King'))       # True
print(animal_crackers('Apple lnt'))       # False
'''


def makes_twenty(n1, n2):
    if n1 + n2 == 20:
        return  True  
    else:
        return False

result = makes_twenty(1, 10)
print (f' based on the above calculation the desired result is {result}!')




def splicer (mystring):
    if len (mystring) %2== 0:
        return 'EVEN'
    else:
        return mystring [0]

names = splicer('Andy') 
print (names )


def gradescore(score):
    # Check if the score is within a valid range
    if not (0 <= score <= 100):
        return 'Out of range'
    
    # Assign grades based on the score
    if score >= 90:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:  # If score is 59 or below
        return 'F'

# Example usage
grade = gradescore(200)
print(f"Your grade is: {grade}")  # Expected output: 'Out of range'

#grade = gradescore(85)
#print(f"Your grade is: {grade}")  # Expected output: 'B'


        