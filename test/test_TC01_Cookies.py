from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
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

    def test_accept_cookies(self):
        accept_cookies_button = self.driver.find_element_by_xpath('//div[@class="cookie__bar__buttons"]/button[2]')
        accept_cookies_button.click()
        time.sleep(3)
        accept_clicked = self.driver.get_cookie('vue-cookie-accept-decline-cookie-policy-panel')
        assert accept_clicked['value'] == 'accept'






