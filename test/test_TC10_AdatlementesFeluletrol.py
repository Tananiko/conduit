import time
from selenium import webdriver
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
        user_name = self.driver.find_element_by_xpath("//input[@placeholder='Your username']").text

    with open('profile.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["username"])

    with open('profile.csv', 'r') as file1:
        csv_reader = csv.reader(file1)
        next(csv_reader)
        for row in csv_reader:
            assert row[0] == user_name
    time.sleep(5)

