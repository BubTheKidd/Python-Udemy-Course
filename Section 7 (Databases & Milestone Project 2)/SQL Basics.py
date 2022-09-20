import sqlite3


# How you interact with SQL
connection = sqlite3.connect('') # 'data.db' is the general naming convention here
cursor = connection.cursor()
"""
- Similar to attaching a peripheral in Lua...
"""


# How you perform any operation in SQLite
cursor.execute('SQL query here')
connection.commit() # Saving result to disk
"""
- Cursors point to a place within the database, hence why it's called a cursor.
- Can have multiple cursors reading data at once (still only one that is writing though)
"""


# Example of SQLite supported data types
cursor.execute("CREATE TABLE books(name text primary key, author text, read integer)")
connection.commit()
"""
- NULL = empty or void
- Integer = whole number
- Real = floating point number
- Text = string
- Blob = binary data field(for images, documents, etc..)
- 'Primary Key' just makes it so that there can be no duplicates of the 'name' variable
"""




# Much like with files, connections to SQL need to be closed to avoid extra data usage
connection.close()

