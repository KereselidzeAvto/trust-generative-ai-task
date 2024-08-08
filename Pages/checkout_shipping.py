from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class ShippingCheckout:
    singleton = SingletonClass()

    def email_checkout(self):
        return self.singleton.find_element(By.ID, "customer-email")

    def first_name_checkout(self):
        return self.singleton.find_element(By.XPATH, "//div[@name='shippingAddress.firstname']//div[@class='control']//input")

    def last_name_checkout(self):
        return self.singleton.find_element(By.XPATH, "//div[@name='shippingAddress.lastname']//div[@class='control']//input")

    def address(self):
        return self.singleton.find_element(By.XPATH, "//div[@name='shippingAddress.street.0']//div[@class='control']//input")

    def city(self):
        return self.singleton.find_element(By.XPATH, "//div[@name='shippingAddress.city']//div[@class='control']//input")

    # def state_dropdown(self):
    #     return self.singleton.find_element(By.XPATH, "I2GIQV0")

    def zip_code(self):
        return self.singleton.find_element(By.XPATH, "//div[@name='shippingAddress.postcode']//div[@class='control']//input")

    def country(self):
        return self.singleton.find_element(By.XPATH, "//div[@name='shippingAddress.country_id']//div[@class='control']//select")

    def phone_number(self):
        return self.singleton.find_element(By.XPATH, "//div[@name='shippingAddress.telephone']//div[@class='control _with-tooltip']//input")

    def radio_button(self):
        return self.singleton.find_element(By.XPATH, "//input[@name='ko_unique_1']")

    def next_button(self):
        return self.singleton.find_element(By.XPATH, "//button[@class='button action continue primary']")

    def warning(self):
        return self.singleton.find_element(By.XPATH, "//span[@data-bind='text: errorValidationMessage()']")
