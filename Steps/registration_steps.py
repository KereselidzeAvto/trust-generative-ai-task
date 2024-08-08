import allure

from Pages.registration import Registration
from Utils.logger import LogManager
from Utils.singleton import SingletonClass


class RegistrationSteps:
    singleton = SingletonClass()
    elements = Registration()
    logger = LogManager

    @allure.step
    def enter_first_name(self, first_name):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.first_name())
            self.elements.first_name().send_keys(first_name)
            self.logger.get_logger().info("Successfully wrote email")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering email : {e}")
            raise e

    @allure.step
    def enter_last_name(self, last_name):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.last_name())
            self.elements.last_name().send_keys(last_name)
            self.logger.get_logger().info("Successfully wrote email")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering email : {e}")
            raise e

    @allure.step
    def enter_email(self, email):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.email())
            self.elements.email().send_keys(email)
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

    @allure.step
    def enter_confirm_password(self, password):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.confirm_password())
            self.elements.confirm_password().send_keys(password)
            self.logger.get_logger().info("Successfully wrote password")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering password : {e}")
            raise e

    @allure.step
    def click_on_register(self):
        try:
            self.elements.create_account_button().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e
