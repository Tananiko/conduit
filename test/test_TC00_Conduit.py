from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestConduit(object):
    def setup(self):
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

        self.driver.find_elements_by_link_text('Home')
        self.driver.find_elements_by_link_text('Sign in')
        self.driver.find_elements_by_link_text('Sign up')
        self.driver.find_element_by_link_text('Global Feed')

        nav_items = self.driver.find_elements_by_css_selector('li.nav-item')
        logged_out_site1 = nav_items[1].text
        assert logged_out_site1 == "Sign in"
        time.sleep(3)

        logged_out_site2 = nav_items[2].text
        assert logged_out_site2 == "Sign up"
        time.sleep(3)






