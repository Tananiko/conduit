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
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("A9")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko9@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-9")
        self.driver.find_element_by_xpath('//button[normalize-space()="Sign up"]').click()

        WebDriverWait(
            self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='OK']"))
        )


        welcome = self.driver.find_element_by_xpath("//div[@class= 'swal-text']")
        assert welcome.text == "Your registration was successful!"
        reg_button = self.driver.find_element_by_xpath("//button[normalize-space()='OK']")
        reg_button.click()
        nav_items = self.driver.find_elements_by_css_selector('li.nav-item')
        reg_name = nav_items[3].text
        assert reg_name == "A9"

