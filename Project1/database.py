#This file is responsible for database connections and SQL statements to insert and fetch data from existing databse
#File : database.py
#Author: Nikhil Divekar

import sqlite3

#Creates table and inserts data from singup window into login.db
def createTable():
    connection = sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS (USERNAME TEXT NOT NULL, EMAIL TEXT, PASSWORD TEXT)")
    connection.execute("INSERT INTO USERS VALUES(?,?,?)",('nikhil','nd@gmail.com','abcd1234'))
    connection.commit()
    result = connection.execute("SELECT * FROM USERS")
    for data in result:
        print("Username: ", data[0])
        print("Email: ", data[1])
        print("Password: ", data[2])
    connection.close()
    
createTable()
