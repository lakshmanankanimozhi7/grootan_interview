from src.helpers.grootan_helper import GrootanHelper
import pytest
import logging
from src.tests.base_test import BaseTest




class GrootanTest(BaseTest):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    """
              This test is to take screenshot by clicking all the available sections (home,services,open source,blog,team,careers,contact us) on the website and save it to folder 1
    """
    @pytest.mark.order1
    def test_screenshot_of_all_sections_in_website(self):
        grootan_helper = GrootanHelper()
        folder_number = "1"
        grootan_helper.visit_grootan_page()
        grootan_helper.click_home_button_and_take_screenshot(folder_num=folder_number)
        grootan_helper.click_services_button_and_take_screenshot(folder_num=folder_number)
        grootan_helper.click_open_source_button_and_take_screenshot(folder_num=folder_number)
        grootan_helper.click_blog_button_and_take_screenshot(folder_num=folder_number)
        grootan_helper.click_team_button_and_take_screenshot(folder_num=folder_number)
        grootan_helper.click_careers_button_and_take_screenshot(folder_num=folder_number)
        grootan_helper.click_contact_us_button_and_take_screenshot(folder_num=folder_number)

    """
        This test is to compare screenshots of home page
    """

    @pytest.mark.order2
    def test_compare_screenshots_of_home_page(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.click_home_button_and_take_screenshot(folder_num="2")
        value= grootan_helper.compare_screenshot(file_name=grootan_helper.home_button_header_name())
        assert value == 0

    """
            This test is to compare screenshots of services page
    """

    @pytest.mark.order3
    def test_compare_screenshots_of_services_page(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.click_services_button_and_take_screenshot(folder_num="2")
        value = grootan_helper.compare_screenshot(file_name=grootan_helper.services_button_header_name())
        assert value == 0

    """
            This test is to compare screenshots of open source page
    """

    @pytest.mark.order4
    def test_compare_screenshots_of_open_source_page(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.click_open_source_button_and_take_screenshot(folder_num="2")
        value = grootan_helper.compare_screenshot(file_name=grootan_helper.open_source_button_header_name())
        assert value == 0

    """
            This test is to compare screenshots of blog page
    """

    @pytest.mark.order5
    def test_compare_screenshots_of_blog_page(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.click_blog_button_and_take_screenshot(folder_num="2")
        value = grootan_helper.compare_screenshot(file_name=grootan_helper.blog_button_header_name())
        assert value == 0

    """
            This test is to compare screenshots of team page
    """

    @pytest.mark.order6
    def test_compare_screenshots_of_team_page(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.click_team_button_and_take_screenshot(folder_num="2")
        value = grootan_helper.compare_screenshot(file_name=grootan_helper.team_button_header_name())
        assert value == 0

    """
            This test is to compare screenshots of career page
    """

    @pytest.mark.order7
    def test_compare_screenshots_of_career_page(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.click_careers_button_and_take_screenshot(folder_num="2")
        value = grootan_helper.compare_screenshot(file_name=grootan_helper.careers_button_header_name())
        assert value == 0

    """
            This test is to compare screenshots of contact us page
    """

    @pytest.mark.order8
    def test_compare_screenshots_of_contact_us_page(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.click_contact_us_button_and_take_screenshot(folder_num="2")
        value = grootan_helper.compare_screenshot(file_name=grootan_helper.contact_us_button_header_name())
        assert value == 0


    """
            This test is to print number of junior engineers on team page in excel
    """

    @pytest.mark.order9
    def test_print_number_of_junior_engineers_on_team_page(self):
        grootan_helper = GrootanHelper()
        grootan_helper.visit_grootan_page()
        grootan_helper.visit_team_page_and_print_junior_software_names()

    """
            This test is to compare co_founder and HR manager images. The test will fail as expected
    """

    @pytest.mark.order10
    def test_compare_co_founder_and_hr_images(self):
        grootan_helper = GrootanHelper()
        grootan_helper.take_screenshots_of_co_founder_and_hr_manager()
        value = grootan_helper.compare_screenshot(file_name="co_founder",file_name_2="hr_manager")
        assert value == 0






