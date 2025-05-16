# File Sharing Application

A Django-based file sharing application with user authentication and access control.

## Features

- User Registration and Login
- File Upload and Download
- File Sharing with Access Control
- Mobile Responsive Design
- Pink Theme UI

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at http://127.0.0.1:8000

## Project Structure

- `file_sharing/` - Main project directory
  - `core/` - Core application
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JS, images)
  - `media/` - Uploaded files 