from pages.PageBase import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from elements.DetailElements import DetailElements

class DetailPage(PageBase):
    @property
    def product_quantity_info(self):
        """Returns the quantity info element"""
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, DetailElements.product_quantity_info))
        )
        return element
