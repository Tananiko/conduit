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

class TestFileUpload(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_upload_new_article_from_file(self):
        conduit_login(self.driver)
        first_article = self.driver.find_element_by_xpath('//h1[text()="Lorem ipsum dolor sit amet"]')
        WebDriverWait(
            self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//h1[text()="Lorem ipsum dolor sit amet"]'))
        )
        first_article.click()
        element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Write a comment...']"))
            )
        with open('data.csv', 'r', encoding="utf-8") as csvfile:
            csv_reader = (csvfile)
            for row in csv_reader:
                element.send_keys(row)
                self.driver.find_element_by_xpath('//button[text()="Post Comment"]').click()
            WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//p[normalize-space()="Tasty,"]'))
            )
            comment = self.driver.find_elements_by_class_name("card-text")
            last_comment = comment[0].text
            WebDriverWait(
                self.driver, 10)
            assert last_comment == "Tasty,"

