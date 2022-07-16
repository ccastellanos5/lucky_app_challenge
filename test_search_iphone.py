import pytest
import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from pages.DetailPage import DetailPage
from utils.utils import get_quantity_number, initialize_driver
from utils.logger import logger

class TestSearchIphone:
    def test_second_item_stock(self):
        """Verify if the second item on the second page has stock available"""
        driver = initialize_driver()
        
        home = HomePage(driver)
        search = SearchPage(driver)
        detail = DetailPage(driver)
        logger.info("Initialize the webdriver")

        try:
            home.btn_close_popup.click()
            logger.info("Close the initial pop up")
        except:
            pass

        try:
            home.input_search.send_keys("iphone"+Keys.RETURN)
            logger.info("Enter product to search")
        except WebDriverException:
            pass

        home.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
        search.btn_pagination.click()
        logger.info("Do scroll and click the second page")
        time.sleep(5)
        
        product = search.get_element_two
        search.go_to_custom(product)
        detail.driver.execute_script("window.scrollTo(0, 160)")
        logger.info("Extract the link from the product detail and open it in the same webdriver")
    
        logger.info("Extract the available quantity of the product and compare in order to validate the stock")
        assert get_quantity_number(detail.product_quantity_info.text) > 0 
        
        detail.driver.close()


