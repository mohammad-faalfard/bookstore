# Bookstore - Hobby Project

An online Bookstore featuring a custom user model, search, image uploads, permissions, and a host of other goodies ready to deploy to heroku.

Dockerized Django project with postgresql

## 📖 Installation
To start,Install Python and Docker then clone the repo to your local computer and change into the proper directory.
```
$ git clone https://github.com/cute-bunny917/bookstore.git
$ cd bookstore
```

How to run Project locally:
```
$ docker-compse up -d --build
$ docker-compse exec web python manage.py migrate
```
How to Deploy to Heroku using heroku.yml file and free tier postgresql:


```
$ touch docker-compose-prod.yml
$ heroku login
$ touch heroku.yml
$ heroku create
$ heroku stack:set container -a appname
$ heroku addons:create heroku-postgresql:hobby-dev -a appname
$ heroku git:remote -a appname
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku open -a appname
```

```

```

## 🚀 Features

- Django 3.1 & Python 3.8
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/), or [Docker](https://www.docker.com/)
- User log in/out, sign up, password reset via [django-allauth](https://github.com/pennersr/django-allauth)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v4](https://github.com/twbs/bootstrap)
- Debugging with [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
