from numpy import arr



first_name = 'Yonas'
last_name = 'G'
marital_status = 'Single'
is_married = False
date_of_birth = 1990
skills= ['SQL', 'SSIS', 'SSRS', 'Python'] 
address = {
    'country' : 'USA',
    'state': 'Marryland',
    'city': 'Silver Spring',
    'streetname': '16th Ave',
    'zipcode' : '20192' 
     }

'''
age = int(input ('What is your age? '))
print (type(age))
if age >= 18:
    print ('You are old enough to drive')
else:
    print ('You are too young to drive')
    
'''
for skill in skills:
    print (skill.upper())

skills.pop()
print (skills)

skills.insert (2, 'MangoDB')
print (skills)



def my_fun (a,b):
    total = a + b
    return total
    
print (my_fun (50,50))
""" 
def sum_all_nums (n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total  """
    
    
def sum_all_nums(n):
    return sum(range(n+1))


print(sum_all_nums(100))
    

    
    
# * if you put this in function it will only accept numbers
# modlue function and package
# the difference b/n module and  pacakge is
#Module may have one or more fun
#package might have one or more moule
#__init__.py this will change into  directory
  
  \
  # Step 2: Define the INSERT query
sql = """
Insert into Movies ([MovieID], [MovieTitle], [YearOfRelease], [Description], 
                    [LengthInMinutes], [Director], [MoviePhotoPath], [Like], [WebSite]) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Step 3: Define values as a tuple (each ? matches a value in this order)
values = (12, "Next in line", "2024", "A great movie", "120", "John Doe", "path/to/photo.jpg", 1, "http://example.com")

# Step 4: Execute the INSERT query
cursor.execute(sql, values)

# Step 5: Commit the transaction to save the record
conn.commit()

print("Data inserted successfully!")

# Step 6: Verify by selecting the inserted row
cursor.execute("SELECT * FROM Movies WHERE MovieID = ?", (11,))
for row in cursor.fetchall():
    pprint(row)

# Step 7: Close the connection
cursor.close()
conn.close()



 Read data from a specific table (Change 'Movies' to a table that exists in each database)
    if "Movies" in tables:
        cursor_db.execute("SELECT * FROM Movies")
        rows = cursor_db.fetchall()
        print(f"Data from {db}.Movies:")
        for row in rows:
            print(row)

    # Close the connection for this database
    cursor_db.close()
    conn_db.close()