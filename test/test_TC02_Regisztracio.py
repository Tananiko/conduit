from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
import string


class TestRegistrationConduit(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_registration(self):

        username = 'A'.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email = f'{username}@gmail.com'
        self.driver.find_element_by_xpath('/html/body//a[contains(@href,"register")]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys('A111')
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('Tananiko-11')
        self.driver.find_element_by_xpath('//button[normalize-space()="Sign up"]').click()

        WebDriverWait(
            self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='OK']"))
        )

        welcome = self.driver.find_element_by_xpath("//div[@class= 'swal-text']")
        assert welcome.text == "Your registration was successful!"

        WebDriverWait(
            self.driver, 25)
        reg_button = self.driver.find_element_by_xpath("//button[normalize-space()='OK']")
        reg_button.click()

        WebDriverWait(
            self.driver, 25)
        nav_items = self.driver.find_elements_by_css_selector('li.nav-item')
        reg_name = nav_items[3].text
        assert reg_name == "A111"

