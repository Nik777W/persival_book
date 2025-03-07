from django.test import TestCase
from django.urls import resolve
from primera_app.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_veiw(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
