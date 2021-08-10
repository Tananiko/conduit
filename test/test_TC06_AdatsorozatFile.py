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


    def test_create_new_article(self):
        conduit_login(self.driver)
        WebDriverWait(
            self.driver, 25)

        self.rand_string = 'Apple'.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.driver.find_element_by_xpath('//a[@href="#/editor"]')
        WebDriverWait(
            self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@href="#/editor"]'))
        ).click()

        WebDriverWait(
            self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]'))
        )
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys("Apple")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
                                          ).send.keys(self.rand_string)
        self.driver.find_element_by_xpath('//input[@placeholder="Write your article (in markdown)"]'
                                          ).send_keys(self.rand_string)
        self.driver.find_element_by_xpath('//form/button').click()

        WebDriverWait(
            self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/h1'))
        )
        article_appearance = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1')
        assert article_appearance == "Apple"

        WebDriverWait(
            self.driver, 20)

    def test_create_comment_upload_from_file(self):

        self.driver.find_element_by_xpath("//textarea[@placeholder='Write a comment...']")
        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Write a comment...']"))
        )
        with open('data.csv', 'r', encoding="utf-8") as csvfile:
            csv_reader = (csvfile)
            next(csv_reader)
            for row in csv_reader:
                element.send_keys(row)
                self.driver.find_element_by_xpath('//button[text()="Post Comment"]').click()

        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[normalize-space()="Tasty"]'))

        )
        comment = self.driver.find_element_by_class_name("card-text")
        last_comment = comment[0].text
        WebDriverWait(
            self.driver, 10
        )
        assert last_comment == "Tasty"

    # def test_create_comment_upload_from_file(self):
    #     con_login(self.driver)
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('//h1[text()="Lorem ipsum dolor sit amet"]').click()
    #     element = WebDriverWait(
    #         self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Write a comment...']"))
    #     )
    #     with open('data.csv', 'r', encoding="utf-8") as csvfile:
    #         csv_reader = (csvfile)
    #         for row in csv_reader:
    #             element.send_keys(row)
    #             self.driver.find_element_by_xpath('//button[text()="Post Comment"]').click()
    #     WebDriverWait(
    #         self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//p[normalize-space()="Tasty,"]'))
    #     )
    #     comment = self.driver.find_elements_by_class_name("card-text")
    #     last_comment = comment[0].text
    #     time.sleep(1)
    #     assert last_comment == "Tasty,"