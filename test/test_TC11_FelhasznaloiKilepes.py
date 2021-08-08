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

    def test_navigate_to_logout(self):

        self.driver.find_element_by_xpath('//a[contains(text(),"Log out")]').click()

        WebDriverWait(
            self.driver, 50).until(
            EC.visibility_of_elements_located((By.XPATH, '//*[@id="app"]/nav/div/ul/li[5]/a')).click()
        )

        nav_items = self.driver.find_elements_by_css_selector('li.nav-item')
        logged_out_site1 = nav_items[1].text
        assert logged_out_site1 == "Sign in"
        logged_out_site2 = nav_items[-1].text
        assert logged_out_site2 == "Sign up"


