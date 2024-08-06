from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

import config.settings as cfgs


def browser_login(address):
    """This function opens the browser to login"""

    driver = webdriver.Edge()  # Selecting MS Edge browser
    driver.get(address)  # Entering the web address
    
    # TODO: Fill in the username from the config/credentials.json file in the browser window

    time.sleep(10)
    driver.close()