from selenium.webdriver.common.by import By
import time, random

def questions(web, browser):
    def gettxt(xpath, browser):
        data = browser.find_element(By.XPATH, str(xpath)).text
        return str(data)
    def insert(q, xpath, browser):
        browser.find_element(By.XPATH, str(xpath)).send_keys(str(q))
        
    browser.get(str(web))
    time.sleep(3)
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[3]").click()
    time.sleep(3)
    
    for i in range(10):
        browser.execute_script(f'document.documentElement.scrollTop={(i+1)*1000}')

    browser.find_element(By.XPATH, "/html/body/div/div/div[3]").click()
    time.sleep(3)    
    
    q_1 = gettxt("/html/body/div[3]/div/div[2]/div[1]/div[2]/span[2]", browser)
    q_2 = gettxt("/html/body/div[3]/div/div[2]/div[2]/div[2]/span[2]", browser)
    q_3 = gettxt("/html/body/div[3]/div/div[2]/div[3]/div[2]/span[2]", browser)
    q_4 = gettxt("/html/body/div[3]/div/div[2]/div[4]/div[2]/span[2]", browser)
    
    insert(q_1, "/html/body/div[3]/div/div[2]/div[1]/div[3]/textarea", browser)
    insert(q_2, "/html/body/div[3]/div/div[2]/div[2]/div[3]/textarea", browser)
    insert(q_3, "/html/body/div[3]/div/div[2]/div[3]/div[3]/textarea", browser)
    insert(q_4, "/html/body/div[3]/div/div[2]/div[4]/div[3]/textarea", browser)
    
    browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/button").click()
    time.sleep(3)