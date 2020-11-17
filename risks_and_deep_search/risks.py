#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
import subprocess
import time
import os
from bs4 import BeautifulSoup
import sys
from clint.textui import colored
import optparse
import undetected_chromedriver as uc
name=""
def r_level(phone_number):
	
	global name
	options = webdriver.ChromeOptions()
	#options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('disable-infobars')
	options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
	options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36")
	loc=os.getcwd()
	driver = uc.Chrome(options=options)
	driver.get("https://spamcalls.net/en")
	
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "q"))).send_keys(phone_number)

	#/html/body/div[3]/div/div/div/div[1]/form/button
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/form/button'))).click()
	name=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'typ'))).text

	if "Other" in name or "other" in name:
		name="Spam Potensial: High Risk/SPAM"
	print(colored.blue(name))

    
