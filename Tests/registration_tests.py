import os
import sys

import allure

from Steps.base_page_steps import BaseSteps
from Steps.registration_steps import RegistrationSteps
from Utils.fake_data import FakeData
from Utils.singleton import SingletonClass

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestRegistration:
    singleton = SingletonClass()
    step = RegistrationSteps()
    base = BaseSteps()
    data = FakeData()
    first_name = data.generate_first_name()
    last_name = data.generate_last_name()
    email = data.generate_email()
    password = data.generate_password()

    @allure.suite("Authentication")
    @allure.title("Registration Positive")
    @allure.description("Passing correct credentials to register user")
    def test_register_positive(self):
        self.base.open_base_page()
        self.base.click_on_create_on_account()
        self.step.enter_first_name(self.first_name)
        self.step.enter_last_name(self.last_name)
        self.step.enter_email(self.email)
        self.step.enter_password(self.password)
        self.step.enter_confirm_password(self.password)
        self.step.click_on_register()
        self.singleton.quit_driver()