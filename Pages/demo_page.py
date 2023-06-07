from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DemoPage(BasePage):
    radio_button = (By.XPATH, "//div[@id='radio-btn-example']//fieldset//label//input")
    input_search = (By.XPATH, "//input[@id='autocomplete']")
    searched_element = (By.XPATH, "//ul[@id='ui-id-1']//li")
    check_box = (By.XPATH, "//div[@id='checkbox-example']//label//input")
    latest_news_text_footer = (By.XPATH, "//a[normalize-space()='Latest News']")

    def __init__(self, browser):
        """
        Initialize the DemoPage class.

        Args:
            browser: WebDriver instance.

        Returns:
            None.
        """
        super().__init__(browser)

    def select_radio_field(self, option_to_select):
        """
        Selects a specific radio button based on the given option.

        Args:
            option_to_select: Option value of the radio button to be selected.

        Returns:
            None.
        """
        radio_buttons = self.wait_for_elements_to_be_visible(self.radio_button)
        for button in radio_buttons:
            if button.get_attribute("value") == option_to_select:
                self.click(button)

    def is_radio_button_selected(self, option_to_select):
        """
        Checks if a specific radio button is selected.

        Args:
            option_to_select: Option value of the radio button to be checked.

        Returns:
            True if the radio button is selected and its text matches the given option, False otherwise.
        """
        radio_buttons = self.wait_for_elements_to_be_visible(self.radio_button)
        for button in radio_buttons:
            if button.is_selected() and button.text in option_to_select:
                return True
        return False

    def search_country(self, country):
        """
        Searches and selects a country by typing in the search field.

        Args:
            country: Country name to be searched.

        Returns:
            None.
        """
        search = self.wait_for_element_to_be_visible(self.input_search)
        self.enter_text(search, country)
        dropdown_lists = self.wait_for_elements_to_be_present(self.searched_element)
        for dpl in dropdown_lists:
            if country in dpl.text:
                self.click(dpl)
                break

    def select_multiple_checkboxes(self, list_to_check):
        """
        Selects multiple checkboxes based on the provided list of values.

        Args:
            list_to_check: List of checkbox values to be selected.

        Returns:
            None.
        """
        check_boxes = self.wait_for_elements_to_be_present(self.check_box)
        for cb in check_boxes:
            if cb.get_attribute("value") in list_to_check:
                self.click(cb)

    def are_checkboxes_selected(self, list_to_check):
        """
        Checks if the specified checkboxes are selected.

        Args:
            list_to_check: List of checkbox values to be checked.

        Returns:
            True if all the checkboxes are selected, False otherwise.
        """
        check_boxes = self.wait_for_elements_to_be_present(self.check_box)
        for cb in check_boxes:
            if cb.is_selected() and cb.get_attribute("value") not in list_to_check:
                return False
        return True

    def scroll_to_latest_news_text(self):
        """
        Scrolls to the latest news text element.

        Returns:
            True if the latest news text is displayed after scrolling, False otherwise.
        """
        element = self.wait_for_element_to_be_visible(self.latest_news_text_footer)
        self.scroll_element_into_view(element)
        return element.is_displayed()

    def is_latest_news_text_displayed(self):
        """
        Checks if the latest news text element is displayed.

        Returns:
            True if the latest news text element is displayed, False otherwise.
        """
        element = self.wait_for_element_to_be_visible(self.latest_news_text_footer)
        return element.is_displayed()
