
def display (row1,row2,row3):
    print (row1)
    print (row2)
    print (row3)
row1=  ['x', 3, '5']
row2 = ['','','']
row3= ['Yo', 'Xo', 'Xo']

row3[2] = 'X'
display (row1, row2, row3)
'''
def user_choice():
    
    choice = 'Wrong'
    
    while choice.isdigit() == False:
        
        choice = input ('please enter a number (0,10):')
        
    return int(choice)

user_choice (3)
    
    
    def user_choice():
    
    Choice = 'Wrong'
    
    while choice.isdigit() == False:
        
        choice = input ('please enter a number (0,10):')
        
    return int(choice)

user_choice (3)
  '''
  
def user_choice():
    choice = 'Wrong'  # Initialize as a non-numeric string to enter the loop
    
    while not choice.isdigit() or not (0 <= int(choice) <= 10):  # Check if it's a number and in range
        choice = input("Please enter a number (0-10): ")
        
        if not choice.isdigit():  # If input is not numeric
            print("Invalid input. Please enter a number.")
        elif not (0 <= int(choice) <= 10):  # If number is out of range
            print("Number out of range. Please enter a number between 0 and 10.")

    return int(choice)  # Convert input to an integer and return it

# Example usage
result = user_choice()
print(f"You entered: {result}")
   