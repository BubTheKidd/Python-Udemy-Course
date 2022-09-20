# Normal way of using SQLite within a program
import sqlite3

# More efficient way of doing SQLite work
from database_connection import DatabaseConnection


# Sets up Table if one doesn't exist
def CreateBookTable():
    connection = sqlite3.connect('data.db') # Sets up connection to database
    cursor = connection.cursor() # Allows user to interact with database

    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
        # Writes to the database / What user does with the database

    connection.commit() # What saves the info to data.db
    connection.close() # Have to close the connection, same as with


def StoreBook(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    #cursor.execute(f"INSERT INTO books VALUES('{name}', '{author}', 0)")
        # Uploading the data to SQLite
        # However, due to SQL Injection Attacks, formatted strings are dangerous
        # to use here so this method is not recommended.
        # Ex: author = DROP TABLE books (if put in, will completly delete everything)

    cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (name, author))
        # As SQLi is very popular, this method of storing data is much safer.
        # -> Very similar to .format()

    connection.commit()
    connection.close()


def _RewriteFile(books):
    """
    Using SQLite, I can select any book by name and change it in place. What this
    means is that I no longer need to recreate the file everytime I change it. I 
    can update data directly. I will keep this function in here tho to show the 
    "before and after" in comparison with the last version of Book Store
    """
    pass

            
def RemoveBook(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE name=?", (name,))
    # When adding input to a database, dont forget to make it a tuple, not
    # a single value. Otherwise, SQL will count the input as a single expression.

    connection.commit()
    connection.close()


def GrabAllBooks():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    all_books = cursor.fetchall() # Returns a list of tuples
    # [(name, author, read), [name, author, read]]

    connection.close()

    return [{'name': book[0], 'author': book[1],
                     'read': book[2]} for book in all_books]


def MarkAsRead(name):
    # Easier way of managing a database
    with DatabaseConnection('data.db') as connection: # Context Manager
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))


