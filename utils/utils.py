import chromedriver_autoinstaller as chromedriver
from selenium import webdriver

def get_quantity_number(txt):
    return [int(s) for s in txt.split() if s.isdigit()][0]

def initialize_driver():
    chromedriver.install()
    driver =  webdriver.Chrome()
    driver.get("http://www.aliexpress.com")
    return driver
