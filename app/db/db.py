import sqlite3

from sqlite3 import Error

def init_queries() :
  conn = None
  try:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("create table file_logs (name, execution_status, last_mail_sent_time)")
  except Error as e:
      print(e) 
  finally:
      if conn:
          conn.close()

def get_conn():
  return sqlite3.connect(r"./pythonsqlite.db")

