import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
import csv
from selenium.webdriver.common.keys import Keys
from conduit_data import conduit_login

class TestDatadownload(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()


    def test_data_download(self):
        conduit_login(self.driver)
        time.sleep(5)


        nav_items = self.driver.find_elements_by_css_selector('li.nav-item')
        profile_setting = nav_items[2]
        profile_setting.click()
        time.sleep(5)

      with open('profile.csv', 'w', ) as csvfile:
            csv_writer = csv.writer(csvfile)
            next(csv_writer)
            csv_writer.write(list)

        for row in csv_writer:
            self.driver.find_element_by_xpath("//input[@placeholder='Your username']").send_keys(row[0])
            self.driver.find_element_by_xpath("//textarea[@placeholder='Short bio about you']").send_keys(row[1])

        with open('profile.csv', 'r', ) as csvfile:
            csv_writer = csv.writer(csvfile)
            first_row = csvfile.readline()
            assert first_row == "A1"
            time.sleep(5)

        print(list)

