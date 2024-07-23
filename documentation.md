# Grade Book Application Documentation

## Introduction

The Grade Book App is a Python console application designed to manage student and course records. It utilizes Object-Oriented Programming (OOP) principles and integrates SQLite for database management. The application supports adding students, creating courses, enrolling students, calculating GPAs, and generating transcripts.

## Key Features

- **Student Management:** Add and manage student records, including email and name.
- **Course Management:** Create and manage course records, including name, trimester, and credits.
- **Enrollment:** Register students for courses and store their grades.
- **GPA Calculation:** Calculate and rank students based on their GPAs.
- **Transcript Generation:** Generate student transcripts showing enrolled courses and GPA.

## Architecture

The application is structured using three primary classes:

1. **Student Class:**
   - **Attributes:** `email`, `names`, `courses_registered`, `GPA`.
   - **Methods:**
     - `calculate_GPA()`: Computes the GPA based on enrolled courses and grades.
     - `register_for_course(course)`: Adds a course to the student's registered courses.

2. **Course Class:**
   - **Attributes:** `name`, `trimester`, `credits`.
   - **Methods:** None (course management is handled by the database).

3. **GradeBookDatabase Class:**
   - **Attributes:** `conn` (database connection), `cursor` (database cursor).
   - **Methods:**
     - `add_student(email, names)`: Inserts a new student into the database.
     - `add_course(name, trimester, credits)`: Inserts a new course into the database.
     - `register_student_for_course(student_email, course_name)`: Enrolls a student in a course.
     - `calculate_GPA(student_email)`: Calculates a student's GPA (to be implemented).
     - `close()`: Closes the database connection.

## Database Schema

The application uses an SQLite database with the following tables:

- **Students Table:**
  - Columns: `id`, `email`, `names`.

- **Courses Table:**
  - Columns: `id`, `name`, `trimester`, `credits`.

- **Enrollments Table:**
  - Columns: `student_id`, `course_id`, `grade`.
  - Foreign Keys: `student_id` references `students(id)`, `course_id` references `courses(id)`.

## Development Environment

- **Operating System:** Linux
- **Programming Language:** Python 3
- **Database:** SQLite
- **Version Control:** Git

## Usage Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/<Maaxboon>/grade-book-app_<your_name>.git
   cd grade-book-app_<maxwel_okoth>
