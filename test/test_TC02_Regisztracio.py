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
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("A5")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko5@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-5")
        self.driver.find_element_by_xpath('//button[normalize-space()="Sign up"]').click()

        WebDriverWait(
            self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='OK']"))
        )


        welcome = self.driver.find_element_by_xpath("//div[@class= 'swal-text']")
        assert welcome.text == "Your registration was successful!"
        self.driver.find_element(By.CSS_SELECTOR('.swal-button.swal-button--confirm')).click()
        self.driver.find_elements(By.CSS_SELECTOR('li.nav-item'))

        # WebDriverWait(
        #    self.driver, 50).until(
        #     EC.visibility_of_element_located((By.LINK_TEXT, "A5"))
        # )
