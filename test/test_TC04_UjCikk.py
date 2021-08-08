from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
import random
import string
from selenium.webdriver.common.keys import Keys

class TestNewBlogPost(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_website(self):
        self.driver.maximize_window()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//a[@class="navbar-brand router-link-exact-active router-link-active"]'
                                                 ).text == "conduit"

    def test_navigate_to_login(self):
        self.driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko1@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-1")
        self.driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
        self.driver.find_elements_by_css_selector('li.nav-item')

        WebDriverWait(
            self.driver, 50).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "A1"))
        )
    def test_create_new_article(self):

        self.rand_string = 'Recipe'.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        self.driver.find_element_by_css_selector("[href='#/editor']").click()
        WebDriverWait(
            self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]'))
        )
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys("Recipe")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
                                          ).send.keys(self.rand_string)
        self.driver.find_element_by_xpath('//input[@placeholder="Write your article (in markdown)"]'
                                          ).send_keys(self.rand_string)
        self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').send_keys('Spice' + Keys.TAB)
        self.driver.find_element_by_xpath('//form/button').click()

        WebDriverWait(
            self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Recipe']"))
        )

        article_appearance =  self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1')
        assert article_appearance == "Recipe"
