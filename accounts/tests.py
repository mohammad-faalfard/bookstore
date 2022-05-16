# words of Django co-founder Jacob Kaplan-Moss, “Code without tests is broken as designed.”
"""
There are two main types of tests:
1) Unit tests are small, fast, and isolated to a specific piece of functionality
2) Integration tests are large, slow, and used for testing an entire
application or a user flow like payment that covers multiple screens

To write unit tests in Django we use TestCase which is, itself, an extension of Python's TestCase.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
"""
We have imported both get_user_model and TestCase before creating a
CustomUserTests class. Within it are two separate tests. 

To run our tests within Docker:
$ docker-compose exec web python manage.py test accounts



assertEqual() in Python is a unittest library function that is used in unit testing to check the equality of
two values. This function will take three parameters as input and return a boolean value
depending upon the assert condition. If both input values are equal assertEqual()
will return true else return false.

assertFalse() in Python is a unittest library function that is used in unit testing to compare test value 
with false. This function will take two parameters as input and return a boolean value depending upon 
the assert condition. If test value is false then assertFalse() will return true else return false.

assertFalse() in Python is a unittest library function that is used in unit testing to compare test value 
with false. This function will take two parameters as input and return a boolean value depending upon 
the assert condition. If test value is false then assertFalse() will return true else return false.
"""


class CustomUserTests(TestCase):

    """
    test_create_user confirms that a new user can be created.
    First we set our user model to the variable User and then create one via the manager method create_user which 
    does the actual work of creating a new user with the proper permissions.
    """

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='mohammad',
            email='mohammad@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'mohammad')
        self.assertEqual(user.email, 'mohammad@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    """
    For test_create_superuser we follow a similar pattern but reference
    create_superuser instead of create_user. The difference between the two
    users is that a superuser should have both is_staff and is_superuser set
    to True.
    """

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)
