# Grade Book App: Gives an overview of the project.

## Introduction

The Grade Book App is a Python console application designed to manage student 
and course records. It utilizes Object-Oriented Programming (OOP) principles 
and integrates SQLite for database management. The application supports 
adding students, creating courses, enrolling students, calculating GPAs, 
generating marklists, and producing transcripts.

## Key Features

- **Student Management:** Add and manage student records, including email, 
  name, ELAB score, and Foundations score.
- **Course Management:** Create and manage courses, including course type 
  (BSE or BEL).
- **Enrollment:** Register students for courses, automatically associating 
  them with their chosen courses.
- **GPA Calculation:** Calculate and rank students based on their average 
  scores (ELAB and Foundations scores).
- **Transcript Generation:** Generate transcripts showing enrolled courses 
  and GPA for individual students.
- **Marklist Generation:** Generate a marklist including all students, their 
  IDs, emails, and average scores.

## Architecture

The application is structured using three primary classes:

1. **Student Class:**
   - **Attributes:**
     - `id`: Auto-generated student ID (between 112 and 128).
     - `name`: Full name of the student.
     - `email`: Student's email address.
     - `elab_score`: Score in ELAB course (≤ 100).
     - `foundations_score`: Score in Foundations course (≤ 100).
     - `course`: Enrolled course (BSE or BEL).
   - **Methods:**
     - `calculate_GPA()`: Computes the GPA based on ELAB and Foundations 
       scores.
     - `register_for_course(course)`: Updates the student's enrolled course.

2. **Course Class:**
   - **Attributes:**
     - `name`: Course name (BSE or BEL).
   - **Methods:** None (course management is handled by the database).

3. **GradeBookDatabase Class:**
   - **Attributes:**
     - `conn`: Database connection.
     - `cursor`: Database cursor.
   - **Methods:**
     - `generate_student_id()`: Generates a unique student ID between 112 and 
       128.
     - `add_student(name, email, elab_score, foundations_score, course)`: 
       Adds a new student to the database.
     - `register_student_for_course(student_id, course)`: Enrolls a student 
       in a course.
     - `calculate_GPA()`: Calculates and updates GPA for all students.
     - `calculate_ranking()`: Calculates and displays student rankings based 
       on GPA.
     - `search_by_id(student_id)`: Searches for a student by ID.
     - `generate_marklist()`: Generates a marklist of all students with their 
       IDs, emails, and average scores.
     - `generate_transcript(student_id)`: Generates a transcript for a student 
       based on their ID.
     - `close()`: Closes the database connection.

## Database Schema

The application uses an SQLite database with the following tables:

- **Students Table:**
  - Columns: `id`, `name`, `email`, `elab_score`, `foundations_score`, 
    `course`.

- **Courses Table:**
  - Columns: `id`, `name` (only course types BSE or BEL).

- **Enrollments Table:**
  - Columns: `student_id`, `course`.
  - Foreign Keys: `student_id` references `students(id)`.

## Development Environment

- **Operating System:** Linux
- **Programming Language:** Python 3
- **Database:** SQLite
- **Version Control:** Git

## Usage Instructions

1. **Clone the Repository:**

   Clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/<YourUsername>/grade-book-app.git
   cd grade-book-app

