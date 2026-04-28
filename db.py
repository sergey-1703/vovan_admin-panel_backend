import psycopg
from psycopg import sql
from pathlib import Path
conn: psycopg.connection
cur: psycopg.cursor
HOST = "localhost"
NAME = "messenger_db"
USER = "postgres"
PASSWORD = 1234

def connect():
    global conn, cur
    try:
        conn = psycopg.connect(host=HOST,
                                   dbname=NAME,
                                   user=USER,
                                   password=PASSWORD,
                                   autocommit=True)
        cur = conn.cursor()
    except Exception as error:
        print("noooo")

def switch_to_test_env():
    global HOST, NAME, USER, PASSWORD
    HOST = "localhost"
    NAME = "postgres"
    USER = "postgres"
    PASSWORD = 1234
    connect()

#switch_to_test_env()
connect()
#this is just for me, you can just use connect() with your info like in original file :D

def set_is_banned(user_id, value):
    global conn, cur
    cur.execute("""SELECT 1 FROM users WHERE id = %s;""", (user_id,))
    if cur.fetchone() != None:
        cur.execute("""SELECT 1
                       FROM users
                       WHERE id = %s AND is_banned = %s;""", (user_id, value))
        if cur.fetchone() != None:
            return False
        query = sql.SQL("""UPDATE users
                           SET is_banned = %s
                           WHERE id = %s;""")
        cur.execute(query, (value, user_id))
        return True

    else:
        return False