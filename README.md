# ToDo-App-Django
ToDo App using Django Models and Templates

setup the project
1. django-admin startproject todoapp
2. cd todoapp
3. python manage.py migrate                 # apply migration
4. python manage.py createsuperuser         # create user
5. goto admin area by appending url with '/admin' and use superuser credentials
6. python manage.py startapp tasks          # create app
7. add in installed app in settings.py
8. add in urls                             # from django.urls import include
9. add urls.py file in tasks
10. add templates
11. go to models.py and create models like tasks model
12. go to admin.py and register the model
13. python manage.py makemigrations                      # run make migration and then step 3
14. do step 5 and see models are there or not.
