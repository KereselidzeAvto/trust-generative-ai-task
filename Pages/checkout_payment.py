from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class PaymentCheckout:
    singleton = SingletonClass()

    def place_order(self):
        return self.singleton.find_element(By.XPATH, "//button[@title='Place Order']")

    def thank_you(self):
        return self.singleton.find_element(By.XPATH, "//span[@class='base']")
