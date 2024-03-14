# login_aux.py
import sys
sys.path.append('/home/itay/my_chat_gpt/')
from app.database import connect_to_database

def login_user(username: str, password: str):
    mydb = connect_to_database()
    cursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    user = cursor.fetchone()
    cursor.close()
    mydb.close()
    if user:
        return True
    else:
        return False
