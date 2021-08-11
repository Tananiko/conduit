from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
import csv
from selenium.webdriver.common.keys import Keys
from conduit_data import conduit_login

class TestEditArticle(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_delete_own_article(self):
        conduit_login(self.driver)
        WebDriverWait(
            self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Recipe']"))
        )
        article = self.driver.find_element_by_xpath("//h1[normalize-space()='Recipe']")
        article.click()

        WebDriverWait(
            self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-sm btn-outline-secondary']//span[1]"))
        )
        delete_article = self.driver.find_element_by_xpath("//a[@class='btn btn-sm btn-outline-secondary']//span[1]")
        delete_article.click()

        time.sleep(5)

        assert self.driver.current_url == 'http://localhost:1667/#/'

