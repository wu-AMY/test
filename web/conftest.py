import os
from typing import List
from selenium import webdriver
import pytest

from web.WXK_union.index_page import IndexPage


@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_index():
    index = IndexPage()
    yield index


@pytest.fixture()
def get_driver_browser():
    browser = os.getenv("browser")
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login():
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=options)
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



