import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="https://rahulshettyacademy.com/AutomationPractice/",
                     help="Base URL for the tests")
    parser.addoption("--browser", action="store", default="chrome,firefox",
                     help="Comma-separated list of browsers to run the tests on")



@pytest.fixture(params = ['chrome', 'firefox'])
def driver(request):
    # browser_option = request.config.getoption("--browser")
    base_url = request.config.getoption("--base-url")
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Invalid browser option. Please specify 'chrome' or 'firefox'.")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()
