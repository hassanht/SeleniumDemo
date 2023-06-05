import time

import pytest

from Pages.demo_page import DemoPage


@pytest.mark.usefixtures("driver")
class TestDemo:

    def test_website_loads(self):
        assert "Practice Page" in self.driver.title

    def test_select_radio_button(self):
        radio_button_value = "radio2"
        demo_page = DemoPage(self.driver)
        demo_page.select_radio_field(radio_button_value)
        assert demo_page.check_radio_button_is_clicked(radio_button_value)

    def test_type_to_select_country(self):
        search_value = "Pakistan"
        demo_page = DemoPage(self.driver)
        demo_page.search_country(search_value)
        assert demo_page.get_country() in search_value

    def test_select_multiple_check_box(self):
        search_value = ["option1", "option3"]
        demo_page = DemoPage(self.driver)
        demo_page.click_multiple_checkbox(search_value)
        assert demo_page.check_multiple_checkbox_are_clicked(search_value)

    def test_scroll_to_latest_news_text(self):
        demo_page = DemoPage(self.driver)
        demo_page.scroll_to_latest_news_text()
        assert demo_page.check_latest_news_text_is_displayed()
