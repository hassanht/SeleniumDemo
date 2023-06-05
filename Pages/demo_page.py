from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DemoPage(BasePage):
    radio_button = (By.XPATH, "//div[@id='radio-btn-example']//fieldset//label//input")
    """Input Search Fields"""
    input_search = (By.XPATH, "//input[@id='autocomplete']")
    searched_element = (By.XPATH, "//ul[@id='ui-id-1']//li")
    check_box = (By.XPATH, "//div[@id='checkbox-example']//label//input")
    latest_news_text_footer = (By.XPATH, "//a[normalize-space()='Latest News']")

    def __init__(self, browser):
        super().__init__(browser)

    def select_radio_field(self, option_to_select):
        radio_buttons = self.wait_for_elements_to_be_visible(self.radio_button)
        for button in radio_buttons:
            if button.get_attribute("value") == option_to_select:
                self.click(button)

    def check_radio_button_is_clicked(self, option_to_select):
        radio_buttons = self.wait_for_elements_to_be_visible(self.radio_button)
        for button in radio_buttons:
            if button.is_selected():
                if button.text in option_to_select:
                    return True
        return False

    def search_country(self, country):
        search = self.wait_for_element_to_be_visible(self.input_search)
        self.enter_text(search, country)
        dropdown_lists = self.wait_for_elements_to_be_present(self.searched_element)
        for dpl in dropdown_lists:
            if country in dpl.text:
                self.click(dpl)
                break

    def get_country(self):
        search = self.wait_for_element_to_be_visible(self.input_search)
        return search.text

    def click_multiple_checkbox(self, list_to_check):
        check_boxes = self.wait_for_elements_to_be_present(self.check_box)
        for cb in check_boxes:
            if cb.get_attribute("value") in list_to_check:
                self.click(cb)

    def check_multiple_checkbox_are_clicked(self, list_to_check):
        check_boxes = self.wait_for_elements_to_be_present(self.check_box)
        for cb in check_boxes:
            if cb.is_selected():
                if cb.get_attribute("value") in list_to_check:
                    pass
                else:
                    return False
        return True

    def scroll_to_latest_news_text(self):
        element = self.wait_for_element_to_be_visible(self.latest_news_text_footer)
        self.scroll_to_window(element)
        return element.is_displayed()

    def check_latest_news_text_is_displayed(self):
        element = self.wait_for_element_to_be_visible(self.latest_news_text_footer)
        return element.is_displayed()