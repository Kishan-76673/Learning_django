
- python install
- install virtual env: pip install virtualenv OR (py -m venv .venv)
- to activate it: .venv\Scripts\activate

- install django: pip install django(version: django-admin --version)
- Deactivate a virtual environment: deactivate
- install pip: py -m pip install --upgrade pip
               py -m pip --version

- django-admin startproject PROJECTNAME

- cd PROJECTNAME
- python manage.py runserver 0.0.0.0:5000(to stop server: ctrl+c).

- FILE STRUCTURE:  
(1). __init__.py(to read the folder structure),
(2). asgi.py(asyncronse gateway interface),
(3). setting.py( add the settings here),
(4). urls.py(mapping the urls) and
(5). wsgi( web server gateway interface )

#####################################

# To creating the apps in django using this cmd: ```python manage.py startapp appname```

__init__: it's dendor init file: to read the file under the folder
admin.py: dj has already a admin panel(to change in it and register the model, so we are using this file).  
apps.py: show that it's a app directory
models.py: under this app, all db are contains it.
tests.py: under this functionality, to test something 
views.py: writing here the logical part.

################


in django, all apps are reusable like if want to use this account app at somewhere there I can copy and paste there.####

####################

we can add the apps in our project folder (settings.py) add apps in internal_apps.


#### to apply log in py
import logging
logger = logging.getLogger(__name__)
logger.error("This is an error message")





##################################################################

Step 8: Execute Migrations and Setup
Now let's run everything:
```
1. Install dependencies
pip install -r requirements.txt

# 2. Create MySQL database (run in MySQL)
# mysql -u root -p
# CREATE DATABASE anthology_dashboard CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# exit;

# 3. Create migrations
python manage.py makemigrations QADashboard

# 4. Apply migrations
python manage.py migrate

# 5. Create superuser for admin access
python manage
```