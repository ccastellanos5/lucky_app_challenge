from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from elements.AliexpressElements import AliexpressElements

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class AliexpressPage:

    def __init__(self):
        chromedriver.install()
        driver =  webdriver.Chrome()
        driver.get("http://www.aliexpress.com")
        self.driver = driver

    @property
    def input_search(self):
        return self.driver.find_element(By.ID, AliexpressElements.input_search)
   
    @property
    def input_search_submit_btn(self):
        return self.driver.find_element(By.XPATH, AliexpressElements.input_search_submit_btn)
   
    @property
    def btn_pagination(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, AliexpressElements.btn_pagination))
        )
        return element
   
    @property
    def product_quantity_info(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, AliexpressElements.product_quantity_info))
        )
        return element
   
    @property    
    def get_element_two(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, AliexpressElements.element_two))
        )
        return element.get_attribute("href")


    @property 
    def btn_close_popup(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, AliexpressElements.btn_close_popup))
        )
        return element

    def go_to_custom(self, link):
        self.driver.get(link)
       

