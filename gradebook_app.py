import sqlite3

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        # Implement GPA calculation logic
        pass

    def register_for_course(self, course):
        self.courses_registered.append(course)


class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBookDatabase:
    def __init__(self, db_file='gradebook.db'):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_student(self, email, names):
        try:
            self.cursor.execute('INSERT INTO students (email, names) VALUES (?, ?)', (email, names))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error adding student: {e}")

    def add_course(self, name, trimester, credits):
        self.cursor.execute('INSERT INTO courses (name, trimester, credits) VALUES (?, ?, ?)', (name, trimester, credits))
        self.conn.commit()

    def register_student_for_course(self, student_email, course_name):
        self.cursor.execute('SELECT id FROM students WHERE email = ?', (student_email,))
        student_id = self.cursor.fetchone()

        self.cursor.execute('SELECT id FROM courses WHERE name = ?', (course_name,))
        course_id = self.cursor.fetchone()

        if student_id and course_id:
            self.cursor.execute('INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)', (student_id[0], course_id[0]))
            self.conn.commit()

    def calculate_GPA(self, student_email):
        # Implement GPA calculation logic here
        pass

    def close(self):
        self.conn.close()


def main():
    db = GradeBookDatabase()

    while True:
        print("Choose an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            db.add_student(email, names)

        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            db.add_course(name, trimester, credits)

        elif choice == "3":
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            db.register_student_for_course(student_email, course_name)

        elif choice == "4":
            # Implement GPA calculation and ranking
            pass

        elif choice == "5":
            # Implement grade search
            pass

        elif choice == "6":
            # Implement transcript generation
            pass

        elif choice == "7":
            db.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
