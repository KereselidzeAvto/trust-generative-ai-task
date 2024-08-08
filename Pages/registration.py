from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class Registration:
    singleton = SingletonClass()

    def first_name(self):
        return self.singleton.find_element(By.ID, "firstname")

    def last_name(self):
        return self.singleton.find_element(By.ID, "lastname")

    def email(self):
        return self.singleton.find_element(By.ID, "email_address")

    def password(self):
        return self.singleton.find_element(By.ID, "password")

    def confirm_password(self):
        return self.singleton.find_element(By.ID, "password-confirmation")

    def create_account_button(self):
        return self.singleton.find_element(By.XPATH, "//button[@title='Create an Account']")
