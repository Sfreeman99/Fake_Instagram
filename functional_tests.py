from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_if_website_will_load(self):
        # Shedlia goes to the website
        self.browser.get('http://localhost:8000/instagram/feed/')
        self.assertIn('Gram', self.browser.title)


if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8