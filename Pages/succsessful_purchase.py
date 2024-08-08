from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class LogIn:
    singleton = SingletonClass()

    def successful_purchase(self):
        return self.singleton.find_element(By.XPATH, "//span[@class='base']")
