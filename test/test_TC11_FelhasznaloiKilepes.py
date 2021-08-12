from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from conduit_data import conduit_login


class TestLogoutConduit(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_logout(self):
        conduit_login(self.driver)
        time.sleep(5)

        nav_list = self.driver.find_elements_by_css_selector('a.nav-link')
        WebDriverWait(
            self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@active-class="active"]'))
        )
        logout_button = self.driver.find_element_by_xpath('//a[@active-class="active"]')
        logout_button.click()
        WebDriverWait(
            self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="#/login"]'))
        )
        self.driver.find_elements_by_link_text('Home')
        self.driver.find_elements_by_link_text('Sign in')
        self.driver.find_elements_by_link_text('Sign up')
        self.driver.find_element_by_link_text('Global Feed')

        nav_items = self.driver.find_elements_by_css_selector('li.nav-item')
        logged_out_site1 = nav_items[1].text
        assert logged_out_site1 == "Sign in"
        time.sleep(3)

        logged_out_site2 = nav_items[2].text
        assert logged_out_site2 == "Sign up"
        time.sleep(3)

