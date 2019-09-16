# Django App


#### Project Setup
 ```bash
# Install Python 3
python --version
python3 --version
brew doctor
brew install python3

# Install Pipenv
pip3 install pipenv

# Install Django Package
pipenv install django

# Activate the Virtual Environment (to exit run `exit`)
pipenv shell

# Create a New Django Project
mkdir <APP_NAME>
django-admin startproject <PROJECT_NAME> <APPLICATION_NAME>

# Create a New Django App in the Project
cd <APPLICATION_NAME>/<PROJECT_NAME>
python ../../application/manage.py startapp <APP_NAME>

# Add the New App to Django Settings
# Edit django/application/project/settings.py => INSTALLED_APPS = [..., '<PROJECT_NAME>.<APP_NAME>',]

# Run Django’s Local Web Server
cd ../..
python application/manage.py runserver

# NOTE:
Anytime we run a command starting by `python` for Django, the path is relative to the place `manage.py` exists.
```

#### Debug Notes:

- Error on Pipenv Commands:
    + Delete `~/.pyenv/versions/.DS_Store`


#### Resources
- https://www.djangoproject.com/
- https://djangoforbeginners.com/
- https://realpython.com/tutorials/django/
