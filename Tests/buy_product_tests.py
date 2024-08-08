import os
import sys

import allure

from Pages.product_page import ProductPage
from Pages.checkout_payment import PaymentCheckout
from Pages.checkout_shipping import ShippingCheckout

from Steps.base_page_steps import BaseSteps
from Steps.product_page_steps import ProductSteps
from Steps.header_steps import HeaderSteps
from Steps.cart_popup_steps import CartPopUpSteps
from Steps.checkout_shipping_steps import CheckoutShippingSteps
from Steps.checkout_payment_steps import CheckoutPaymentSteps

from Utils.fake_data import FakeData
from Utils.singleton import SingletonClass

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestBuy:
    product_page = ProductPage()
    payment_page = PaymentCheckout()
    checkout_shipping_page = ShippingCheckout()

    singleton = SingletonClass()
    base_steps = BaseSteps()
    product_steps = ProductSteps()
    header_steps = HeaderSteps()
    cart_popup_steps = CartPopUpSteps()
    checkout_shipping_steps = CheckoutShippingSteps()
    checkout_payment_steps = CheckoutPaymentSteps()

    data = FakeData()
    first_name = data.generate_first_name()
    last_name = data.generate_last_name()
    address = data.generate_address()
    email = data.generate_email()
    password = data.generate_password()
    city = data.generate_city()
    zip_code = data.generate_zip_code()
    phone_number = data.generate_phone_number()

    @allure.suite("Buying Products")
    @allure.title("Buying product Positive")
    @allure.description("full flow of user purchasing product successfully")
    def test_register_positive(self):
        self.base_steps.open_base_page()
        self.base_steps.click_product()
        self.product_steps.click_on_add_cart()
        self.header_steps.click_on_cart()
        self.cart_popup_steps.click_on_proceed()
        self.checkout_shipping_steps.enter_email(self.email)
        self.checkout_shipping_steps.enter_first_name(self.first_name)
        self.checkout_shipping_steps.enter_last_name(self.last_name)
        self.checkout_shipping_steps.enter_address(self.address)
        self.checkout_shipping_steps.enter_city(self.city)
        self.checkout_shipping_steps.enter_zip_code(self.zip_code)
        self.checkout_shipping_steps.choose_country()
        self.checkout_shipping_steps.enter_phone_number(self.phone_number)
        self.checkout_shipping_steps.click_on_radio_button()
        self.checkout_shipping_steps.click_on_place_order()
        self.checkout_payment_steps.click_on_pay()
        assert self.payment_page.thank_you().is_displayed()
        self.singleton.quit_driver()

    @allure.suite("Buying Products")
    @allure.title("Buying product negative")
    @allure.description("flow of user purchasing product unsuccessfully")
    def test_register_positive(self):
        self.base_steps.open_base_page()
        self.base_steps.click_product()
        self.product_steps.click_on_add_cart()
        self.header_steps.click_on_cart()
        self.cart_popup_steps.click_on_proceed()
        self.checkout_shipping_steps.click_on_place_order()
        assert self.checkout_shipping_page.warning().is_displayed()
        self.singleton.quit_driver()
