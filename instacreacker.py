from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.proxy import ProxyType,Proxy
import sys
import random

from selenium.webdriver.common.keys import Keys
url="https://www.instagram.com/"
driver=webdriver.Chrome(executable_path='C:\Windows\driver\chromedriver')
driver.get(url)
wait = WebDriverWait(driver, 10)
second_page_flag = wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, "KPnG0")))  # util login page appear
driver.find_element_by_name('username').send_keys('y.xi4')
driver.find_element_by_name('password').send_keys('Huseen#512')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[2]/form/span/button').click()
time.sleep(4)
lst='4983'
sec=str(random.randint(0,9))
for i in range(100):
    sec+=lst
    driver.find_element_by_xpath('//*[@id="security_code"]').send_keys(sec)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/form/span/button').click()

