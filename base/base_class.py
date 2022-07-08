from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_locator(self, find_by):
        locators = {
            'xpath': By.XPATH,
            'id': By.ID,
            'name': By.NAME
        }
        return locators[find_by]

    def is_clickable(self, find_by, locator):
        return self.wait.until(ec.element_to_be_clickable((self.get_locator(find_by), locator)))

    def is_present(self, find_by, locator):
        return self.wait.until(ec.presence_of_element_located((self.get_locator(find_by), locator)))

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
            return True
        except:
            return False