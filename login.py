from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

def login(web, pwd, acc): 
    browser = webdriver.Edge()
    browser.get(str(web))
    time.sleep(round(random.uniform(0,2),1))
    browser.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/input").send_keys(str(acc))
    time.sleep(round(random.uniform(0,2),1))
    browser.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/input").send_keys(str(pwd))
    time.sleep(round(random.uniform(0,2),1))
    browser.find_element(By.XPATH, "/html/body/div/div/div[3]/button").click()
    time.sleep(round(random.uniform(0,2),1))
    return browser

