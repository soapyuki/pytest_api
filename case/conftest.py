import pytest
import requests, allure
from case.common_func import login


@pytest.fixture(scope="session")
def login_fixture():
    '''登录操作'''
    s = requests.session()
    login(s)
    return s