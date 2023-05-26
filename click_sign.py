from selenium.webdriver.common.by import By

def sign(web, browser):
    browser.get(str(web))
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/div[3]").click()
