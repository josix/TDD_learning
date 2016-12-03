from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user open his index
        self.browser.get('http://localhost:8000')
        # he found that "To-Do" show up at the title of the web
        # assert "To-Do" in browser.title
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")


        # he accept a to-do request

        # he enter "to buy wine" in the text box

        # when he hit enter, the web refresh and show the text he just entered
        # 1. to buy wine

        # At the same time, the text box still exists. And he enter another to-do item.
        # he enter "use wine for celebrating"

        # when page refresh again, he can see two item exists in his list

        # he wonder if this page will remember what the items are
        # he see only URL generated from this page, and some text explain what this url use for

        # he go to that URL, and the to-do list is still there.
if __name__ == "__main__":
    unittest.main(warnings='ignore')

