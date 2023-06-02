from selenium.webdriver.common.by import By
import time

def sign(web, browser):
    browser.get(str(web))
    time.sleep(5)
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/div[3]").click()
    time.sleep(3)
