import json
import time
import requests
from selenium import webdriver


class Login(object):
    def __init__(self, login_url):
        self.login_url = login_url
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_url)

    def get_element(self):
        username = self.driver.find_element_by_id('login_field')
        pwd = self.driver.find_element_by_id('password')
        # img_code = self.driver.find_element_by_id('checkCode')
        login_btn = self.driver.find_element_by_class_name('btn-primary')
        return username, pwd, login_btn

    def get_img_code(self):
        # 截图获取验证码
        self.driver.save_screenshot('login.png')

    def main(self, username=None, password=None):
        # self.get_img_code()
        # img_code = input("请输入验证码：")
        if username and password:
            element = self.get_element()
            element[0].send_keys(username)
            element[1].send_keys(password)
            element[2].click()
            time.sleep(3)
            cookies = self.driver.get_cookies()
            time.sleep(5)
            self.driver.quit()
            return cookies
        else:
            print('检查输入内容')


if __name__ == '__main__':
    login_url = 'https://github.com/login'
    login = Login(login_url)
    username = ''
    password = ''
    cookies = login.main(username=username, password=password)
    # print(cookies)

    jsonCookies = json.dumps(cookies)
    # print(jsonCookies)
    with open('qqhomepage.json', 'w') as f:
        f.write(jsonCookies)

    str = ''
    with open('qqhomepage.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    cookie1 = [item["name"] + "=" + item["value"] for item in listCookies]
    cookiestr = ';'.join(item for item in cookie1)
    print(cookiestr)

    headers = {
        'cookie': cookiestr,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    response = requests.get('https://github.com/kidword', headers=headers)
    print(response.text)



