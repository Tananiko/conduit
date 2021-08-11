from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
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



class TestDataListing(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_tag_list(self):
        conduit_login(self.driver)
        time.sleep(5)

        popular_tags = self.driver.find_elements_by_xpath('//div[@class="sidebar"]/div[@class="tag-list"]/a[text()="lorem"]')
        popular_tags.click()
        time.sleep(3)
        popular_tags_list= self.driver.find_element_by_xpath('//a[@class="preview-link"]/h1')
        assert len(popular_tags_list) > 0


