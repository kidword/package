import time
from selenium import webdriver


class Login(object):
    def __init__(self, login_url):
        self.login_url = login_url
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_url)

    def get_element(self):
        username = self.driver.find_element_by_class_name('userName')
        pwd = self.driver.find_element_by_class_name('userPwd')
        img_code = self.driver.find_element_by_class_name('checkCode')
        login_btn = self.driver.find_element_by_class_name('login_btn')
        return username, pwd, img_code, login_btn

    def get_img_code(self):
        # 截图获取验证码
        self.driver.save_screenshot('login.png')

    def main(self, username=None, password=None):
        self.get_img_code()
        img_code = input("请输入验证码：")
        if username and password and img_code:
            element = self.get_element()
            element[0].send_keys(username)
            element[1].send_keys(password)
            element[2].send_keys(img_code)
            element[3].click()
            time.sleep(3)
            cookies = self.driver.get_cookies()
            time.sleep(5)
            self.driver.quit()
            return cookies
        else:
            print('检查输入内容')


if __name__ == '__main__':
    login_url = ''
    login = Login(login_url)
    username = ''
    password = ''
    cookies = login.main(username=username, password=password)
    print(cookies)
