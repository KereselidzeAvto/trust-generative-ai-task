import time

import allure

from Pages.header import Header
from Utils.logger import LogManager
from Utils.singleton import SingletonClass


class HeaderSteps:
    singleton = SingletonClass()
    elements = Header()
    logger = LogManager

    @allure.step
    def click_on_cart(self):
        try:
            time.sleep(3)
            self.elements.cart().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e
