import logging
import pytest
from Pages.demo_page import DemoPage
from Utilities.utilities import Utils


@pytest.mark.usefixtures("driver")
class TestDemo():
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.demo_page = DemoPage(self.driver)

    @pytest.mark.parametrize("abc,qrs,xyz", [("Hello", "test", "user"), ("Hello", "test", "user2")])
    def test_website_loads(self, abc, qrs, xyz):
        """
        Test case to verify if the website loads successfully.

        Test Steps:
        1. Assert the expected page title contains the string "Practice Page".

        Args:
            None

        Returns:
            None
        """
        self.log.info("Asserting on title: %s %s %s", abc, qrs, xyz)
        assert "Practice Page" in self.demo_page.get_title()

    # def test_select_radio_button(self):
    #     """
    #     Test case to verify the selection of a radio button.
    #
    #     Test Steps:
    #     1. Select a specific radio button value.
    #     2. Assert if the selected radio button is selected.
    #
    #     Args:
    #         None
    #
    #     Returns:
    #         None
    #     """
    #
    #     radio_button_value = "radio2"
    #     self.demo_page.select_radio_field(radio_button_value)
    #     assert self.demo_page.is_radio_button_selected(radio_button_value)
    #
    # def test_type_to_select_country(self):
    #     """
    #     Test case to verify the selection of a country by typing.
    #
    #     Test Steps:
    #     1. Type the search value for the country.
    #     2. Search for the country.
    #     3. Assert if the selected country matches the search value.
    #
    #     Args:
    #         None
    #
    #     Returns:
    #         None
    #     """
    #
    #     search_value = "Pakistan"
    #     self.demo_page.search_country(search_value)
    #
    # def test_select_multiple_check_box(self):
    #     """
    #     Test case to verify the selection of multiple checkboxes.
    #
    #     Test Steps:
    #     1. Select multiple checkboxes based on the provided values.
    #     2. Assert if all the selected checkboxes are selected.
    #
    #     Args:
    #         None
    #
    #     Returns:
    #         None
    #     """
    #
    #     search_values = ["option1", "option3"]
    #     self.demo_page.select_multiple_checkboxes(search_values)
    #     assert self.demo_page.are_checkboxes_selected(search_values)
    #
    # def test_scroll_to_latest_news_text(self):
    #     """
    #     Test case to verify scrolling to the latest news text.
    #
    #     Test Steps:
    #     1. Scroll to the latest news text element.
    #     2. Assert if the latest news text is displayed.
    #
    #     Args:
    #         None
    #
    #     Returns:
    #         None
    #     """
    #
    #     self.demo_page.scroll_to_latest_news_text()
    #     assert self.demo_page.is_latest_news_text_displayed()
