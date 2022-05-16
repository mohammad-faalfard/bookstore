# Bookstore - Hobby Project

An online Bookstore featuring a custom user model, search, image uploads, permissions, and a host of other goodies ready to deploy to heroku.

Dockerized Django project with postgresql

## 📖 Installation
To start,Install Python and Docker then clone the repo to your local computer and change into the proper directory.
```
$ git clone https://github.com/cute-bunny917/bookstore.git
$ cd bookstore
```

### How to run Project locally:
```
$ docker-compse up -d --build
$ docker-compse exec web python manage.py migrate
```

replace DJANGO_SECRET_KEY in docker-compose-prod.yml by generating new secret key
```
python -c 'import secrets; print(secrets.token_urlsafe(38))'
```
* How to Deploy to Heroku using heroku.yml file and docker-compose-prod.yml:
```
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

## docker-compose-prod.yml
```
# Production docker-compose file
# docker-compose -f docker-compose-prod.yml up -d --build

# docker-compose version
version: '3.8'

services:
  web:
    build: .
    # command: python /code/manage.py runserver 0.0.0.0:8000
    # Gunicorn : Python Web Server Gateway Interface HTTP server.
    command: gunicorn config.wsgi -b 0.0.0.0:8000 # new
    # Docker volumes allow you to persist data from containers and easily share the data between multiple containers.
    volumes:
      - .:/code
    ports:
      - 8000:8000
    # Express dependency between services
    depends_on:
      - db
    environment:
      - "DJANGO_SECRET_KEY=o7xku_XuDwD_v0B5TJIxc2qt_3t5Vq4b_BoBsQYX2C7yuC6h0kY"

  db:
    image: postgres:11
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    # For simplicity, we use POSTGRES_HOST_AUTH_METHOD=trust to allow passwordless access from your local host machine.
    # In a real production deployment, don’t use this option. Instead, configure proper root credentials using POSTGRES_PASSWORD. For more information, see the PostgreSQL documentation on “trust”.
    environment:
      - "POSTGRES_HOST_AUTH_METHOD=trust"
# The Postgres official image, however, comes with a VOLUME predefined in its image description.
# This means that when you run a PostgreSQL image as a container, it creates a volume for itself and stores data in there.
volumes:
  postgres_data:

```

## 🚀 Features

- Django 3.1 & Python 3.8
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/), or [Docker](https://www.docker.com/)
- User log in/out, sign up, password reset via [django-allauth](https://github.com/pennersr/django-allauth)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v4](https://github.com/twbs/bootstrap)
- Debugging with [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
