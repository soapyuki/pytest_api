import requests, re


class CourseAPI():
    def __init__(self, s):
        self.s = s

    def login(self, username="soapyuki", password="1234abcd"):
        # 获取登录页面
        login_page_url = "http://127.0.0.1:7777/admin/login/?next=/admin/"
        r  = self.s.get(url=login_page_url)
        # 此时cookie包含csrftoken
        # 响应页面内容中input:hidden 有个隐藏input
        # 对应值是csrfmiddlewaretoken
        '''name='csrfmiddlewaretoken' value='xxxx' '''
        cmt = re.findall("'csrfmiddlewaretoken' value='(.+?)'", r.text)
        # print(cmt[0])

        # 登录操作
        url = "http://127.0.0.1:7777/admin/login/?next=/admin/"
        body = {
            "csrfmiddlewaretoken": cmt[0],
            "username": username,
            "password": password
        }
        r = self.s.post(url=url, data=body)
        # print(r.text)

    def check_per_info(self):
        url = "http://127.0.0.1:7777/admin/auth/user/"
        r = self.s.get(url=url)
        # print(r.text)
        return r.text

    def edit_per_pwd(self, opwd='1234abcd', newpwd='1234abcd'):
        url = "http://127.0.0.1:7777/admin/password_change/"
        r = self.s.get(url = url)
        cmt = re.findall("'csrfmiddlewaretoken' value='(.+?)'", r.text)
        body = {
            "csrfmiddlewaretoken": cmt[0],
            "old_password": opwd,
            "new_password1": newpwd,
            "new_password2": newpwd
        }
        r =  self.s.post(url=url, data=body)
        # print(r.text)

if __name__ == '__main__':
    s = requests.session()
    obj = CourseAPI(s)
    obj.login()
    obj.check_per_info()
    obj.edit_per_pwd()


