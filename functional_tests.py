from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_if_website_will_have_the_title(self):
        # Shedlia goes to the website
        self.browser.get('http://localhost:8000/instagram/feed/')
        self.assertIn('Gram', self.browser.title)

    def test_if_the_website_has_jumbotron(self):
        self.browser.get('http://localhost:8000/instagram/feed/')
        Jumbotron_text = self.browser.find_element_by_class_name(
            'jumbotron').text
        self.assertIn('Fake Instagram', Jumbotron_text, msg='No Jumbotron')
        self.assertIn('Post', Jumbotron_text, 'No post tab')
        self.fail('Add link to <a> tag in jumbotron')


if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8