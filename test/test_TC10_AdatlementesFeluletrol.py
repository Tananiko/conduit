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



class Datadownload(object):
    def setup(self):
        self.driver = webdriver.Chrome("/Users/tarjanyibela/Downloads/chromedriver")
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_website(self):
        self.driver.maximize_window()
        assert self.driver.find_element_by_xpath('//a[@class="navbar-brand router-link-exact-active router-link-active"]').text == "conduit"


    def test_navigate_to_login(self):

        self.driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').click("Tananiko-1")

        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[4]/div/button")).click()
        )
        assert element
        WebDriverWait(
            self.driver, 3).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "A1"))
        )

    def test_profile_settings(self):
        profile_picture = self.driver.find_element_by_xpath("//input[@placeholder='URL of profile picture']")
        assert profile_picture == 'https://static.productionready.io/images/smiley-cyrus.jpg'
        reg_name = self.driver.find_element_by_xpath("//input[@placeholder='Your username']")
        assert reg_name == "A1"
        assert self.driver.find_element_by_xpath("//textarea[@placeholder='Short bio about you']")
        self.driver.find_element_by_xpath("//input[@placeholder='Email']")

        WebDriverWait(
            self.driver, 50).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "A1"))
        )

    def test_screenshot(self):
        capture_time = datetime.datetime.now().strftime("%Y!%m-%d_%H-%M-%S")
        self.driver.save_screenshot("Profile Settings" + capture_time + ".png")



