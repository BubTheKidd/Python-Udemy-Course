import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE books(name text primary key, author text, read integer)")

connection.commit()
connection.close()