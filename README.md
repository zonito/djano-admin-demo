djano-admin-demo
================

Django Admin Demo + Bootstrap

### Step 1: create database in mysql
```
CREATE DATABASE djangodemo;
```

### Step 2: Sync DB and configure
```
python manage.py syncdb
```

### Step 3: Install [django-admin-bootstrap](https://github.com/django-admin-bootstrapped/django-admin-bootstrapped)
```
pip install django-admin-bootstrapped
```
Copy django-admin-bootstrapped folder to root.

### Step 4: Runserver
```
python manage.py runserver
```

Now, open [localhost:8000](http://localhost:8000/)
- A form with manual entry.

Open admin [localhost:8000/admin](http://localhost:8000/admin)
- Administration module.
