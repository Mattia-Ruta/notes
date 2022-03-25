# Python3 Installation and Setup

Make sure you have python and pip installed before you start
Download Python from web \
`apt install python3 python3-pip`

Once you have py installed, install django using pip \
`sudo apt install python3-django`

# Virual Environment
With everything installed you want to create a virtual environment

Install virtual environment \
`sudo pip install virtualenv`

`sudo apt install python3.8-venv`

Create new virtualenv \
`virtualenv venv`

Activate venv \
`source /path/to/venv/bin/activate`


exit virtualenv \
`deactivate`

## Environment Files
Create .env file for settings

```
DEBUG=False
DB_HOST=localhost
DB_USERNAME=username
```

## Python Environ
Install environ integration with Django

`pip install django-environ`

Once installed, import environment

(In settings.py)

```python
import environ

#Sets .env function for env('value')
env = environ.Env(
    # Set any Default Values
    DEBUG=(bool, False)
)

#Connects the .env file with the function
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

#Pull vars from .env
DEBUG = env('DEBUG')

```

# Mariadb Setup

Make sure you have the python package pymysql \
`pip3 install pymysql`

Inside your project/project/__init__.py (Same dir as settings.py) \

```python
import pymysql

pymysql.install_as_MySQLdb()
```

# Django Setup
## New Project
Once you have django-admin installed, you can start creating Django projects

*Make sure you're in your virtualenv* \
`django-admin startproject website` \
This creates the project directory


In settings.py, make sure to add the IPs allowed to access the project, normally the server's IP

```python
ALLOWED_HOSTS = [
    '123.123.123.123',
    'domain.co.uk',
]
```

## New App
cd into your main project dir where manage.py is \
`python3 manage.py startapp newapp`

Remember to add the app to your project's settings.py file

```python
INSTALLED_APPS = [
    '...',
    'newapp',
]
```