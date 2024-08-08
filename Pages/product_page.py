from Utils.singleton import SingletonClass
from selenium.webdriver.common.by import By


class ProductPage:
    singleton = SingletonClass()

    def options_div(self):
        return self.singleton.find_element(By.XPATH, "//div[@class='swatch-opt']")

    def size_option(self):
        return self.singleton.find_element(By.XPATH,
                                           "//div[@class='swatch-attribute size']//div[@role='listbox']//div[last()]")

    def color_option(self):
        return self.singleton.find_element(By.XPATH,
                                           "//div[@class='swatch-attribute color']//div[@role='listbox']//div[last()]")

    def add_to_cart(self):
        return self.singleton.find_element(By.XPATH, "//button[@id='product-addtocart-button']")
