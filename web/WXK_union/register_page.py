import time

from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
    def register(self, mobile_num, password):
        self.driver.find_element(By.ID, "J_mobile_name").send_keys(mobile_num)
        self.driver.find_element(By.ID, "J_mobile_pwd").send_keys(password)
        self.driver.find_element(By.ID, "J_mobile_confirm_pwd").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "[class = 'ui-checkbox-simulation']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "ui-btn-loading-before").click()
        time.sleep(3)




