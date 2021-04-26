import os.path
import csv 
import time 
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pywhois 


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

src_request = input('Masukkan Request : ')

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"./chromedriver.exe",chrome_options=options)

driver.get('https://www.hostinger.co.id/whois')

time.sleep(3)

elementForm = driver.find_element_by_id("whois-input").send_keys(src_request)

time.sleep(3)

elementSubmit = driver.find_element_by_css_selector("input.hb.hb--h60-xxl.hb--255.hb--h50.w-100").click()

time.sleep(10)

# exeElement = driver.find_elements_by_xpath('//div[contains(text(), "Informasi WHOIS untuk")]')
exeElement = driver.find_elements_by_css_selector("div.ng-binding")


for x in range (len(exeElement)):
    print(exeElement[x].text)

# print(exeElement[0])

# resultElement = exeElement.text
# print(exeElement)
