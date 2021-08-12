import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
from conduit_data import conduit_login

class TestUploadNewCommentFromFile(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_upload_new_comment_from_file(self):
        conduit_login(self.driver)
        time.sleep(5)
        first_article = self.driver.find_element_by_xpath("//h1[normalize-space()='Alma']")
        first_article.click()
        element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Write a comment...']"))
            )
        post_comment_button = self.driver.find_element_by_xpath('//button[text()="Post Comment"]')
        with open('data.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                element.click()
                element.send_keys(row[0])
                self.driver.find_element_by_xpath("//textarea[@placeholder='Write a comment...']")
                self.driver.find_element_by_xpath("//html").click
                post_comment_button.click()
                time.sleep(5)

        comment = self.driver.find_elements_by_class_name("card-text")
        last_comment = comment[0].text
        time.sleep(2)
        assert last_comment == "apple"

