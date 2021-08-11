from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def conduit_login(driver):
    driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko1@gmail.com")
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-1")
    driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()

# def conduit_create_new_post(driver):
#
#     driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys("Vanilla")
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send.keys("Spices")
#     driver.find_element_by_xpath('//input[@placeholder="Write your article (in markdown)"]').send_keys('an interesting journey to Madagaskar to find the real vanilla falvor" )
#     driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').send_keys('Spice' + Keys.TAB)
#     driver.find_element_by_xpath('//form/button').click()



