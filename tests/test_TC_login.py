import time

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pom.login_page import LoginPage
from utilities.logs import GetLogs

logger = GetLogs.get_logs()
class TestLogin:
    url = 'https://demo.guru99.com/V4/index.php'
    def test_login(self, setup):
        driver = setup
        driver.get(TestLogin.url)
        logger.debug('the page was opened')
        loginPage = LoginPage(driver)
        loginPage.fill_username('mngr418032')
        logger.debug('the username filed was filled')
        loginPage.fill_password('nyqUsYj')
        logger.debug('the password field was filled')
        loginPage.click_login()
        time.sleep(3)

        if loginPage.is_alert_present() == True:
            driver.switch_to.alert.accept()
            print('Test Failed')
            logger.debug('Test failed')
            assert False
        else:
            if loginPage.get_member_id().text == 'Manger Id : mngr418032':
                print('Test Passed')
                logger.debug('Test passed')
                assert True
            else:
                print('Test Failed')
                logger.debug('Test failed')
                assert False