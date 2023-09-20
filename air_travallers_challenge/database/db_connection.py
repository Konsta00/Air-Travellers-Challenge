import mysql.connector

# Function to establish a database connection
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="flight_game"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to execute an SQL query
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        return cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to fetch data from the database
def fetch_data(connection, query, data=None):
    cursor = execute_query(connection, query, data)
    if cursor:
        return cursor.fetchall()
    return None
