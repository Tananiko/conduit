from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from conduit_data import conduit_login

class TestEditOwnArticle(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://conduitapp.progmasters.hu:1667/#/")

    def teardown(self):
        self.driver.quit()

    def test_edit_own_article(self):
        conduit_login(self.driver)
        WebDriverWait(
            self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Cupcakes']"))
        )
        article = self.driver.find_element_by_xpath("//h1[normalize-space()='Cupcakes']")
        article.click()
        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Write a comment...']"))
            )
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write a comment...']").send_keys("Find your taste...")

        self.driver.find_element_by_xpath('//button[text()="Post Comment"]').click()

        WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[normalize-space()="Find your taste..."]'))
            )
        comment = self.driver.find_elements_by_class_name("card-text")
        last_comment = comment[0].text
        WebDriverWait(
        self.driver, 10)
        assert last_comment == "Find your taste..."
