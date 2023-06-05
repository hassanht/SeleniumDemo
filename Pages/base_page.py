from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url):
        self.driver.get(base_url)

    def click(self, locator):
        """ Performs click on web element whose locator is passed to it"""
        locator.click()

    def enter_text(self, locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        locator.send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_present(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements_to_be_present(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_elements_to_be_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def scroll_to_window(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
