from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Book

"""
LoginRequiredMixin Mixin:
First import LoginRequiredMixin at the top
then add it before ListView since mixins are loaded from left-to-right
That way the first thing that is checked is whether the user is logged in;
if they're not ,there's no need to load the ListView.
The other part is setting a login_url for the user to be redirected to.
This is the URL name for log in which, since we're using django-allauth is account_login
If we were using the traditional Django authentication system then this link would be called simply login.
If you now log out of your account and click on the “Books” link 
it will automatically redirect you to the Log In page. However if you are logged in, the Books page loads normally.
Even if you somehow knew the UUID of a specific book page you'd be redirected to Log In as well!

summary:
1) import LoginRequiredMixin
2) add LoginRequiredMixin
3) add a login_url route.
"""
"""
Basic permission : we can set them via django admin panel 
https://docs.djangoproject.com/en/3.1/topics/auth/default/#permissions-and-authorization
1) define user in admin panel
2) select permission

Custom Permissions: We can set them via the Meta class on our database models and django admin panel
https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#custom-permissions
example: let's add a special status so that an author can read all books. 
In other words they have access to the DetailView.
1) define Meta class in model
2) define user in admin panel
3) login and select new created custom permission
4) apply the custom permission using the PermissionRequiredMixin to detailview

if a user isn't already logged in it makes no sense to do the additional check of whether they have permission.
Finally add a permission_required field which specifies the desired permission.
"""


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


"""
Search functionality consists of two parts: 
1) a form to pass along a user search query 
2) a results page that performs a filter based on that query.
3) web form with get method

all we need to do is configure URL, view, and template and query filter(Q objects).
https://docs.djangoproject.com/en/3.1/topics/db/queries/#complex-lookups-with-q-objects
"""


class SearchResultsListView(ListView):
    # model used for query
    model = Book
    context_object_name = 'book_list'
    # result page based on query
    template_name = 'books/search_results.html'
    
    # for any given search do the query based on provided filter, for example based on title or author of the book
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
