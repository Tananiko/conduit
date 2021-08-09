from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random
import string
from conduit_data import conduit_login
from selenium.webdriver.common.keys import Keys


class TestLogoutConduit(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_navigate_to_logout(self):
        conduit_login(self.driver)
        WebDriverWait(
            self.driver, 25)

        nav_list = self.driver.find_elements_by_css_selector('a.nav-link')
        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@active-class='active']"))
        )
        nav_list[4].click()
        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_elements_located((By.XPATH, '//a[@href="#/login"]'))
        )
        nav_items = self.driver.find_elements_by_css_selector('li.nav-item')
        logged_out_site1 = nav_items[1].text
        assert logged_out_site1 == "Sign in"
        WebDriverWait(
            self.driver,50)
        logged_out_site2 = nav_items[2].text
        assert logged_out_site2 == "Sign up"
        WebDriverWait(
            self.driver, 50)


