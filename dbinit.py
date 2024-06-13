import sqlite3

def create_connection():
    con = None
    try:
        con = sqlite3.connect('child.db')
        print("SQLite Connection created")
    except sqlite3.Error as sqliteError:
        print(sqliteError)
    return create_tables(con)        

def create_tables(con):
    try:
        cursor = con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS children(
            name TEXT,
            gender TEXT, 
            birthdate DATE,
            height FLOAT)''')
        con.commit()
    except sqlite3.Error as sqLiteError:
        print(sqLiteError)
        
create_connection()        