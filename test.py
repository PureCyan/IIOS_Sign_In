from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

s = Service(executable_path=r"/usr/local/bin/chromedriver")
browser = webdriver.Chrome(service=s, options=chrome_options)

browser.get("https://www.baidu.com")
time.sleep(3)
print(browser.title)
browser.quit()