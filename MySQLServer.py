import mysql.connector
from mysql.connector import Error
def create_database():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "mysql@1920"
        )
        if connection.is_connected():
            mycursor = connection.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error:
     print(Error)
    finally:
     if connection.is_connected():
        mycursor.close()
        connection.close()
if __name__== "__main__":git 
   create_database()