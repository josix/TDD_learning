from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page # home_page is a view function we will write and it will return a HTML
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve is the function Django uses internally to resolve URLs, and find what view function they should map to.
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() # create an HttpRequest object, which is what Django will see when a user’s browser asks for a page.
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertTrue(response.content.endswith(b'</html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
