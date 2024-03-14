# database.py
import mysql.connector

def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="my_chat_gpt",
        password="1234",
        database="mydatabase"
    )
    return mydb
