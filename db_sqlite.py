import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='user';")
tables = cursor.fetchall()
print(tables)
