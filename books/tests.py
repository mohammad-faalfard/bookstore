from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from .models import Book, Review

"""
we want to test both ListView and DetailView.
We want to ensure that the Books model works as expected.

We have imported both get_user_model and TestCase before creating a
CustomUserTests class. Within it are two separate tests. 
test_create_user
confirms that a new user can be created. 
"""
"""
to test permission that is working or not 
1) The first step is to import Permission from the built-in auth models.
2) Then within our BookTests in books/tests.py add the special_status
permission to the setUp method so it is available for all our tests. 
3) We'll transfer the existing single test_book_list_view test into one for logged in
users and one for logged out users. 
4) And we'll update the detail view test to check if a user has the correct permission.
"""

class BookTests(TestCase):
    """
    First we set our user model to the variable User and then 
    create one via the manager method create_user which does 
    the actual work of creating a new user with the proper permissions.
    """

    def setUp(self):
        # We need to create a new user for our review and add a review to the setUp method in our test suite.
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )
        self.special_permission = Permission.objects.get(
            codename='special_status')
        # we add a sample book to test
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

        # create a review object that is linked to our single book object
        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='An excellent review',
        )

    # test_book_listing checks that both its string representation and content are correct.
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    # test_book_list_view to confirm that our homepage returns a 200 HTTP status code,
    # contains our body text, and uses the correct books/book_list.html template
    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    # test_book_detail_view tests that our detail page works as expected and
    # that an incorrect page returns a 404. It’s always good both to test that
    # something does exist and that something incorrect doesn’t exist in your tests.

    def test_book_detail_view_with_permissions(self):  
        self.client.login(email='reviewuser@email.com', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        # test that the book object contains the correct review.
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'books/book_detail.html')
