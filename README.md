User Management Application
This is a Django-based web application for managing user details, including first name, last name, phone number, email ID, and address. The application provides CRUD (Create, Read, Update, Delete) operations and includes form validation to ensure data integrity.



Features
User Interface:

Responsive and user-friendly interface built with Django Templates and Bootstrap.

Intuitive form for adding and editing user details.

Table view for displaying all users with options to edit or delete.

Confirmation dialog for user deletion.

CRUD Operations:


Create: Add a new user with form validation.

Read: View a list of all users.

Update: Modify existing user details.

Delete: Remove user records with confirmation.

Form Validation:

Ensures valid input for each field with helpful error messages.

Checks for unique email addresses to prevent duplicate entries.


Technology Stack

Backend: Django (Python)

Frontend: Django Templates, HTML, CSS (Bootstrap)

Database:  MySQL

Environment: Python 3.x, Django 4.x


Requirements

Python 3.x

Django 4.x

SQLite (default for Django, no setup needed)

Bootstrap (included via CDN in templates)


Installation
Clone the Repository:

git clone https://github.com/sneha-royal/UserManagement.git

cd UserManagement

Set up a Virtual Environment (optional but recommended):
python -m venv venv
source `venv\Scripts\activate`

Install Dependencies:

python manage.py migrate

Start the Development Server:

python manage.py runserver

Access the Application:

Open a web browser and navigate to http://127.0.0.1:8000/

Usage
1. Adding a New User
Click the "Add New User" button.
Fill in the form with the user details and click "Save".
2. Viewing All Users
The home page displays a table of all users with options to edit or delete each user.
3. Editing a User
Click the "Edit" button next to a user to modify their details.
4. Deleting a User
Click the "Delete" button next to a user. Confirm deletion on the confirmation page.

