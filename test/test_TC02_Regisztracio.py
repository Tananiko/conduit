from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
from selenium.webdriver.common.keys import Keys

class TestRegistrationConduit(object):

    def setup(self):
        # self.driver = webdriver.Chrome("/Users/tarjanyibela/Downloads/chromedriver")
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

        self.driver.find_element_by_xpath('/html/body//a[contains(@href,"register")]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("A1")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko1@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-1")
        self.driver.find_element_by_xpath('//button[normalize-space()='Sign up']').click()

      element = WebDriverWait(
            self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='OK']"))

        )
        assert self.driver.find_element_by_xpath("//div[@class='swal-title']").text == "Welcome!"
        self.driver.find_element_by_css_selector('.swal-button.swal-button--confirm').click()
        self.driver.find_element_by_css_selector("nav[class='navbar navbar-light'] li:nth-child(4)").text == "A1"
