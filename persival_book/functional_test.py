from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """ установка """
        options = Options()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)

    def tearDown(self):
        """ демонтаж """
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Marina', self.browser.title)
        header_text = self.browser.find_element('tag_name','h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element('id', 'id_new_item')
        self.assertEqual(inputbox.get_attribute('pleaceholder'), 'Enter a to-do item')

        inputbox.send_keys('купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element('id', 'id_list_table')
        rows = table.find_element('tag_name', 'tr')
        self.assertTrue(row.text == '1: купить павлиньи перья' for row in rows)


        self.fail('"Тест остановлен на данном этапе"')




if __name__ == '__main__':
    unittest.main(warnings='ignore')