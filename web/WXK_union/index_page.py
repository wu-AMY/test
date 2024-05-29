from selenium.webdriver.common.by import By
from selenium import webdriver

from web.WXK_union.login_pege import LoginPage
from web.WXK_union.register_page import RegisterPage


class IndexPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://union.vip.com/index")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def goto_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class = "el-button el-button--primary"]').click()
        return LoginPage(self.driver)
    def goto_cookies_login(self):
        return LoginPage(self.driver)
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class = "register-item user-select color-hover"]').click()
        return RegisterPage(self.driver)
