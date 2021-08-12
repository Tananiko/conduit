
def conduit_login(driver):
    driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Aniko1@gmail.com")
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tananiko-1")
    driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()

