from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time




class TestCookies(object):
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
    #     assert self.driver.find_element_by_xpath(
    #         '//a[@class="navbar-brand router-link-exact-active router-link-active"]'
    #         ).text == "conduit"

    def test_accept_cookies(self):
        self.driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]').click()

# assert


