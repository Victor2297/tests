from selenium.webdriver.common.by import By

from base.base_class import BaseClass
from utilities.read_properties import ReadProperties


class LoginPage(BaseClass):
    username_name = ReadProperties.get_username()
    password_name = ReadProperties.get_password()
    login_button_name = ReadProperties.get_login_button()
    manager_id_xpath = ReadProperties.get_manager_id()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_username(self):
        return self.is_present('name', LoginPage.username_name)

    def get_password(self):
        return self.is_present('name', LoginPage.password_name)

    def get_login_button(self):
        return self.is_clickable('name', LoginPage.login_button_name)

    def fill_username(self, uname):
        self.get_username().send_keys(uname)

    def fill_password(self, upass):
        self.get_password().send_keys(upass)

    def click_login(self):
        self.get_login_button().click()

    def get_member_id(self):
        return self.is_present('xpath', LoginPage.manager_id_xpath)

