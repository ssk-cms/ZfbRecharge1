# -*- coding: utf-8 -*-
import json
import requests
from selenium import webdriver
import time
import random
import threading

# from apps.aliPay.models import Cookies


status = "未登录"


class Chromes(object):
    def __init__(self, username=None, passwd=None):
        self.username = username
        self.password = passwd
        self._login_url = "https://auth.alipay.com/login/index.htm"
        self.threads = 0
        self.is_login = False
        self.login_times = 0
        self.ck = None
        # cookie存储
        self.session = requests.session()
        self.cookie = {}
        self._browser = webdriver.Chrome()

    # 减慢账号密码的输入速度
    @staticmethod
    def _slow_input(ele, word):
        for i in word:
            # 输出一个字符
            ele.send_keys(i)
            # 随机睡眠0到1秒
            time.sleep(random.uniform(0, 1))

    def login(self):
        # if self._login_url in self._browser.current_url:
        #
        #     # 点击密码登录的选项卡
        #     self._browser.find_element_by_xpath('//*[@id="J-loginMethod-tabs"]/li[2]').click()
        #     # 用户名输入框
        #     username = self._browser.find_element_by_id('J-input-user')
        #     username.clear()
        #     print('正在输入账号.....')
        #     self._slow_input(username, self.username)
        #     time.sleep(random.uniform(0.4, 0.8))
        #     # 密码输入框
        #     password = self._browser.find_element_by_xpath('//*[@id="password_container"]/input')
        #     password.clear()
        #     print('正在输入密码....')
        #     self._slow_input(password, self.password)
        #     # 判断是否出现验证码
        #     if self._browser.find_element_by_class_name("ui-checkcode"):
        #         imgUrl = self._browser.find_element_by_id("J-checkcode-img").get_attribute("src")
        #         img = requests.get(imgUrl)
        #         with open('verficode.png', 'wb') as f:
        #             # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
        #             f.write(img.content)
        #         time.sleep(random.uniform(20,40))
        #     else:
        #         # 登录按钮
        #         time.sleep(random.uniform(0.5, 1))
        #     self._browser.find_element_by_id('J-login-btn').click()
        #     self.login_times = self.login_times + 1

            # 判断是否出现短信验证
            # https://authet15.alipay.com/login/checkSecurity.htm
        time.sleep(20)
        # 输出当前链接
        print("当前页面链接: " + self._browser.title)
        if "登录" in self._browser.title:
            print("登录失败")
            return False
        else:
            print("登录成功")
            return True
        # return True

    # set cookies 到 session
    def _set_cookies(self):
        cookie = self.cookie
        self.session.cookies.update(cookie)

        return True

    # 判断是否需要登录
    def islogin(self):
        flag = True
        if self._login_url in self._browser.current_url:
            print("islogin")
            flag = self.login()
        if flag:
            self.save_cookies()
        self.is_login = flag
        return flag

    def save_cookies(self):
        # 获取cookies转换成字典
        cookies = self._browser.get_cookies()
        # cookie字典
        cookies_dict = {}
        for cookie in cookies:

            if 'name' in cookie and 'value' in cookie:
                cookies_dict[cookie['name']] = cookie['value']

        # 向数据库保存cookie
        cookies_str = json.dumps(cookies_dict)
    #     self.db_get_or_update_cookies(cookies_str)
    #
    # def db_get_or_update_cookies(self, cookies_str):
    #     alipay = Cookies.objects(name='alipay')
    #     if alipay:
    #         alipay.update(set__cookies=cookies_str, set__updated_at=int(time.time()))
    #     else:
    #         Cookies(cookies=cookies_str).save()


class MyThread(threading.Thread):
    AccountDetailUrl = 'https://mbillexprod.alipay.com/enterprise/fundAccountDetail.htm'

    def __init__(self, chrome):
        super(MyThread, self).__init__()
        self.chrome = chrome
        self.flag = True
        self.thread_sum = chrome.threads + 1

    def run(self):
        while self.flag:

            self.chrome._browser.get(self.AccountDetailUrl)

            self.chrome._browser.implicitly_wait(3)
            if self.chrome.islogin():

                print("" + str(self.thread_sum))
                time.sleep(180)  # 一分钟刷新一次
            else:
                self.flag = False
                self.thread_sum = self.thread_sum - 1
                print("" + str(self.thread_sum))


def start_chrome(username, password):
    status = ""

    if username == None:
        status = '用户名不能为空'
    if password == None:
        status = '密码不能为空'

    chrom = Chromes()

    chrom.username = username
    chrom.password = password
    if status == "":
        is_login = chrom.is_login
        if is_login:
            status = "在线中...."
        else:
            status = "不在线，登录中..."
        if chrom.threads == 0:
            thread = MyThread(chrom)
            thread.start()

    return status
if __name__ == "__main__":

    start_chrome = start_chrome("13295037295","110xiaoyangzi")