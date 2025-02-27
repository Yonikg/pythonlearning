import pyodbc
from pprint import pprint

# Step 1: Connect to SQL Server (connect to the 'master' database first)
conn = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=YONI\MY_MSSQL_SERVER;'
    r'DATABASE=master;'  # Connect to 'master' first to list all databases
    # r'UID=your_username;'  # Uncomment if authentication is required
    # r'PWD=your_password;'
)

cursor = conn.cursor()

# Step 2: Get all database names
cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")  # Excluding system databases
databases = [row[0] for row in cursor.fetchall()]

# Corrected print statement
print("Databases found:")
pprint(databases)  # pprint takes a single argument

cursor.execute("select ID, AcctNo, first_name, last_name, email  from Bofa_Customer.dbo.Accounts_Profile where gender = 'male'and Channel = 'saving'")  # Change to your table name
cursor.execute ("Select ChannelKey, ChannelLabel, ChannelName from ESCO.[dbo].[DimChannel]")

rows = cursor.fetchall()
for row in rows:
    pprint(row)  # Prints each row

# Step 4: Close the connection
cursor.close()
conn.close()

