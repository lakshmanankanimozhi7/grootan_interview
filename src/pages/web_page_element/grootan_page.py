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

    def team_member_role(self,x,y):
        team_member_role = (By.CSS_SELECTOR,f"#root .section.section.team.design-two .col-xl-10 div:nth-child({str(x)}) > div:nth-child({str(y)}) .member-role")
        return team_member_role

    def team_member_name(self,x,y):
        team_member_name = (By.CSS_SELECTOR,f"#root .section.section.team.design-two .col-xl-10 div:nth-child({str(x)}) > div:nth-child({str(y)}) .member-name")
        return team_member_name

    co_founder_image = (By.CSS_SELECTOR,".team .col-xl-10 div:nth-child(1) > div:nth-child(1) > img")
    hr_manager_image = (By.CSS_SELECTOR,".team .col-xl-10 div:nth-child(1) > div:nth-child(2) > img")
    cookie_decline = (By.CSS_SELECTOR,"#root .col-lg-5 button")
    full_page_element = (By.CSS_SELECTOR,' body[data-aos-easing="ease"] #root')
    blog_full_page_element = (By.CSS_SELECTOR," body #___gatsby")
    close_grootan_chat = (By.CSS_SELECTOR,"#root .drift-widget-controller-icon.circle")
    chat_active = (By.CSS_SELECTOR,"#root .drift-widget-controller--closed")
    iframe_grootan_chat = (By.XPATH,"/html/body/div[3]/iframe")






