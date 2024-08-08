import allure
from selenium.webdriver.common.by import By
from Pages.cart_popup import CartPopup
from Utils.logger import LogManager
from Utils.singleton import SingletonClass


class CartPopUpSteps:
    singleton = SingletonClass()
    elements = CartPopup()
    logger = LogManager

    @allure.step
    def click_on_proceed(self):
        try:
            self.singleton.find_element(By.ID, "top-cart-btn-checkout").click()
            self.logger.get_logger().info("Successfully clicked element")
        except Exception as e:
            self.logger.get_logger().error(f"Error while clicking element : {e}")
            raise e
