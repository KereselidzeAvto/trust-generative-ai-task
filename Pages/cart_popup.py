from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class CartPopup:
    singleton = SingletonClass()

    def proceed_to_checkout(self):
        return self.singleton.find_element(By.ID, "top-cart-btn-checkout")
