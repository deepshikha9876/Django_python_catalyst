# Django_python_catalyst

## Overview
This application is designed to handle large CSV file uploads, user authentication, and data filtering. It includes the following pages:

1. Login
2. Upload Data
3. Query Builder
4. Users

## Features

1. Login Page:
User authentication using Django's built-in authentication system.
Secure login and logout functionalities.

2. Upload Data Page:
Allows users to upload large CSV files.
Data validation and error handling.
Efficient processing and storage of uploaded data.

2. Query Builder Page:
Enables users to create and execute custom queries on the uploaded data.
User-friendly interface for building queries.
Supports filtering, sorting, and exporting query results.

3. Users Page:
Displays a list of registered users.
Provides options to view and manage user profiles.
Administrative functionalities for user management.

## Installation
Clone the repository:

`git clone https://github.com/yourusername/django-python-catalyst.git
cd django-python-catalyst`

Set up the database:
`python manage.py migrate`

Create a superuser:
`python manage.py createsuperuser`

Run the development server:
`python manage.py runserver`

Open your browser and navigate to http://127.0.0.1:8000/ to access the application.
