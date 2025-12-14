import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql@1920"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE alx_book_store")
mycursor.close()
mydb.close()