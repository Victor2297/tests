import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as Service_ch
from selenium.webdriver.firefox.service import Service as Service_ff
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


#@pytest.fixture
# def setup():
#     options = Options()
#     options.add_argument('start-maximized')
#     options.add_experimental_option('detach', True)
#     service = Service_ch(executable_path=ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     return driver

# @pytest.fixture
# def get_options():
#     options = Options()
#     options.add_argument('start-maximized')
#     options.add_experimental_option('detach', True)
#     return options
#
# @pytest.fixture
# def get_chrome_webdriver(get_options):
#     options = get_options
#     service = Service_ch(executable_path=ChromeDriverManager().install())
#     driver = webdriver.Chrome(service = service, options = options)
#     return driver
#
# @pytest.fixture
# def get_firefox_webdriver():
#     service = Service_ff(executable_path='C:\\Users\\Victor\\Downloads\\geckodriver-v0.30.0-win64\\geckodriver.exe')
#     driver = webdriver.Firefox(service = service)
#     return driver
#
# @pytest.fixture(params=['chrome', 'firefox'])
# def setup(request, get_chrome_webdriver, get_firefox_webdriver):
#     if request.param == 'chrome':
#         driver = get_chrome_webdriver
#         return driver
#     if request.param == 'firefox':
#         driver = get_firefox_webdriver
#         return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="session")
def get_browser(pytestconfig):
    return pytestconfig.getoption("browser")

@pytest.fixture
def setup(get_browser):
    if get_browser == 'chrome':
        options = Options()
        options.add_argument('start-maximized')
        options.add_experimental_option('detach', True)
        service = Service_ch(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service, options = options)
        return driver
    if get_browser == 'firefox':
        service = Service_ff(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service = service)
        return driver
    return get_browser
