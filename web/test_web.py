import pytest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestSelienium:
    @pytest.mark.skip
    def test_selen(self,get_driver):
        # # 指定Chrome WebDriver的路径
        # get_driver.get("https://baidu.com")
        # get_driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("selenium")
        # # driver.find_element_by_id("kw").send_keys("selenium")
        # get_driver.find_element(By.XPATH, '//*[@id="su"]').click()
        # # driver.find_element_by_id("su").click()

        get_driver.get("https://baidu.com")
        get_driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("selenium")
        get_driver.find_element(By.CSS_SELECTOR, '#su').click()
        get_driver.find_element(By.CSS_SELECTOR, '[id=s_tab] a:nth-child(3)').click()
        time.sleep(10)

    @pytest.mark.skip
    def test_action(self,get_driver):
        get_driver.get("https://sahitest.com/demo/clicks.htm")
        # get_driver.find_element(By.XPATH, '//*[@name="f1"]/input[3]').click()
        element_click = get_driver.find_element(By.XPATH, '//input[@value="click me"]')
        element_double = get_driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        element_right = get_driver.find_element(By.XPATH, '//input[@value="right click me"]')
        action = ActionChains(get_driver)
        action.click(element_click)
        action.double_click(element_double)
        action.context_click(element_right)
        time.sleep(3)
        action.perform()
        time.sleep(3)

    #鼠标移动
    @pytest.mark.skip
    def test_moveto(self,get_driver):
        get_driver.get("https://baidu.com")
        ele = get_driver.find_element(By.XPATH, '//*[@id="s-top-left"]/div[last()]')
        time.sleep(3)
        action = ActionChains(get_driver)
        action.move_to_element(ele).perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_drop(self,get_driver):
        get_driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        ele_from = get_driver.find_element(By.XPATH, '//*[@id="dragger"]')
        ele_to = get_driver.find_element(By.XPATH, '//div[2]')
        action = ActionChains(get_driver)
        # action.drag_and_drop(ele_from,ele_to).per          form
        # action.click_and_hold(ele_from).release(ele_to).perform()
        action.click_and_hold(ele_from).move_to_element(ele_to).release().perform()
        time.sleep(3)
    #滚动
    @pytest.mark.skip
    def test_touchaction_scroll(self,get_driver):

        get_driver.get("https://www.baidu.com")
        # el = get_driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("selenium")
        # el_search = get_driver.find_element(By.CSS_SELECTOR, '#su').click()
        get_driver.find_element(By.LINK_TEXT, "登录")

    #多窗口切换
    @pytest.mark.skip
    def test_windows(self,get_driver):
        get_driver.get("https://www.baidu.com")
        get_driver.find_element(By.LINK_TEXT, "登录").click()
        time.sleep(3)
        get_driver.find_element(By.LINK_TEXT, "立即注册").click()
        time.sleep(3)
        print(get_driver.window_handles)
        print(get_driver.current_window_handle)
        for handle in get_driver.window_handles:
            if handle != get_driver.current_window_handle:
                get_driver.switch_to.window(handle)
                print(get_driver.current_url)
                get_driver.find_element(By.CSS_SELECTOR, '[name=userName]').send_keys("123456789")
                time.sleep(3)
                get_driver.find_element(By.CSS_SELECTOR, '[name=phone]').send_keys("17857411480")
                get_driver.close()
                time.sleep(3)
                get_driver.switch_to.window(get_driver.window_handles[0])
        get_driver.find_element(By.CSS_SELECTOR, '[name=userName]').send_keys("17857411480")
        time.sleep(3)
        get_driver.find_element(By.CSS_SELECTOR, '[name="password"]:nth-child(2)').send_keys("17857411480")
        # get_driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys("12345w")
        time.sleep(3)
        get_driver.find_element(By.CSS_SELECTOR, '[name=isAgree]').click()
        time.sleep(3)
        get_driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()
        time.sleep(3)

    #切换iframe
    @pytest.mark.skip
    def test_iframe(self, get_driver):
        get_driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # get_driver.switch_to_frame("iframeResult")
        get_driver.switch_to.frame("iframeResult")
        dragga_ele = get_driver.find_element(By.CSS_SELECTOR, '[id=draggable]')
        print(dragga_ele.text)
        time.sleep(3)
        drop_ele = get_driver.find_element(By.CSS_SELECTOR, '[id=droppable]')
        print(drop_ele.text)
        # action = ActionChains(get_driver)
        # action.drag_and_drop(dragga_ele,drop_ele).perform()
        time.sleep(3)
        get_driver.switch_to.default_content()
        # get_driver.switch_to.parent_frame()
        get_driver.find_element(By.CSS_SELECTOR, '[id=submitBTN]').click()


    def test_Js_scroll(self,get_driver):
        get_driver.get("https://www.baidu.com")
        get_driver.find_element(By.ID, 'kw').send_keys("selenium测试")
        element = get_driver.execute_script("return document.getElementById('su')")
        element.click()
        time.sleep(3)
        get_driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        # get_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        get_driver.find_element(By.CSS_SELECTOR,'[class="n"]').click()
        # time.sleep(5)
        for code in [
            'return document.body.scrollHeight', 'return document.documentElement.scrollHeight', 'return window.pageYOffset',
            'return document.title', 'return JSON.stringify(window.performance.timing)'
        ]:
            print(get_driver.execute_script(code))

    @pytest.mark.skip
    def test_datetime(self,get_driver):
        get_driver.get("https://www.12306.cn/index/")
        ele_date = get_driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        get_driver.execute_script("document.getElementById('train_date').value='2024-05-02'")
        time.sleep(3)
    @pytest.mark.skip
    def test_alert(self, get_driver):
        get_driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # get_driver.switch_to_frame("iframeResult")
        get_driver.switch_to.frame("iframeResult")
        # dragga_ele = get_driver.find_element(By.CSS_SELECTOR, '[id=draggable]')
        dragga_ele = get_driver.find_element(By.ID, 'draggable')
        print(dragga_ele.text)
        # time.sleep(3)
        drop_ele = get_driver.find_element(By.ID, 'droppable')
        print(drop_ele.text)
        action = ActionChains(get_driver)
        action.drag_and_drop(dragga_ele, drop_ele).perform()
        # time.sleep(3)
        get_driver.switch_to.alert.accept()
        get_driver.switch_to.default_content()
        # get_driver.switch_to.parent_frame()
        get_driver.find_element(By.CSS_SELECTOR, '[id=submitBTN]').click()
        time.sleep(3)


    def test_button(self, get_driver):
        get_driver.get("https://union.vip.com/index")
        get_driver.find_element(By.CSS_SELECTOR, '[class="el-button el-button--primary"]').click()
        time.sleep(3)
        print(get_driver.window_handles)
        print(get_driver.current_window_handle)
        # get_driver.find_element(By.CSS_SELECTOR, '[class="c-tab-nav-item  J-tab-nav-item is-tab-nav-item-active"]').click()
        time.sleep(3)
        #切换页面到用户登录页面
        get_driver.find_element(By.CSS_SELECTOR, '[data-current-item="form"]').click()
        #输入用户名字和密码
        get_driver.find_element(By.ID, "J_login_name").send_keys("17857411480")
        get_driver.find_element(By.ID, "J_login_pwd").send_keys("123456")
        time.sleep(3)
        checkbox_aggre = get_driver.find_element(By.CSS_SELECTOR, '[for="J_login_agree"]').click()
        get_driver.find_element(By.ID, "J_login_submit").click()
        time.sleep(10)










