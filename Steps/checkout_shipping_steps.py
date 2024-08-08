import time

import allure
from selenium.webdriver.support.ui import Select

from Pages.checkout_shipping import ShippingCheckout
from Utils.fake_data import FakeData
from Utils.logger import LogManager
from Utils.singleton import SingletonClass


class CheckoutShippingSteps:
    singleton = SingletonClass()
    elements = ShippingCheckout()
    logger = LogManager
    data = FakeData()

    @allure.step
    def enter_email(self, email):
        try:
            time.sleep(3)
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.email_checkout())
            self.elements.email_checkout().send_keys(email)
            self.logger.get_logger().info("Successfully wrote email")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering email : {e}")
            raise e

    @allure.step
    def enter_first_name(self, first_name):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.first_name_checkout())
            self.elements.first_name_checkout().send_keys(first_name)
            self.logger.get_logger().info("Successfully wrote first name")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering first name : {e}")
            raise e

    @allure.step
    def enter_last_name(self, last_name):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.last_name_checkout())
            self.elements.last_name_checkout().send_keys(last_name)
            self.logger.get_logger().info("Successfully wrote last name")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering last name : {e}")
            raise e

    @allure.step
    def enter_address(self, address):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.address())
            self.elements.address().send_keys(address)
            self.logger.get_logger().info("Successfully wrote address")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering address : {e}")
            raise e

    @allure.step
    def enter_city(self, city):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.city())
            self.elements.city().send_keys(city)
            self.logger.get_logger().info("Successfully wrote city")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering city : {e}")
            raise e

    @allure.step
    def enter_zip_code(self, zip_code):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.zip_code())
            self.elements.zip_code().send_keys(zip_code)
            self.logger.get_logger().info("Successfully wrote zip code")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering zip code : {e}")
            raise e

    @allure.step
    def choose_country(self):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.country())
            Select(self.elements.country()).select_by_index(1)
            self.logger.get_logger().info("Successfully selected country")
        except Exception as e:
            self.logger.get_logger().error(f"Error while selecting country : {e}")
            raise e

    @allure.step
    def enter_phone_number(self, phone_number):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);",
                                                     self.elements.phone_number())
            self.elements.phone_number().send_keys(phone_number)
            self.logger.get_logger().info("Successfully wrote phone number")
        except Exception as e:
            self.logger.get_logger().error(f"Error while entering zip phone number : {e}")
            raise e

    @allure.step
    def click_on_radio_button(self):
        try:
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);", self.elements.radio_button())
            self.elements.radio_button().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e

    @allure.step
    def click_on_place_order(self):
        try:
            time.sleep(3)
            self.singleton.get_driver.execute_script("arguments[0].scrollIntoView(true);", self.elements.next_button())
            self.elements.next_button().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e
