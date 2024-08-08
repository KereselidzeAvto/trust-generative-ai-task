from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class BasePage:
    singleton = SingletonClass()

    def create_an_account(self):
        return self.singleton.find_element(By.LINK_TEXT, "Create an Account")

    def sign_in(self):
        return self.singleton.find_element(By.LINK_TEXT, " Sign In ")

    def product(self):
        return self.singleton.find_element(By.XPATH,  "//main[@id='maincontent']//li[last()]")
