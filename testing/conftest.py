from typing import List
from selenium import webdriver
import pytest

from pythoncode.calculator import Calculater


@pytest.fixture()
def login():

    #这个相当于tearup
    print("登录操作")

    #相当teardown
    yield ["tom","1234"]
    print("登出操作")


@pytest.fixture
def get_conn():
    #这个相当于tearup
    print("连接数据库，完成")
    #相当teardown


@pytest.fixture()
def get_calc():
    calc = Calculater()
    print("在执行setup_class")
    yield calc
    print("资源销毁  teardown_class")



@pytest.fixture(params=["成龙","甄子丹"],ids=["成龙1","甄子丹2"],name="name")
def get_username(request):
    print("这个是前置步骤")
    yield request.param
    print("这个是后置步骤")



@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]) -> None:
    items.reverse()
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")

        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        elif "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
