from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from urllib3 import request

from primera_app.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_veiw(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Marina</title>', html)
        self.assertTrue(html.endswith('</html>'))
