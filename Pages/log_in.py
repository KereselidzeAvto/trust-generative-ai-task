from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class LogIn:
    singleton = SingletonClass()

    def login_email(self):
        return self.singleton.find_element(By.ID, "email")

    def password(self):
        return self.singleton.find_element(By.ID, "pass")

    def signin_button(self):
        return self.singleton.find_element(By.XPATH, "//fieldset[@class='fieldset login']//button[@id='send2']")
