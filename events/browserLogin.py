from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import json

import config.settings as cfgs
import events.notify as notify

def browser_login(address):
    """This function opens the browser to login"""

    # Ignoring SSL errors as we are proceeding to a private ip 
    options = webdriver.EdgeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Edge(options=options)  # Selecting MS Edge browser

    driver.get(address) # The web address of the Captive Portal (importing from config.settings.py)

    time.sleep(cfgs.sleepTimeForBrowserToLoadContentAtStartup)  # Waiting for the page to load

    # Locate the username and password fields
    username_field = driver.find_element(By.ID, 'username')  
    password_field = driver.find_element(By.ID, 'password')  

    with open("config/Credentials.json", "r") as file:
        data = json.load(file)

    # Input the username and password
    username_field.send_keys(data['username'])
    password_field.send_keys(data['password'])

    # Locate and click the login button
    login_button = driver.find_element(By.ID, 'loginbutton')  # Replace with the correct locator
    login_button.click()

    notify.send_notification(title="Login Successfull", message="Successful login at Internet Captive Portal", timeout=1)

    time.sleep(cfgs.sleepTimeBeforeBrowserCloses)  # Time before browser closes
    driver.close()