from src.pages.web_page_element.grootan_page import GrootanPage
from src.tests.base_test import BaseTest
import src.framework.global_config as config
import time
from PIL import Image, ImageDraw
import os
import xlsxwriter
import numpy as np
import cv2


class GrootanHelper(BaseTest):

    grootan_page = GrootanPage()

    def save_screen_shot(self, name,num):
        dir = os.getcwd() + "/screenshots{}/".format(num)
        if not os.path.exists(dir):
            os.makedirs(dir)
        file_name = dir + name + ".png"
        self.logger.info(file_name)
        config.DRIVER.save_screenshot(filename=file_name)

    def visit_grootan_page(self, url=None):
        self.grootan_page.open_url(uri=self.grootan_page.APP_URL)

    def click_home_button_and_take_screenshot(self):
        self.grootan_page.click(self.grootan_page.home_button)
        self.save_screen_shot("homes","1")

    def verify_what_we_do_text_in_services_page(self):
        text = self.grootan_page.get_attribute(self.grootan_page.what_we_do_text_in_services_page,"innerText")
        assert text == "What We Do"

    def click_services_button_and_take_screenshot(self):
        self.grootan_page.click_and_wait(self.grootan_page.services_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot("servicess","1")

    def click_open_source_button_and_take_screenshot(self):
        self.grootan_page.click_and_wait(self.grootan_page.open_source_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot("open_sources","1")

    def click_blog_button_and_take_screenshot(self):
        self.grootan_page.click_and_wait(self.grootan_page.blog_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot("blogs","1")

    def click_team_button_and_take_screenshot(self):
        self.grootan_page.click_and_wait(self.grootan_page.team_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot("teams","1")

    def click_careers_button_and_take_screenshot(self):
        self.grootan_page.click_and_wait(self.grootan_page.careers_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot("careers","1")

    def click_contact_us_button_and_take_screenshot(self):
        self.grootan_page.click_and_wait(self.grootan_page.contact_us_button,timeout=3)
        time.sleep(2)
        self.save_screen_shot("contacts","1")





    def visit_grootan_page_(self,name,num,text):
        self.grootan_page.open_url(uri=self.grootan_page.APP_URL)
        time.sleep(2)
        self.grootan_page.click(self.grootan_page.search)
        self.grootan_page.type(self.grootan_page.search, text)
        self.save_screen_shot(name,num)

    def analyze(self):
        screenshot_staging = Image.open("screenshots1/page.png")
        screenshot_production = Image.open("screenshots2/page.png")
        columns = 60
        rows = 80
        screen_width, screen_height = screenshot_staging.size

        block_width = ((screen_width - 1) // columns) + 1  # this is just a division ceiling
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height + 1):
            for x in range(0, screen_width, block_width + 1):
                region_staging = self.process_region(screenshot_staging, x, y, block_width, block_height)
                region_production = self.process_region(screenshot_production, x, y, block_width, block_height)

                if region_staging is not None and region_production is not None and region_production != region_staging:
                    draw = ImageDraw.Draw(screenshot_staging)
                    draw.rectangle((x, y, x + block_width, y + block_height), outline="red")

        screenshot_staging.save("result.png")

    def process_region(self, image, x, y, width, height):
        region_total = 0

        # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 10

        for coordinateY in range(y, y + height):
            for coordinateX in range(x, x + width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel) / 4
                except:
                    return

        return region_total / factor




    def visit_team_page_and_print_junior_software_names(self):
        self.grootan_page.click(self.grootan_page.team_button)
        junior_engineers_list = []
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


    def compare_ss(self):
        img = cv2.imread("screenshots1/open_source.png")
        img1 = cv2.imread("screenshots1/open_sources.png")
        # compare image
        diff_img = cv2.subtract(img, img1)
        cv2.imwrite("screenshots1/diffs.png", diff_img)
        value = np.sum(diff_img)
        print(value)
        return value







    def write_data_in_excel(self):
        workbook = xlsxwriter.Workbook('Example3.xlsx')
        worksheet = workbook.add_worksheet("My sheet 1")


















