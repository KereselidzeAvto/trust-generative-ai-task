import pytest
from Utils.singleton import SingletonClass


@pytest.fixture(scope="function")
def setup_driver():
    singleton = SingletonClass()
    driver = singleton.get_driver
    singleton.navigate_to("https://magento.softwaretestingboard.com/")
    yield driver
    singleton.quit_driver()
