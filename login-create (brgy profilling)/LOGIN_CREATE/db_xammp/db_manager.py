import mysql.connector
from mysql.connector import Error

def create_connection(self):
    try:
        # Establish MySQL connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            database='db_brgyprofilling',
            port=3306
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def close_connection(connection, cursor):
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
