import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Utils.logger import LogManager


class SingletonClass:
    _instance = None
    _lock = threading.Lock()
    _logger = LogManager()

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._driver = None
            self._initialized = True
            self._logger = LogManager.get_logger()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._driver = None
        return cls._instance

    @property
    def get_driver(self):
        if self._driver is None:
            self._driver = self._create_driver()
        return self._driver

    def _create_driver(self):
        try:
            chrome_options = Options()
            # chrome_options.add_argument("--headless")  # uncomment to run tests in headless mode
            chrome_options.add_argument("--enable-automation")
            chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=chrome_options)
            self._logger.info(f"Successfully created Webdriver")
            return driver
        except Exception as e:
            self._logger.error(f"Error while creating WebDriver: {e}")
            raise e

    def quit_driver(self):
        try:
            if self._driver is not None:
                self._driver.quit()
                self._driver = None
                self._logger.info("WebDriver quite successfully")
        except Exception as e:
            self._logger.error(f"Error while quiting WebDriver: {e}")
            raise e

    def find_element(self, by, value: str, timeout=10):
        try:
            element = WebDriverWait(self.get_driver, timeout).until(
                EC.presence_of_element_located((by, value)))
            self._logger.info("Element found successfully")
            return element
        except Exception as e:
            self._logger.error(f"Error while finding element: {e}")
            raise e

    def navigate_to(self, url):
        try:
            self.get_driver.get(url)
            self._logger.info(f"Successfully navigated to: {url}")
        except Exception as e:
            self._logger.error(f"Error while navigating to {url} : {e}")
            raise e

    def wait_for_element_clickable(self, by, value: str, timeout=10):
        try:
            element = WebDriverWait(self.get_driver, timeout).until(
                EC.element_to_be_clickable((by, value)))
            self._logger.info("Element is clickable")
            return element
        except Exception as e:
            self._logger.error(f"Error while waiting for element to be clickable: {e}")
            raise e

    def click_element(self, by, value: str, timeout=10):
        try:
            element = self.wait_for_element_clickable(by, value, timeout)
            element.click()
            self._logger.info("Successfully clicked element")
        except Exception as e:
            self._logger.error(f"Error while clicking element : {e}")
            raise e

    def input_text(self, by, value: str, text, timeout=10):
        try:
            element = self.wait_for_element_clickable(by, value, timeout)
            element.send_keys(text)
            self._logger.info("Successfully inputted text")
        except Exception as e:
            self._logger.error(f"Error while inputting text: {e}")
            raise e

    def switch_to_frame(self, by, value: str, timeout=10):
        try:
            frame = WebDriverWait(self.get_driver, timeout).until(
                EC.frame_to_be_available_and_switch_to_it((by, value)))
            self._logger.info("Successfully switched to frame")
            return frame
        except Exception as e:
            self._logger.error(f"Error while switching to frame: {e}")
            raise e

    def switch_to_default_content(self):
        try:
            self.get_driver.switch_to.default_content()
            self._logger.info("Successfully switched to default content")
        except Exception as e:
            self._logger.error(f"Error while switching to default content: {e}")
            raise e

    def get_current_url(self):
        return self.get_driver.current_url
