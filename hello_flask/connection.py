import pyodbc
# Set up the connection string
server = 'capstone2023.database.windows.net'
database = 'capstone2023'
username = 'ymejia'
password = 'Password01!'
driver= '{ODBC Driver 17 for SQL Server}'
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
try:
    conn = pyodbc.connect(connection_string)
    print("Successfully connected to the database!")
    print(connection_string)    
except pyodbc.Error as e:
    print("Failed to connect to the database:", e)

# close the connection
conn.close()