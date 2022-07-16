from pages.PageBase import PageBase
from elements.HomeElements import HomeElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(PageBase):
    @property
    def input_search(self):
        """Returns the input element"""
        return self.driver.find_element(By.ID, HomeElements.input_search)
   
    @property
    def input_search_submit_btn(self):
        """Returns the input submit element"""
        return self.driver.find_element(By.XPATH, HomeElements.input_search_submit_btn)

    @property 
    def btn_close_popup(self):
        """Returns button element to close the first popup"""
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, HomeElements.btn_close_popup))
        )
        return element    