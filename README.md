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

# Create `requirements.txt` File
_Create a `requirements.txt` file and list all the dependencies you want to install_
django-jinja==2.4.1
Django==2.2.5
Jinja2==2.10.1

# Install Dependency Packages
pipenv install -r requirements.txt

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



#### Connect Django MTV (Model, Template, View) Together
1. Import Models in `views.py`
2. Query for data in `views.py`
3. Pass the data from `view.py` to template
4. Update the template to show/use the received data
5. Map a URL to the view


#### Notes:

- Error on Pipenv Commands:
    + Delete `~/.pyenv/versions/.DS_Store`

- DB Migration
    + https://realpython.com/django-migrations-a-primer/
  ```
  python application/manage.py makemigrations
  python application/manage.py migrate
  ```
    
- Flush the DB Records:
  ```
  python application/manage.py flush
  python application/manage.py createsuperuser
  ```

- Django Structure Issues:
    + https://wsvincent.com/django-tips-template-structure/

- Django Best Practices:
    + https://www.toptal.com/django/django-top-10-mistakes

- Django Database Setup with PostgreSQL:
    + Install [PostgreSQL](https://pypi.org/project/postgres/)
    + Install [psycopg2](https://pypi.org/project/psycopg2/)
    + Guide https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/


#### Resources
- https://www.djangoproject.com/
- https://legacy.gitbook.com/@djangogirls
- https://djangoforbeginners.com/
- https://realpython.com/tutorials/django/
- https://docs.pipenv.org/en/latest/basics/
- https://niwinz.github.io/django-jinja/latest/
- https://medium.com/@djstein/modern-django-part-1-project-refactor-and-meeting-the-django-settings-api-d2784efb606f




#### Project Structure:
```
PROJECT_NAME/
    PROJECT/
        __init__.py
        settings.py
        url.py
        wsgi.py
    manage.py
```


