# register_aux.py
import sys
sys.path.append('/home/itay/my_chat_gpt/')
from app.database import connect_to_database

def register_user(username: str, password: str):
    mydb = connect_to_database()
    cursor = mydb.cursor()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    try:
        cursor.execute(sql, val)
        mydb.commit()
        return True
    except Exception as e:
        print(f"Unable to register user: {str(e)}")
        return False
    finally:
        cursor.close()
        mydb.close()

