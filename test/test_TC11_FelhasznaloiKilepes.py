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
            self.driver, 30)

        nav_list = self.driver.find_elements_by_css_selector('a.nav-link')
        WebDriverWait(
            self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@active-class="active"]'))
        )
        logout_button = self.driver.find_element_by_xpath('//a[@active-class="active"]')
        logout_button.click()
        WebDriverWait(
            self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="#/login"]'))
        )
        sign_in_button = self.driver.find_elements_by_xpath('//a[@href="#/login"]')
        assert sign_in_button.is_displayed()


