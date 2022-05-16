from django.contrib import admin
from .models import Book, Review
# we can access Models Data via admin panel by simple configuration
# we can login to admin and add a book entry to our database
"""
The admin interface has the ability to edit models on the same page as a parent model. 
Django provides two subclasses of InlineModelAdmin and they are:
    1) TabularInline
    2) StackedInline
The difference between these two is merely the template used to render them.
"""
class ReviewInline(admin.TabularInline):
    model = Review
    # we can add reviews to the book now by logged in user.
class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price",)

admin.site.register(Book, BookAdmin)

