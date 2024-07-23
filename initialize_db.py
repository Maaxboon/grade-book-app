import sqlite3

def initialize_db():
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    
    # Drop the table if it exists to avoid issues
    cursor.execute('DROP TABLE IF EXISTS students')
    
    # Create the table with the correct schema
    cursor.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            elab_score INTEGER,
            foundations_score INTEGER,
            course TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
