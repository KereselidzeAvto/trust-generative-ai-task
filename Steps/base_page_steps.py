import allure

from Pages.base_page import BasePage
from Utils.logger import LogManager
from Utils.singleton import SingletonClass


class BaseSteps:
    singleton = SingletonClass()
    elements = BasePage()
    logger = LogManager

    @allure.step
    def open_base_page(self):
        self.singleton.navigate_to("https://magento.softwaretestingboard.com/")

    @allure.step
    def click_on_create_on_account(self):
        try:
            self.elements.create_an_account().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e

    @allure.step
    def click_sign_in(self):
        try:
            self.elements.sign_in().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e

    @allure.step
    def click_product(self):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);", self.elements.product())
            self.elements.product().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e
