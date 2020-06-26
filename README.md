# Django rest framework with docker and postgreSQL token authorization


# !!! postgres not working !!!
#     conn = _connect(dsn, connection_factory=connection_factory, **kwasync) django.db.utils.OperationalError: could not translate host name "db" to address: nodename nor servname provided, or not known
> terminal command
- work in repo
**folder/file**

## setup
> $ mkdir drf-api-deploy

Use poetry to initialize folder 

> $ cd `drf-api-deploy` 
> $ poetry init -n 
> $ poetry add django djangorestframework 
> $ poetry add --dev black 
> $ poetry shell 

> $ django-admin startproject garden_project .
> $ python manage.py startapp flowers

> $ django-environ 

static/
