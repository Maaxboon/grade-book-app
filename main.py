#!/usr/bin/env python3

import sqlite3
import random

class Student:
    def __init__(self, name, email, elab_score, foundations_score, course):
        self.id = None
        self.name = name
        self.email = email
        self.elab_score = elab_score
        self.foundations_score = foundations_score
        self.course = course

    def calculate_avg_score(self):
        return (self.elab_score + self.foundations_score) / 2.0

class Course:
    def __init__(self, name):
        self.name = name

class GradeBookDatabase:
    def __init__(self, db_file='gradebook.db'):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                elab_score INTEGER,
                foundations_score INTEGER,
                course TEXT
            )
        ''')
        self.conn.commit()

    def generate_student_id(self):
        while True:
            student_id = random.randint(112, 128)
            self.cursor.execute('SELECT COUNT(*) FROM students WHERE id = ?', (student_id,))
            if self.cursor.fetchone()[0] == 0:
                return student_id

    def add_student(self, student):
        if not (0 <= student.elab_score <= 100) or not (0 <= student.foundations_score <= 100):
            print("Scores should be between 0 and 100.")
            return

        student.id = self.generate_student_id()
        self.cursor.execute('''
            INSERT INTO students (id, name, email, elab_score, foundations_score, course)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (student.id, student.name, student.email, student.elab_score,
              student.foundations_score, student.course))
        self.conn.commit()
        print(f"Student added with ID: {student.id}")

    def register_student_for_course(self, student_id, course_name):
        self.cursor.execute('''
            UPDATE students
            SET course = ?
            WHERE id = ?
        ''', (course_name, student_id))
        self.conn.commit()

    def calculate_ranking(self):
        self.cursor.execute('''
            SELECT id, name, email, course, (elab_score + foundations_score) / 2.0 AS avg_score
            FROM students
            ORDER BY avg_score DESC
        ''')
        return self.cursor.fetchall()

    def search_by_id(self, student_id):
        self.cursor.execute('''
            SELECT id, name, email, elab_score, foundations_score
            FROM students
            WHERE id = ?
        ''', (student_id,))
        return self.cursor.fetchone()

    def generate_marklist(self):
        self.cursor.execute('''
            SELECT id, name, email, (elab_score + foundations_score) / 2.0 AS avg_score
            FROM students
        ''')
        return self.cursor.fetchall()

    def generate_transcript(self, student_id):
        student = self.search_by_id(student_id)
        if student:
            id, name, email, elab_score, foundations_score = student
            avg_score = (elab_score + foundations_score) / 2.0
            return f"Transcript for {name} (ID: {id}):\nEmail: {email}\nAverage Score: {avg_score}"
        else:
            return "Student not found."

    def close(self):
        self.conn.close()

class GradeBook:
    def __init__(self):
        self.db = GradeBookDatabase()

    def add_student(self):
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        elab_score = int(input("Enter ELAB score (≤ 100): "))
        foundations_score = int(input("Enter Foundations score (≤ 100): "))
        course = input("Enter course (BSE or BEL): ").upper()
        student = Student(name, email, elab_score, foundations_score, course)
        self.db.add_student(student)

    def register_student_for_course(self):
        student_id = int(input("Enter student ID: "))
        course_name = input("Enter course (BSE or BEL): ").upper()
        self.db.register_student_for_course(student_id, course_name)

    def calculate_ranking(self):
        ranking = self.db.calculate_ranking()
        print("\nRanking:")
        for entry in ranking:
            print(f"ID: {entry[0]}, Name: {entry[1]}, Email: {entry[2]}, "
                  f"Course: {entry[3]}, Average Score: {entry[4]}")

    def search_by_id(self):
        student_id = int(input("Enter student ID: "))
        student = self.db.search_by_id(student_id)
        if student:
            id, name, email, elab_score, foundations_score = student
            avg_score = (elab_score + foundations_score) / 2.0
            print(f"ID: {id}\nName: {name}\nEmail: {email}\n"
                  f"ELAB Score: {elab_score}\nFoundations Score: {foundations_score}\n"
                  f"Average Score: {avg_score}")
        else:
            print("Student not found.")

    def generate_marklist(self):
        marklist = self.db.generate_marklist()
        print("\nMarklist:")
        for entry in marklist:
            print(f"ID: {entry[0]}, Name: {entry[1]}, Email: {entry[2]}, "
                  f"Average Score: {entry[3]}")

    def generate_transcript(self):
        student_id = int(input("Enter student ID: "))
        transcript = self.db.generate_transcript(student_id)
        print(transcript)

def main():
    grade_book = GradeBook()

    while True:
        print("\nChoose an action:")
        print("1. Add Student")
        print("2. Register Student for Course")
        print("3. Calculate Ranking")
        print("4. Search by ID")
        print("5. Generate Marklist")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            grade_book.add_student()

        elif choice == "2":
            grade_book.register_student_for_course()

        elif choice == "3":
            grade_book.calculate_ranking()

        elif choice == "4":
            grade_book.search_by_id()

        elif choice == "5":
            grade_book.generate_marklist()

        elif choice == "6":
            grade_book.generate_transcript()

        elif choice == "7":
            grade_book.db.close()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
