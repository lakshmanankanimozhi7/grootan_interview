from src.pages.web_page_element.grootan_page import GrootanPage
from src.tests.base_test import BaseTest
import src.framework.global_config as config
import time
import os
import xlsxwriter
import numpy as np
import cv2
from matplotlib import pyplot as plt
from src.tests.base_test import BaseTest


class GrootanHelper(BaseTest):

    grootan_page = GrootanPage()

    """
        Save screenshot helper using save_screenshot() method
    """

    def save_screen_shot(self, name,num):
        time.sleep(2)
        # close cookie consent banner and grootan chat before taking screenshot
        try:
            self.click_cookie_decline()
            time.sleep(5)
            self.close_grootan_chat()
        except:
            pass
        dir = os.getcwd() + f"/Folder{str(num)}/"
        #if directory not exist create one
        if not os.path.exists(dir):
            os.makedirs(dir)
        file_name = dir + name + ".png"
        self.logger.info(file_name)
        # Take screenshot and save it as png format
        config.DRIVER.save_screenshot(filename=file_name)
        config.DRIVER.get_screenshot_as_png()

    """
        Open grootan website helper
    """

    def visit_grootan_page(self, url=None):
        self.grootan_page.open_url(uri=self.grootan_page.APP_URL)

    """
        Get home button header text
    """

    def home_button_header_name(self):
        return self.grootan_page.get_text(self.grootan_page.home_button)

    """
        Visit home page and take screenshot
    """

    def click_home_button_and_take_screenshot(self,folder_num):
        self.grootan_page.click(self.grootan_page.home_button)
        file_name = self.home_button_header_name()
        self.save_screen_shot(file_name,folder_num)
        #self.full_page_element_ss(image_name=file_name, folder_num=folder_num)

    """
        Get services button header text
    """

    def services_button_header_name(self):
        return self.grootan_page.get_text(self.grootan_page.services_button)

    """
        Visit services page and take screenshot
    """

    def click_services_button_and_take_screenshot(self,folder_num):
        file_name = self.services_button_header_name()
        self.grootan_page.click_and_wait(self.grootan_page.services_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot(file_name,folder_num)
        #self.full_page_element_ss(image_name=file_name, folder_num=folder_num)

    """
        Get open source button header text
    """

    def open_source_button_header_name(self):
        return self.grootan_page.get_text(self.grootan_page.open_source_button)

    """
        Visit open source page and take screenshot
    """

    def click_open_source_button_and_take_screenshot(self,folder_num):
        file_name = self.open_source_button_header_name()
        self.grootan_page.click_and_wait(self.grootan_page.open_source_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot(file_name,folder_num)
        #self.full_page_element_ss(image_name=file_name, folder_num=folder_num)

    """
        Get open blog button header text
    """

    def blog_button_header_name(self):
        return self.grootan_page.get_text(self.grootan_page.blog_button)

    """
        Visit blog page and take screenshot
    """

    def click_blog_button_and_take_screenshot(self,folder_num):
        file_name = self.blog_button_header_name()
        self.grootan_page.click_and_wait(self.grootan_page.blog_button,timeout=3)
        time.sleep(3)
        self.save_screen_shot(file_name,folder_num)
        #self.full_page_element_ss_blog(image_name=file_name, folder_num=folder_num)

    """
        Get open team button header text
    """

    def team_button_header_name(self):
        return self.grootan_page.get_text(self.grootan_page.team_button)

    """
        Visit team page and take screenshot
    """

    def click_team_button_and_take_screenshot(self,folder_num):
        file_name = self.team_button_header_name()
        self.grootan_page.click_and_wait(self.grootan_page.team_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot(file_name,folder_num)
        #self.full_page_element_ss(image_name=file_name, folder_num=folder_num)

    """
        Get careers button header text
    """

    def careers_button_header_name(self):
        time.sleep(2)
        header_name = self.grootan_page.get_text(self.grootan_page.careers_button)
        return header_name

    """
        Visit careers page and take screenshot
    """

    def click_careers_button_and_take_screenshot(self,folder_num):
        file_name = self.careers_button_header_name()
        self.grootan_page.click_and_wait(self.grootan_page.careers_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot(file_name,folder_num)
        #self.full_page_element_ss(image_name=file_name, folder_num=folder_num)

    """
        Get contact us button header text
    """

    def contact_us_button_header_name(self):
        return self.grootan_page.get_text(self.grootan_page.contact_us_button)

    """
        Visit contact us page and take screenshot
    """

    def click_contact_us_button_and_take_screenshot(self,folder_num):
        file_name = self.contact_us_button_header_name()
        self.grootan_page.click_and_wait(self.grootan_page.contact_us_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot(file_name,folder_num)
        #self.full_page_element_ss(image_name=file_name,folder_num=folder_num)

    """
            Visit team page , collect all junior engineer names and store it in new excel
    """

    def visit_team_page_and_print_junior_software_names(self):
        self.grootan_page.click(self.grootan_page.team_button)
        junior_engineers_list = []
        # get junior engineers name from the team page
        for x in range(1,20,2):

            for y in range(1,5,1):
               try:
                    if (self.grootan_page.get_text(self.grootan_page.team_member_role(x,y))) == "Junior Engineer":
                        name = self.grootan_page.get_text((self.grootan_page.team_member_name(x,y)))
                        junior_engineers_list.append(name)
                        print(name)
               except:
                   break

        number_of_junior_engineers = len(junior_engineers_list)
        print(number_of_junior_engineers)
        # create excel sheet and save all the junior engineers name
        workbook = xlsxwriter.Workbook("rekani.xlsx")
        worksheet = workbook.add_worksheet("JuniorEngineers")
        row = 0
        col = 0

        # Iterate over the data and write junior engineers name row by row.
        for name in (junior_engineers_list):
            worksheet.write(row, col, name)
            row += 1
        # Write total number of junior engineers name in the excel sheet
        worksheet.write(0, 1, "number_of_junior_engineers")
        worksheet.write(0, 2, number_of_junior_engineers)
        workbook.close()

    """
        Compare two screenshots and return value (if value == 0: "both the images are same" else: "Images are not same")
    """

    def compare_screenshot(self,file_name,file_name_2=None):

        img = cv2.imread(f"/Users/kanimozhi/PycharmProjects/grootan/src/tests/web/Folder1/{str(file_name)}.png")

        if file_name_2 != None:
            img1 = cv2.imread(f"/Users/kanimozhi/PycharmProjects/grootan/src/tests/web/Folder2/{str(file_name_2)}.png")
        else:
            img1 = cv2.imread(f"/Users/kanimozhi/PycharmProjects/grootan/src/tests/web/Folder2/{str(file_name)}.png")

        # find width and height of the images
        time.sleep(2)
        img_size = img.shape
        img1_size = img1.shape
        print(img1_size,img_size)

        #resize img1 with same height and width as img
        if(img_size[1]!=img1_size[1] or img_size[0]!=img1_size[0]):
            print("image resized")
            img1 = cv2.resize(img1, (img_size[1], img_size[0]))
            cv2.imwrite(f"/Users/kanimozhi/PycharmProjects/grootan/src/tests/web/FolderDiff/{str(file_name)}+resize.png",
                        img1)

        # find the difference between img, img1
        diff_img = cv2.subtract(img, img1)
        print(diff_img)
        value = np.sum(diff_img)
        cv2.imwrite(f"/Users/kanimozhi/PycharmProjects/grootan/src/tests/web/FolderDiff/{str(file_name)}+Diffs.png", diff_img)
        print(value)
        return value

    """
        Take screenshots of co_founder and HR manager images form team page
    """

    def take_screenshots_of_co_founder_and_hr_manager(self):
        self.visit_grootan_page()
        self.grootan_page.click_and_wait(self.grootan_page.team_button, timeout=3)
        time.sleep(3)
        self.click_cookie_decline()
        time.sleep(3)
        co_founder_element = self.grootan_page.find_element(self.grootan_page.co_founder_image)
        time.sleep(3)

        # Take screenshot using element and save image  as png
        co_founder_screenshot_by_element_in_bytes = co_founder_element.screenshot_as_png
        with open('src/tests/web/Folder1/co_founder.png', 'wb') as f:
            f.write(co_founder_screenshot_by_element_in_bytes)
        hr_manager_element = self.grootan_page.find_element(self.grootan_page.hr_manager_image)
        hr_manager_screenshot_by_element_in_bytes = hr_manager_element.screenshot_as_png
        with open('src/tests/web/Folder2/hr_manager.png', 'wb') as f:
            f.write(hr_manager_screenshot_by_element_in_bytes)

    """
        Take full page screenshot using element
    """

    def full_page_element_ss(self,image_name,folder_num):
        time.sleep(2)
        # close cookie consent banner and grootan chat before taking screenshot
        try:
            self.click_cookie_decline()
            time.sleep(5)
            self.close_grootan_chat()
        except:
            pass

        # Take screenshot using element and save image  as png
        full_page = self.grootan_page.find_element(self.grootan_page.full_page_element)
        time.sleep(5)
        full_page_in_bytes = full_page.screenshot_as_png
        with open(f'Folder{str(folder_num)}/{str(image_name)}.png', 'wb') as f:
            f.write(full_page_in_bytes)

    """
         Take full page screenshot of blog page using element
    """

    def full_page_element_ss_blog(self,image_name,folder_num):
        full_page = self.grootan_page.find_element(self.grootan_page.blog_full_page_element)
        time.sleep(5)
        full_page_in_bytes = full_page.screenshot_as_png
        with open(f'Folder{str(folder_num)}/{str(image_name)}.png', 'wb') as f:
            f.write(full_page_in_bytes)

    """
        Click cookie decline button on cookie consent banner
    """

    def click_cookie_decline(self):
        self.grootan_page.click(self.grootan_page.cookie_decline)

    """
        Close grootan chat
    """

    def close_grootan_chat(self):
        time.sleep(5)
        iframe = config.DRIVER.find_element_by_xpath('//iframe[@class="drift-frame-controller"]')
        # switch to grootan chat iframe
        config.DRIVER.switch_to.frame(iframe)
        time.sleep(5)
        if (self.grootan_page.is_element_present(self.grootan_page.chat_active)):
            self.grootan_page.click(self.grootan_page.close_grootan_chat)
        else:
            pass
        # switch to main page
        config.DRIVER.switch_to.default_content()


































