import shelve
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver


class TestLogin:
    def test_getCokies(self,get_driver):
        get_driver.get("https://union.vip.com/index")
        get_driver.find_element(By.CSS_SELECTOR, '[class="el-button el-button--primary"]').click()
        time.sleep(100)
        get_driver.get("https://union.vip.com/index")
        print(get_driver.get_cookies())



    def test_login(self,get_driver):
        #直接获取到cookies信息进行登录验证
        # cookies= [{ 'domain': '.vip.com', 'expiry': 1714404756, 'httpOnly': False, 'name': 'VipLID', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '0%7C1714361557%7C0671fd'},
        #  {'domain': '.vip.com', 'expiry': 1748921556, 'httpOnly': False, 'name': 'VipRNAME', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': 'amy001'},
        #  {'domain': '.vip.com', 'expiry': 1714793556, 'httpOnly': False, 'name': 'VipDegree', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': 'D1'},
        #  {'domain': '.vip.com', 'expiry': 1748921556, 'httpOnly': False, 'name': 'VipUID', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '57d6b666c0c50082c70d663efe4f256e'},
        #  {'domain': '.vip.com', 'expiry': 1748921556, 'httpOnly': False, 'name': 'VipRUID', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '335306176'},
        #  {'domain': '.vip.com', 'expiry': 1714390356, 'httpOnly': True, 'name': 'PASSPORT_ACCESS_TOKEN', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '04568170CD3531BD0297F8BFB165D8FAF9A2BB52'},
        #  {'domain': '.vip.com', 'httpOnly': False, 'name': 'vip_tracker_source_from', 'path': '/', 'sameSite': 'Lax',
        #   'secure': False, 'value': ''},
        #  {'domain': '.union.vip.com', 'expiry': 1748921529, 'httpOnly': False, 'name': 'vip_cps_uid', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '8b3408c402e54e4b914054dce2037d94'},
        #  {'domain': '.vip.com', 'httpOnly': False, 'name': 'pg_session_no', 'path': '/', 'sameSite': 'Lax',
        #   'secure': False, 'value': '1'},
        #  {'domain': 'union.vip.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'sameSite': 'Lax',
        #   'secure': False, 'value': '2004A30470FE7017E5717AD5FAE1E31A-s1'},
        #  {'domain': '.vip.com', 'expiry': 1714363335, 'httpOnly': False, 'name': 'vipshop_passport_src', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False,
        #   'value': 'https%3A%2F%2Funion.vip.com%2Fvip_login_redirect%3Ftimestamp%3D1714361531715'},
        #  {'domain': '.vip.com', 'expiry': 1714363445, 'httpOnly': False, 'name': 'visit_id', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '0B64AB856EA738D79EBAAD27276FC369'},
        #  {'domain': '.vip.com', 'expiry': 1714390356, 'httpOnly': False, 'name': 'user_class', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': 'c'},
        #  {'domain': '.vip.com', 'httpOnly': False, 'name': 'mars_sid', 'path': '/', 'sameSite': 'Lax', 'secure': False,
        #   'value': '180d547f45064152617168756c5f632d'},
        #  {'domain': '.vip.com', 'expiry': 1748921645, 'httpOnly': False, 'name': 'mars_cid', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '1714361530770_395eb32233286d089f6a863d823fff7a'},
        #  {'domain': '.union.vip.com', 'expiry': 1714447929, 'httpOnly': False, 'name': '_csrf_token', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '1714361530026'},
        #  {'domain': '.vip.com', 'expiry': 1748921645, 'httpOnly': False, 'name': 'mars_pid', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False, 'value': '0'},
        #  {'domain': '.vip.com', 'expiry': 1730129539, 'httpOnly': False, 'name': '_jzqco', 'path': '/',
        #   'sameSite': 'Lax', 'secure': False,
        #   'value': '%7C%7C%7C%7C%7C1.2126396045.1714361538985.1714361538985.1714361539003.1714361538985.1714361539003.0.0.0.1.1'}]
        # cookies = [{'name': 'JSESSIONID',  'value': 'C32745D449515C35B0451FEEFF49AD59-s2'}]
        # get_driver.get("https://passport.vip.com/login?src=https%3A%2F%2Funion.vip.com%2Fvip_login_redirect%3Ftimestamp%3D1714279745626")
        db = shelve.open("cookies")
        cookies = db["cookie_vip"]
        db.close()
        get_driver.get("https://union.vip.com/index")
        time.sleep(2)
        get_driver.delete_all_cookies()
        for cookie in cookies:
            get_driver.add_cookie(cookie)
        get_driver.get("https://union.vip.com/index")
        get_driver.refresh()
        time.sleep(3)

    def test_browserLogin(self,login):
        print(login.add_cookie())

    def test_shelve(self,get_driver):
        db = shelve.open("cookies")
        cokkies = db["cookie"]
        db.close()
        get_driver.get("https://www.baidu.com")
        for cookie in cokkies:
            get_driver.add_cookie(cookie)
        get_driver.refresh()






