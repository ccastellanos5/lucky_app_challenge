from pages.PageBase import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from elements.SearchElements import SearchElements

class SearchPage(PageBase):
   
    @property
    def btn_pagination(self):
        """Returns the second page button element"""
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, SearchElements.btn_pagination))
        )
        return element
   
    @property    
    def get_element_two(self):
        """Returns the second search element"""
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, SearchElements.element_two))
        )
        return element.get_attribute("href")

    def go_to_custom(self, link):
        """Go to a custom page based on link"""
        self.driver.get(link)
       

