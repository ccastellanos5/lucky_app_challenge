import pytest
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from pages.AliexpressPage import AliexpressPage
from utils.utils import get_quantity_number
from utils.logger import logger

class TestSearchIphone:
    def test_second_item_stock(self):
        alipage = AliexpressPage()
        logger.info("Initialize the webdriver")

        try:
            alipage.btn_close_popup.click()
            logger.info("Close the initial pop up")
        except:
            pass

        try:
            alipage.input_search.send_keys("iphone"+Keys.RETURN)
            logger.info("Enter product to search")
        except WebDriverException:
            pass

        alipage.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
        alipage.btn_pagination.click()
        logger.info("Do scroll and click the second page")
        time.sleep(5)
        
        product = alipage.get_element_two
        alipage.go_to_custom(product)
        alipage.driver.execute_script("window.scrollTo(0, 160)")
        logger.info("Extract the link from the product detail and open it in the same webdriver")
    
        logger.info("Extract the available quantity of the product and compare in order to validate the stock")
        assert get_quantity_number(alipage.product_quantity_info.text) > 0 
        
        alipage.driver.close()


