import re, allure, os


@allure.story("编辑个人信息 原密码 新密码")
@allure.issue("个人信息有bug, http://zentao/xxx.html 对应bug在哪个页面")
def test_edit_per_pwd(login_fixture, opwd='1234abcd', newpwd='1234abcd'):
    s = login_fixture
    url = os.environ["admin_host"]+"/admin/password_change/"
    r = s.get(url=url)
    cmt = re.findall("'csrfmiddlewaretoken' value='(.+?)'", r.text)
    body = {
        "csrfmiddlewaretoken": cmt[0],
        "old_password": opwd,
        "new_password1": newpwd,
        "new_password2": newpwd
    }
    r = s.post(url=url, data=body)
    assert r.status_code == 200
    assert "密码更改成功" in r.text
