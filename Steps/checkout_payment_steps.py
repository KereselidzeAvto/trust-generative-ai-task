import time

import allure

from Pages.checkout_payment import PaymentCheckout
from Utils.logger import LogManager
from Utils.singleton import SingletonClass


class CheckoutPaymentSteps:
    singleton = SingletonClass()
    elements = PaymentCheckout()
    logger = LogManager

    @allure.step
    def click_on_pay(self):
        try:
            time.sleep(3)
            self.elements.place_order().click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e
