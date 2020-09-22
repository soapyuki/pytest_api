import pytest, os
import requests,allure

@allure.story("查看个人信息 用例")
def test_per_info(login_fixture):
    ''' 查看个人信息 接口详情
    url： "http://127.0.0.1:7777/admin/auth/user/"
    请求方法 get
    请求头
    请求参数'''
    s = login_fixture
    url = os.environ["admin_host"]+"/admin/auth/user/"
    r = s.get(url=url)
    assert r.status_code == 200
    assert "选择 用户 来修改 " in r.text
