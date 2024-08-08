import allure

from Pages.product_page import ProductPage
from Utils.logger import LogManager
from Utils.singleton import SingletonClass


class ProductSteps:
    singleton = SingletonClass()
    elements = ProductPage()
    logger = LogManager

    @allure.step
    def click_on_size(self):
        try:
            self.elements.size_option().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e

    @allure.step
    def click_on_color(self):
        try:
            self.elements.color_option().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e

    @allure.step
    def click_on_add_cart(self):
        try:
            self.elements.add_to_cart().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e
