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

class Datadownload(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()


    def test_profile_content_download(self):
        conduit_login(self.driver)
        time.sleep(5)

        profile_details = self.driver.find_element_by_xpath("//a[contains(text(),'Settings']")
        profile_details.click()
        time.sleep(5)

        list = ['URL of profile picture', 'Username', 'Short bio about you', 'Email']
        for i in list:
            element = WebDriverWait(
        self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, f"{i.text}")))
        assert element

        with open('../profile.csv', 'w', ) as csvfile:
            csv_writer = csv.writer(csvfile)
            next(csv_writer)
            csv_writer.write(list)

        for row in csv_writer:
            self.driver.find_element_by_xpath("//input[@placeholder='URL of profile picture']").send.keys(row[0])
            self.driver.find_element_by_xpath("//input[@placeholder='Your username']").send_keys(row[1])
            self.driver.find_element_by_xpath("//textarea[@placeholder='Short bio about you']").send_keys(row[2])
            self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(row[3])

        with open('../profile.csv', 'r', ) as csvfile:
            csv_writer = csv.writer(csvfile)
            first_row = csvfile.readline()
            assert first_row == "https://static.productionready.io/images/smiley-cyrus.jpg"
            time.sleep(5)


