# Corrected print statement
#print("Databases found:")
#pprint(databases)  # pprint takes a single argument

cursor = conn.cursor()
cursor.execute("Select ChannelKey, ChannelLabel, ChannelName, ETLLoadID, MachineName from ESCO.[dbo].[DimChannel]")  

# Step 3: Fetch and print the results
rows = cursor.fetchall()
for row in rows:
   pprint(row)  # Prints each row

# Step 4: Close the connection
cursor.close()
conn.close()



# Loops, function, List, 