import sqlite3

def initialize_database():
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            names TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            trimester TEXT NOT NULL,
            credits INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id INTEGER,
            course_id INTEGER,
            grade REAL,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (id),
            PRIMARY KEY (student_id, course_id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
