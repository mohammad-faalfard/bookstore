import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
"""
model defines a Book, which has a title ,author ,price, cover
The id is a model field automatically set by Django internally to autoincrement.
slug is newspaper term for a short label for something that is often used in URLs.

UUID, Universal Unique Identifier, is a python library that helps in generating random objects of 128 bits as ids.
It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.). 
Universally unique identifiers are a good alternative to AutoField for primary_key and slug.
steps:
1) Import uuid
2) Update id field to be uuid field
3) In the URL path swap out int for uuid in the detail view . from '<int:pk> to '<uuid:pk>.
4) Applying a “plain” migration that adds a unique non-nullable field to a table with existing rows will raise an error 
because the value used to populate existing rows is generated only once, thus breaking the unique constraint.
Therefore, the following steps should be taken. In this example, we'll add a non-nullable UUIDField 
with a default value. Modify the respective field according to your needs.
https://docs.djangoproject.com/en/3.1/howto/writing-migrations/#migrations-that-add-unique-fields

*** The simplest approach, which we will use, is the most destructive: to simply delete old books migrations and start over.
$ docker-compose exec web rm -r books/migrations
$ docker-compose down
$ docker volume ls
$ docker volume rm books_postgres_data
$ docker-compose up -d
$ docker-compose exec web python manage.py makemigrations books
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser

Now go into admin and add the three books again. If you then navigate to
the main books page and click on an individual book you’ll be taken to a
new detail page with a UUID in the URL.

then add add a link to the books page in our navbar. We can use the url
template tag and the URL name of the page: book_list.
href="{% url 'book_list' %}
"""


class Book(models.Model):
    #  uuid4 is used for the encryption.
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # handle Image Upload as book cover (Media)
    # if we dont add blank=True , we will see error on migrations , 
    # some books that exist in database already doesnt have cover.
    # blank=True option will make it optional
    cover = models.ImageField(upload_to='covers/', blank=True) 
    """
    Indexing is a common technique for speeding up database performance. It
    is a separate data structure that allows faster searches and is typically only
    applied to the primary key in a model. The downside is that indexes require
    additional space on a disk so they must be used with care.
    A general rule of thumb is that if a given field is being
    used frequently, such as 10-25% of all queries, it is a prime candidate to be indexed.
    """
    class Meta:
        indexes = [  # new
            models.Index(fields=['id'], name='id_index'),
        ]
        # Custom Permission Configuration via Meta class 
        permissions = [
            ("special_status", "Can read all books"),
        ]

    # we’ve specified a __str__ method to control how the object is outputted in the Admin and Django shell.
    def __str__(self):
        return self.title

    # Define a get_absolute_url() method to tell Django how to calculate the canonical URL for an object.
    # To callers, this method should appear to return a string that can be used to refer to the object over HTTP.
    # It is also required when using the reverse() function, which is commonly used.
    # Then we can update the templates. from {% url 'book_detail' book.pk %} to {{ book.get_absolute_url }}
    # cleaner approach
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


""" 
we can create dedicated review app but lets keep things simple and update books app.
create a dedicated Review model.

"""


class Review(models.Model):
    """ The book field is the one-to-many foreign key that links Book to Review and we're
     following the standard practice of naming it the same as the linked model.
     1 book can have 1 or many authors
     For all many-to-one relationships such as a ForeignKey we must also specify an on_delete option.
     Cascade Delete option means that if a record from one table is deleted, corresponding records in the other table are also deleted.
     for example if user deleted , then review will be deleted too.

     The related_name attribute specifies the name of the reverse relation from the User model back to your model. 
     If you don't specify a related_name, Django automatically creates one using the name of your model with the suffix _set.
     Syntax: field_name = models.Field(related_name="name")
    """
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    # The review field contains the actual content which perhaps could be a TextField
    review = models.CharField(max_length=255)
    # we’ll also link to the author field to auto-populate the current user with the review.
    author = models.ForeignKey(
        # And we’re using get_user_model to reference our custom user model.
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review

