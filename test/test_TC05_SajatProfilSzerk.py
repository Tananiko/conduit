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

class TestEditProfile(object):


    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_profile_settings(self):
        conduit_login(self.driver)
        profile_picture = self.driver.find_element_by_xpath("//input[@placeholder='URL of profile picture']")
        assert profile_picture == 'https://static.productionready.io/images/smiley-cyrus.jpg'
        reg_name = self.driver.find_element_by_xpath("//input[@placeholder='Your username']")
        assert reg_name == "A1"
        bio = self.driver.find_element_by_xpath("//textarea[@placeholder='Short bio about you']")
        bio.send_keys("Updated bio about")
        updated_success = self.driver.find_element_by_xpath('//div[@class="swal-title"]')
        updated_success.text == "Update successful!"
        ok_button = self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
        ok_button.click()

