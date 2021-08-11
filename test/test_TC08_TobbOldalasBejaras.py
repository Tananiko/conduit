from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from conduit_data import conduit_login

class TestPaginationConduit(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_pagination(self):
        conduit_login(self.driver)
        time.sleep(3)

        pagination = self.driver.find_element_by_class_name("page-link")
        WebDriverWait(
            self.driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "page-link"))
        )
        max_pagination = len(pagination)
        for page in pagination:
            if page.text < max_pagination:
                    page.click()
            else:
                   assert page.text == max_pagination

