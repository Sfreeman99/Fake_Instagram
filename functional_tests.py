from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(20)

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

    def test_if_you_can_successfully_go_to_the_post_form(self):
        self.browser.get('http://localhost:8000/instagram/feed/')
        link = self.browser.find_element_by_id('post_photo')
        link.click()
        assert self.current_url == 'http://localhost:8000/instagram/post_photo'
        self.fail('Finish the test if this passes')


if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8