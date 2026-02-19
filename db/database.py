# Database Setup and Schema

# Import necessary libraries
import sqlite3
from sqlite3 import Error

# Create a database connection

def create_connection(db_file):
    """ create a database connection to the SQLite database """ 
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(e)
    return conn

# Create a table

def create_table(conn):
    """ create a table in the database """ 
    try:
        sql_create_table = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
        '''
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print("Table 'users' created successfully.")
    except Error as e:
        print(e)

# Main function to setup database

def main():
    database = "db.sqlite"
    conn = create_connection(database)
    if conn:
        create_table(conn)
        conn.close()

if __name__ == '__main__':
    main()