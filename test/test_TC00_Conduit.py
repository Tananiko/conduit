from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
from selenium.webdriver.common.keys import Keys

class TestConduit(object):
    def setup(self):
        # self.driver = webdriver.Chrome("/Users/tarjanyibela/Downloads/chromedriver")
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)

        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_home_page_appearances(self):
        assert self.driver.find_element_by_xpath(
            '//a[@class="navbar-brand router-link-exact-active router-link-active"]').text == "conduit"

    def test_website(self):
        # self.driver.maximize_window()
        home_element = self.driver.find_elements_by_link_text('Home')
        self.driver.find_elements_by_link_text('Sign in')
        self.driver.find_elements_by_link_text('Sign up')
        self.driver.find_element_by_link_text('Global Feed')

        list = [home_element.text, 'Sign in', 'Sign up', 'Global Feed']
        for i in list:
            element = WebDriverWait(
                self.driver, 5).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, f"{i.text}"))
            )
            assert element




