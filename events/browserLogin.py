from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import json

import config.settings as cfgs


def browser_login(address):
    """This function opens the browser to login"""

    options = webdriver.EdgeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')



    driver = webdriver.Edge(options=options)  # Selecting MS Edge browser

    driver.get(address)  # Entering the web address
    time.sleep(cfgs.sleepTimeForBrowserToLoadContentAtStartup)  # Waiting for the page to load


    # Locate the username and password fields
    username_field = driver.find_element(By.ID, 'username')  # Replace with the correct locator
    password_field = driver.find_element(By.ID, 'password')  # Replace with the correct locator

    with open("config/Credentials.json", "r") as file:
        data = json.load(file)

    # Input the username and password
    username_field.send_keys(data['username'])
    password_field.send_keys(data['password'])

    # Locate and click the login button
    login_button = driver.find_element(By.ID, 'loginbutton')  # Replace with the correct locator
    login_button.click()

    time.sleep(cfgs.sleepTimeBeforeBrowserCloses)  # Time before browser closes
    driver.close()