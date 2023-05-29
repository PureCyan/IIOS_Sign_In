from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time, random

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

def login(web, pd, acc): 
    s = Service(executable_path=r"/usr/local/bin/chromedriver")
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get(str(web))
    time.sleep(round(random.uniform(0,2),1))
    browser.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/input").send_keys(str(acc))
    browser.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/input").send_keys(str(pd))
    browser.find_element(By.XPATH, "/html/body/div/div/div[3]/button").click()
    time.sleep(round(random.uniform(0,2),1))
    return browser

