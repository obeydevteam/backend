import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(host="localhost", user="root", passwd="password")

cursor = db.cursor()

## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'datacamp' database
cursor.execute("CREATE DATABASE sample")
