import allure

from Pages.log_in import LogIn
from Utils.logger import LogManager
from Utils.singleton import SingletonClass


class CheckoutShippingSteps:
    singleton = SingletonClass()
    elements = LogIn()
    logger = LogManager

    @allure.step
    def enter_email(self, email):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.login_email())
            self.elements.login_email().send_keys(email)
            self.logger.get_logger().info("Successfully wrote email")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering email : {e}")
            raise e

    @allure.step
    def enter_password(self, password):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.password())
            self.elements.password().send_keys(password)
            self.logger.get_logger().info("Successfully wrote password")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering password : {e}")
            raise e
