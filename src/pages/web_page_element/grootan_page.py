from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class GrootanPage(BasePage):
    home_button = (By.CSS_SELECTOR,"#main-nav .st-nav-menu li:nth-child(2) a:nth-child(1)")
    services_button = (By.CSS_SELECTOR,"#main-nav .st-nav-menu li:nth-child(2) a:nth-child(2)")
    what_we_do_text_in_services_page = (By.CSS_SELECTOR,"#built-tech .section-heading.text-center h2")
    open_source_button = (By.CSS_SELECTOR,".st-nav-menu li:nth-child(2) a:nth-child(3)")
    blog_button = (By.CSS_SELECTOR,".st-nav-menu li:nth-child(2) a:nth-child(4)")
    team_button = (By.CSS_SELECTOR,".st-nav-menu li:nth-child(2) a:nth-child(5)")
    careers_button = (By.CSS_SELECTOR,".st-nav-menu li:nth-child(2) a:nth-child(6)")
    contact_us_button = (By.CSS_SELECTOR,".st-nav-menu li:nth-child(2) a:nth-child(7)")

    search =(By.CSS_SELECTOR,'input[title="Search"]')

    def team_member_role(self,x,y):
        team_member_role = (By.CSS_SELECTOR,f"#root .section.section.team.design-two .col-xl-10 div:nth-child({str(x)}) > div:nth-child({str(y)}) .member-role")
        return team_member_role

    def team_member_name(self,x,y):
        team_member_name = (By.CSS_SELECTOR,f"#root .section.section.team.design-two .col-xl-10 div:nth-child({str(x)}) > div:nth-child({str(y)}) .member-name")
        return team_member_name

    def more_to_come(self,x,y):
        more_to_come = (By.CSS_SELECTOR,f"#root .section.section.team.design-two .col-xl-10 div:nth-child({str(x)}) > div:nth-child({str(y)}) a")
        return more_to_come






