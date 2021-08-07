from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
from selenium.webdriver.common.keys import Keys

class TestLogoutConduit(object):

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


    def test_registration(self):

        self.driver.find_element_by_xpath('//a[contains(text(),"Sign up")]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("A1")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-1")
        self.driver.find_element_by_xpath('//form/button').click()

        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[4]/div/button"))
        )

    def test_navigate_to_logout(self):
        self.driver.find_element_by_xpath('//*[@class="nav-link" and contains(text(),"Log out")]')
        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/nav/div/ul/li[5]/a')).click()
        )

    def test_website(self):
            self.driver.maximize_window()
            self.driver.find_elements_by_link_text('Home')
            self.driver.find_elements_by_link_text('Sign in')
            self.driver.find_elements_by_link_text('Sign up')
