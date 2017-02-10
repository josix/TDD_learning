from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page # home_page is a view function we will write and it will return a HTML

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve is the function Django uses internally to resolve URLs, and find what view function they should map to.
        self.assertEqual(found.func, home_page)

