
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pyotp
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
from kiteconnect import exceptions
import numpy as np


# Define your TOTP secret key and website credentials
username = 'username'
password = 'password'

# Define the URL of the trading platform you want to use
l_u = KiteConnect(api_key="apikey")
login_url=l_u.login_url()
time.sleep(5)
#login_url = 'https://kite.trade/connect/login?api_key=wdz136by8cx4qy0x&v=3'

time.sleep(1)

# Open a browser and navigate to the login page
browser = webdriver.Chrome()
browser.get(login_url)
time.sleep(5)

login_id = WebDriverWait(browser, 10).until(
        lambda x: x.find_element(by=By.XPATH, value="//input[@type='text']"))
login_id.send_keys(username)
time.sleep(5)
pwd = WebDriverWait(browser, 10).until(
        lambda x: x.find_element(by=By.XPATH, value="//input[@type='password']"))
pwd.send_keys(password)
time.sleep(5)
submit = WebDriverWait(browser, 10).until(lambda x: x.find_element(
        by=By.XPATH,
        value="//button[@type='submit']"))
submit.click()

time.sleep(5)
numb = pyotp.TOTP('your totp key')
totp_code = numb.now()
totp = WebDriverWait(browser, 10).until(lambda x: x.find_element(
        by=By.XPATH,
        value="//input[@type='number']"))

authkey = totp_code
totp.send_keys(authkey)
url = browser.current_url
print(url)
time.sleep(10)
browser.close()

#This code will give you url and this url will passed to generate token


