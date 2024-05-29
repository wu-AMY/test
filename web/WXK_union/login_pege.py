import shelve
import time

from selenium.webdriver.common.by import By

from web.WXK_union.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def scan(self, cookies):
        db = shelve.open("cookies")
        db["cookie_vip"] = cookies
        self.db.close()
        time.sleep(2)
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://union.vip.com/index")
        self.driver.refresh()
        time.sleep(3)
        # return SuccessPage(self.driver)

    def phoneLogin(self, phone, code):
        self.driver.find_element(By.CSS_SELECTOR, '[data-current-item="form"]').click()
        # 输入用户名字和密码
        self.driver.find_element(By.ID, "J_login_name").send_keys("17857411480")
        self.driver.find_element(By.ID, "J_login_pwd").send_keys("123456")
        time.sleep(3)
        checkbox_aggre = self.driver.find_element(By.CSS_SELECTOR, '[for="J_login_agree"]').click()
        self.driver.find_element(By.ID, "J_login_submit").click()
        time.sleep(10)

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'[class = "c-register-link J-password-login-register"]')
        return RegisterPage(self.driver)