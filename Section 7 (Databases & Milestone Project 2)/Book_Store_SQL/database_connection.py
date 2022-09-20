import sqlite3


# Class that makes it easier to interact with SQLite
class DatabaseConnection:
    # Gets called 1st
    def __init__(self, host):
        self.connection = None
        self.host = host
        # Using the self.host property makes it so that this class can be used with other
        # SQLite databases as well


    # Gets called 2nd
    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection


    # Gets called 3rd (or last)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        # Performs the commit() as well as the close() for you, making it easier overall.
        # Although you might not always need to commit() anything, it's okay to put it here
        # because if there is nothing to commit, then nothing detrimental will occur