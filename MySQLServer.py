import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "mysql@1920"
    )
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("database 'alx_book_store' created successfully!")
except Error as e:
    print("Error while connecting to MySQL",e)
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()