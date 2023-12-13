1. .venv
2. source .venv/bin/activate
3. pip install django
4. django-admin startproject student_support_system
5. cd student_support_system
6. python3 manage.py runserver
7. django-admin startapp webapp
8. setting.py

````python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'webapp', #add the name of webapp created
    # add 'crispy_forms",
]```
````

9. check
   `python3 manage.py runserver`

10. python manage.py migrate

- migrating all default files

11. python manage.py createsuperuser

- password: Djangoapp1

## Keep building on form.py

- create
- update

keep importing form into views.py

## Dashboard.html

views.py - define functions, add records, render page
urls.py - add path of each page(functionality)

## Database

models.py - create data, create table

## createRecord.html

## updateRecord.html

- goal: able to have a view, (view in detail) to update the data

1. create function in views.py first

2. add path to urls.py
   `path('filename?',views.update_record(function name in views), name='(same name as filename)')`

- add `pass` to the update file

3. go to html file and set up the page

4. Update record

- remember to add id, otherwise no argument
- record.id is the argument now, since <int>pk and id=pk

````html
<a href="{% url 'updateRecord' record.id %}" class="btn btn-info">
  Update record &nbsp; <i class="fa fa-plus" aria-hidden="true"></i> </a
>```
````

5. add logic to the links href

6. Remember to add <int>pk value after link href, otherwise it will error

7. if after logic something needs to be rendered, then go to the html file and write page
