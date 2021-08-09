from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def conduit_login(driver):
    driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko1@gmail.com")
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-1")
    driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()

# def conduit_create_new_post(driver):
#     self.now = datetime.now().strftime("%Y%m%d")
#     self.rand_string = 'Recipe'.join(random.choices(string.ascii_uppercase + string.digits, k=15))
#     self.driver.find_elements_by_css_selector('li.nav-item'[1]).click()
#
#     WebDriverWait(
#         self.driver, 50).until(
#         EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]'))
#     )
#
#     self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys("Vanilla" + self.now)
#
#     WebDriverWait(
#         self.driver, 50)
#     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
#                                       ).send.keys(self.rand_string)
#     WebDriverWait(
#         self.driver, 50)
#     self.driver.find_element_by_xpath('//input[@placeholder="Write your article (in markdown)"]'
#                                       ).send_keys(self.rand_string)
#     WebDriverWait(
#         self.driver, 50)
#     self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').send_keys('Spice' + Keys.TAB)
#     WebDriverWait(
#         self.driver, 50)
#     self.driver.find_element_by_xpath('//form/button').click()
#
#     WebDriverWait(
#         driver, 50).until(
#         EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Vanilla']"))
#     )
#
#
#
#     article_appearance = self.driver.find_element_by_xpath("//h1[normalize-space()='Vanilla']")
#
#
# def waiting_element_with_webdriver_xpath(driver, ertek):
#     element = WebDriverWait(
#         driver, 50)
#     driver.find_element_by_xpath(ertek)
#     return element
#  waiting_element_with_webdriver_xpath(driver,  "//h1[normalize-space()='Vanilla']").click()