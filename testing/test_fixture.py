import pytest





@pytest.mark.usefixtures("login")
def test_case1():
    print("用例1")

def test_case2():
    print("用例2")


@pytest.mark.smoke
def test_case3(login, get_conn):
    print(login[0])
    print("用例3")


def test_username(name):
    print(name)
