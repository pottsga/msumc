import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()

    def tearDown(self):
        self.driver.close()

    def test_index_page_title(self):
        driver = self.driver
        driver.get("http://localhost:6543/")
        assert "Index" in driver.title

    def test_index_page_body(self):
        driver = self.driver
        driver.get("http://localhost:6543/")
        assert "Thank you for visiting our website." in driver.page_source
