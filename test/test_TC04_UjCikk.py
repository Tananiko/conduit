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
from selenium.webdriver.common.keys import Keys
from conduit_data import conduit_login

class TestNewBlogPost(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()
    #
    # def test_website(self):
    #     self.driver.maximize_window()
    #     time.sleep(2)
    #     assert self.driver.find_element_by_xpath('//a[@class="navbar-brand router-link-exact-active router-link-active"]'
    #                                              ).text == "conduit"
    #
    # def test_navigate_to_login(self):
    #     self.driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
    #     self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko1@gmail.com")
    #     self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-1")
    #     self.driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
    #     self.driver.find_elements_by_css_selector('li.nav-item')
    #
    #     WebDriverWait(
    #         self.driver, 50).until(
    #         EC.visibility_of_element_located((By.LINK_TEXT, "A1"))
    #     )
    def test_create_new_article(self):
        conduit_login(self.driver)
        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='#/editor']"))
        )

        self.driver.find_element_by_xpath("//a[@href='#/editor']").click()

        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]'))
        )
        title = self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
        title.send_keys("Recipe")
        about = self.driver.find_element_by_xpath('//input[contains(@placeholder,"What")]')
        about.send_keys("Spice")
        article = self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Write your")]')
        article.send_keys("Recipe, more recipe")
        tag = self.driver.find_element_by_xpath('//input[contains(@placeholder,"tags")]')
        tag.send_keys('Spice' + Keys.TAB)
        self.driver.find_element_by_xpath('//button[contains(text(),"Publish")]').click()

        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Recipe']"))
        )

        article_appearance = self.driver.find_element_by_xpath('//h1')
        assert article_appearance.text == "Recipe"