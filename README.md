# bookstore - hobby project

an online Bookstore featuring a custom user model, search, image uploads, permissions, and a host of other goodies ready to deploy to heroku.

Dockerized Django project with postgresql

How to run locally:
$ docker-compse up -d --build

[packages]

* django 
* psycopg2-binary 
* django-crispy-forms 
* django-allauth : used for user registration signup
* environs : to deploy
* pillow : image upload support
* django-debug-toolbar : to check performance 
* whitenoise : for static files
* gunicorn : as webserver gateway
