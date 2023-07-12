import pytest
from selenium import webdriver

from Pages.demo_page import DemoPage
from Utilities.constants import BASE_URL, IMPLICIT_WAIT_TIME


@pytest.fixture(params=['chrome', 'firefox'], scope="class")
def driver(request):
    """
        Fixture to initialize the WebDriver instance based on the selected browser.

        This fixture receives the selected browser as a parameter and sets up the WebDriver instance accordingly.
        It maximizes the window, sets an implicit wait time of 30 seconds, and navigates to the specified base URL.
        The WebDriver instance is then attached to the request object, allowing it to be used in the test classes.

        Args:
            request: The pytest request object containing the test configuration and fixtures.

        Yields:
            WebDriver: The initialized WebDriver instance.

        Raises:
            ValueError: If an invalid browser option is provided.

        Returns:
            None
    """
    base_url = BASE_URL
    implicit_wait_time = IMPLICIT_WAIT_TIME
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError("Invalid browser option. Please specify 'chrome' or 'firefox'.")
    driver.maximize_window()
    driver.implicitly_wait(implicit_wait_time)
    driver.get(base_url)
    request.cls.driver = driver
    yield driver
    driver.quit()
