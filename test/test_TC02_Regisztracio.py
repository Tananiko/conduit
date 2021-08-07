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
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-1")
        self.driver.find_element_by_xpath('//form/button').click()

        # element = WebDriverWait(
        #     self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[4]/div/button"))

        )
        assert self.driver.find_element_by_css_selector(".swal-title").text == "Welcome!"
        self.driver.find_element_by_css_selector('.swal-button.swal-button--confirm').click()
        self.driver.find_elements_by_css_selector('li.nav-item')
        assert self.driver.find_element_by_xpath('/html/bodydiv[1]/nav/div/ul/li[4]/a').text == "A1"
