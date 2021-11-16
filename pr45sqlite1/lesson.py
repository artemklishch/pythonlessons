import sqlite3
from sqlite3.dbapi2 import Cursor

db = sqlite3.connect("test1_db.sqlite")
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE users (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            email TEXT NOT NULL UNIQUE
        )
''')

db.close()
