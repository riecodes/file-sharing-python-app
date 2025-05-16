# 📁 File Sharing Application

A modern, secure, and user-friendly file sharing application built with Django. Share files with ease while maintaining control over who has access to your content.

## ✨ Features

- 🔐 User Authentication & Authorization
- 📤 File Upload & Download
- 👥 File Sharing with Access Control
- 📱 Mobile Responsive Design
- 🎨 Beautiful Pink Theme UI
- 🔄 Multiple File Support
- 🔒 Secure File Management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/riecodes/pet-grooming-python.git
cd file-sharing-app
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
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

7. Access the application:
- Main app: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin

## 🏗️ Project Structure

```
file_sharing/
├── core/               # Main application
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   └── core/          # Core app templates
├── static/            # Static files (CSS, JS)
├── media/             # Uploaded files
└── manage.py          # Django management script
```

## 🔧 Technologies Used

- 🐍 Python 3.8+
- ⚡ Django 5.0
- 🎨 Bootstrap 5
- 📦 SQLite Database
- 🔒 Django Authentication
- 🎯 Crispy Forms

## 👥 User Management

### Default Admin Account
- Username: admin
- Password: admin123

### User Features
- 🔐 Secure registration and login
- 👤 User profile management
- 🔑 Password reset functionality
- 👥 User-specific file access

## 📱 Mobile Responsiveness

The application is fully responsive and works seamlessly on:
- 📱 Mobile phones
- 💻 Tablets
- 🖥️ Desktop computers

## 🔒 Security Features

- 🔐 CSRF Protection
- 🔑 Secure Password Hashing
- 👥 User Authentication
- 📁 File Access Control
- 🔒 Session Management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

[@riecodes](https://github.com/riecodes)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- All contributors and supporters 