import os
import subprocess
import sys

def run_command(command):
    subprocess.run(command, shell=True, check=True)

def setup_project():
    # Create virtual environment
    print("Creating virtual environment...")
    run_command("python -m venv venv")
    
    # Activate virtual environment and install requirements
    if sys.platform == "win32":
        activate_cmd = "venv\\Scripts\\activate && "
    else:
        activate_cmd = "source venv/bin/activate && "
    
    print("Installing requirements...")
    run_command(f"{activate_cmd}pip install -r requirements.txt")
    
    # Create Django project
    print("Creating Django project...")
    run_command(f"{activate_cmd}django-admin startproject file_sharing .")
    
    # Create core app
    print("Creating core application...")
    run_command(f"{activate_cmd}python manage.py startapp core")
    
    # Create necessary directories
    os.makedirs("templates", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    os.makedirs("media", exist_ok=True)
    
    print("Setup completed successfully!")
    print("\nNext steps:")
    print("1. Activate the virtual environment")
    print("2. Run migrations: python manage.py makemigrations && python manage.py migrate")
    print("3. Create superuser: python manage.py createsuperuser")
    print("4. Run the server: python manage.py runserver")

if __name__ == "__main__":
    setup_project() 