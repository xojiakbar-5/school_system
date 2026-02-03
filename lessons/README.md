# School System

## About the Project
This is a School Management System built with Django. It allows teachers to create and manage lesson timetables, while students can view the schedules.
This is a School Management System built with Django. It facilitates lesson management for teachers, schedule viewing for students, and activity monitoring for directors.

## Key Features
- **User Registration:** Users can register as Teachers or Students.
- **Authentication:** Secure Login and Logout functionality.
- **User Roles:** Supports Student, Teacher, and Director roles.
- **Authentication:** Secure Login and Logout with protection against re-login attempts while active.
- **Timetable:** View lesson schedules organized by day and time.
- **Teacher Controls:** Teachers can add, edit, and delete their own lessons.
- **Permissions:** Only the teacher who created a lesson can modify or delete it.
- **Action History:** Directors can view a history log of all changes made by teachers.
- **Permissions:** Strict role-based permissions for editing and viewing data.

## Technologies Used
- Python
- Django
- HTML/CSS

## Installation and Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python manage.py runserver`
3. Apply migrations: `python manage.py migrate`
4. Run the server: `python manage.py runserver`