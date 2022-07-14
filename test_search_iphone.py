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
        except:
            pass

        try:
            alipage.input_search.send_keys("iphone"+Keys.RETURN)
        except WebDriverException:
            pass

        alipage.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
        alipage.btn_pagination.click()
        time.sleep(5)
        
        product = alipage.get_element_two
        alipage.go_to_custom(product)
        alipage.driver.execute_script("window.scrollTo(0, 160)")
    
        assert get_quantity_number(alipage.product_quantity_info.text) > 0 
        
        alipage.driver.close()


