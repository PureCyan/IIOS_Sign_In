from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver', options=chrome_options)

browser.get("www.baidu.com")
time.sleep(3)
print(browser.title)
browser.quit()