import re, allure, os


# 公共获取token操作函数
@allure.step("登录步骤")
def login(s, username="soapyuki", password="1234abcd"):
    '''登录获取token或获取cookie'''
    url = os.environ["admin_host"]+"/admin/login/?next=/admin/"
    r = s.get(url=url)
    cmt = re.findall("'csrfmiddlewaretoken' value='(.+?)'", r.text)
    body = {
        "csrfmiddlewaretoken": cmt[0],
        "username": username,
        "password": password
    }
    r = s.post(url=url, data=body)
    return r
