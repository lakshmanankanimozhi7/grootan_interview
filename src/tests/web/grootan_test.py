from src.helpers.grootan_helper import GrootanHelper
import pytest
import logging
from src.tests.base_test import BaseTest



@pytest.mark.grootantests
class GrootanTest(BaseTest):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    """
              Test click home button
    """

    def test_click_home_button(self):
        grootan_helper = GrootanHelper()

        grootan_helper.visit_grootan_page()
        grootan_helper.click_home_button_and_take_screenshot()
        grootan_helper.click_services_button_and_take_screenshot()
        grootan_helper.click_open_source_button_and_take_screenshot()
        grootan_helper.click_blog_button_and_take_screenshot()
        grootan_helper.click_team_button_and_take_screenshot()
        grootan_helper.click_careers_button_and_take_screenshot()
        grootan_helper.click_contact_us_button_and_take_screenshot()


    def test_1(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.visit_team_page_and_print_junior_software_names()

    def test_ss(self):
        grootan_helper = GrootanHelper()
        value= grootan_helper.compare_ss()
        assert value == 0











