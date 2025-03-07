from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

# options = Options()
# options.add_argument("--headless")

# brauser = webdriver.Chrome(options=options)
# brauser.get('http://localhost:8000')
# assert 'To-Do' in brauser.title, '' + brauser.title
# print(brauser.title)


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.brauser = webdriver.Chrome(options=options)

    def tearDown(self):
        self.brauser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.brauser.get('http://localhost:8000')
        self.assertIn('To-Do', self.brauser.title)
        self.fail('"Тест остановлен на данном этапе"')


if __name__ == '__main__':
    unittest.main(warnings='ignore')