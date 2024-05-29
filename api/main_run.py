import os

import pytest

if __name__ == '__main__':
    pytest.main(["-vs", "./case/test_login01.py", "--alluredir", './result', '--clean-alluredir'])
    os.system("allure generate ./result/ -o ./report_allure --clean")