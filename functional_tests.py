from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent

    def apply_style(s):
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    sleep(.3)
    apply_style(original_style)


class NewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_if_website_will_have_the_title(self):
        # Shedlia goes to the website
        self.browser.get('http://localhost:8000/')
        self.assertIn('Gram', self.browser.title)

    def test_if_the_website_has_jumbotron(self):
        self.browser.get('http://localhost:8000/')
        Jumbotron_text = self.browser.find_element_by_class_name(
            'jumbotron').text
        self.assertIn('Fake Instagram', Jumbotron_text, msg='No Jumbotron')
        self.assertIn('Post', Jumbotron_text, 'No post tab')

    def test_if_you_can_successfully_go_to_the_post_form(self):
        self.browser.get('http://localhost:8000/')
        link = self.browser.find_element_by_id('post_photo')
        highlight(link)
        sleep(2)
        link.click()
        sleep(10)
        self.assertEqual(self.browser.current_url,
                         'http://localhost:8000/post_photo/',
                         'They do not equal each other')
        form_present = self.browser.find_element_by_tag_name('form')
        assert form_present

    def test_that_the_post_photo_form_has_all_fields(self):
        self.browser.get('http://localhost:8000/post_photo/')
        form = self.browser.find_element_by_tag_name('form')
        highlight(form)
        sleep(1)
        name = self.browser.find_element_by_name('name')
        highlight(name)
        sleep(1)
        image = self.browser.find_element_by_name('image')
        highlight(image)
        sleep(1)
        self.assertIn(name.text, form.text)
        self.assertIn(image.text, form.text)


if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8