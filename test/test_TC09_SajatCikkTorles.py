from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from conduit_data import conduit_login

class TestDeleteOwnArticle(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_delete_own_article(self):
        conduit_login(self.driver)
        WebDriverWait(
            self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Recipe']"))
        )
        article = self.driver.find_element_by_xpath("//h1[normalize-space()='Recipe']")
        article.click()
        time.sleep(5)
        delete_article = self.driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']")
        delete_article.click()

        time.sleep(5)

        WebDriverWait(
                self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Home']"))
            )
        nav_items = self.driver.find_elements_by_css_selector('li.nav-item')
        self.driver.find_elements_by_link_text('Home')
        time.sleep(2)
        home_page = nav_items[0].text
        assert home_page == "Home"

