from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class Header:
    singleton = SingletonClass()

    def cart(self):
        return self.singleton.find_element(By.XPATH, "//a[@class='action showcart']")