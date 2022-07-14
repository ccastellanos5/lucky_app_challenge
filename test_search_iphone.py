import pytest
from pages.AliexpressPage import AliexpressPage
from utils.logger import logger

class TestSearchIphone:
    def test_second_item_stock(self):
        alipage = AliexpressPage()
        logger.info("Initialize the webdriver")

        alipage.btn_close_popup.click()

