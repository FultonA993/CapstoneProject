import pyodbc
# Set up the connection string
server = 'capstone2023.database.windows.net'
database = 'capstone2023'
username = 'ymejia'
password = 'Password01!'
driver= '{ODBC Driver 18 for SQL Server}'
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

def connect_db():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    return cursor

#used to query the database
'''def fetch_all_data():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Execute a query to fetch all data from the Employee table
    query = "SELECT * FROM Payroll"
    cursor.execute(query)

    # Fetch all the rows and columns from the query result
    row = cursor.fetchall()
    print(row)

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    return row

data = fetch_all_data()
for row in data:
    print(row)'''
