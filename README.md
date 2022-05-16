# Bookstore - Hobby Project

an online Bookstore featuring a custom user model, search, image uploads, permissions, and a host of other goodies ready to deploy to heroku.

Dockerized Django project with postgresql

How to run locally:
$ docker-compse up -d --build

[packages]

* django: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design
* psycopg2-binary : the most popular PostgreSQL database adapter for the Python programming language.
* django-crispy-forms : an application that helps to manage Django forms. 
* django-allauth : Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
* environs : that allows you to use Twelve-factor methodology to configure your Django application with environment variables.
* pillow : Python Imaging Library to support image uploads
* django-debug-toolbar : is a configurable set of panels that display various debug information about the current request/response and when clicked
* whitenoise : simplified static file serving for Python web apps
* gunicorn : Python Web Server Gateway Interface HTTP server.
