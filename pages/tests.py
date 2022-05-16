from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

"""
For our homepage we can use Django's SimpleTestCase
which is a special subset of Django's TestCase that is designed for
webpages that do not have a model included.

At the top we import SimpleTestCase as well as reverse which is useful for
testing our URLs. Then we create a class called HomepageTests that
extends SimpleTestCase and within it add a method for each unit test.
"""


class HomepageTests(SimpleTestCase):

    # When a setUp() method is defined, the test runner will run that method prior to each test. setUp() executed before each test !
    def setUp(self):
        # calling the URL name of home via the reverse method.
        # if we change the actual route of this page in the future, we can still refer to it by the same home URL name.
        url = reverse('home')
        self.response = self.client.get(url)

    # check that the HTTP status code for the homepage equals 200 which means that it exists.
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # Asserts that the template with the given name was used in rendering the response.
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    # Asserts that a response produced the given status_code and that text appears in its content. 
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    # Asserts that a response produced the given status_code and that text does not appear in its content
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    """ 
    We will need to import both resolve as well as the HomePageView at the top of the file.
    this test checks that the name of the view used to resolve / matches HomePageView
    """
    def test_homepage_url_resolves_homepageview(self): 
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):  

    # When a setUp() method is defined, the test runner will run that method prior to each test. setUp() executed before each test !
    def setUp(self):
        # calling the URL name of about via the reverse method.
        # if we change the actual route of this page in the future, we can still refer to it by the same home URL name.
        url = reverse('about')
        self.response = self.client.get(url)

    # check that the HTTP status code for the homepage equals 200 which means that it exists.
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # Asserts that the template with the given name was used in rendering the response.
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
        
    # Asserts that a response produced the given status_code and that text appears in its content. 
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    # Asserts that a response produced the given status_code and that text does not appear in its content
    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    """ 
    We will need to import both resolve as well as the AboutPageView at the top of the file.
    this checks that the name of the view used to resolve / matches AboutPageView
    """
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
