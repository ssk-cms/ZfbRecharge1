'''
尝试登录支付宝
并获取账单记录

通过 seleium 登录支付宝，
获取 cookies
'''

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# 登录 url
Login_Url = 'https://auth.alipay.com/login/index.htm?goto=https%3A%2F%2Fwww.alipay.com%2F'
# 账单 url
Bill_Url = 'https://consumeprod.alipay.com/record/standard.htm'
#我的支付宝 url
MyZfb_Url = 'https://my.alipay.com/portal/i.htm'
# 充值页面
reCharge_Url = 'https://shenghuo.alipay.com/transfer/deposit/depositPreprocessGw.htm'
# 选择网银充值页面 url
e_bank_Url = 'https://cashiergtj.alipay.com:443/standard/deposit/chooseBank.htm?orderId=0619bedabc159101e112013083NN8402'


# 登录用户名和密码
USERNMAE = ''
PASSWD = ''

# 自定义 headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Referer': 'https://consumeprod.alipay.com/record/advanced.htm',
    'Host': 'consumeprod.alipay.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive'
}


class Alipay_Bill_Info(object):
    '''支付宝账单信息'''

    def __init__(self, headers, user, passwd):
        '''
        类的初始化

        headers：请求头
        cookies: 持久化访问
        info_list: 存储账单信息的列表
        '''
        self.headers = headers
        # 初始化用户名和密码
        self.user = user
        self.passwd = passwd
        # 利用 requests 库构造持久化请求
        self.session = requests.Session()
        # 将请求头添加到缓存之中
        self.session.headers = self.headers
        # 初始化存储列表
        self.info_list = []

    def wait_input(self, ele, str):
        '''减慢账号密码的输入速度'''
        for i in str:
            ele.send_keys(int(i))
            time.sleep(0.5)

    def get_cookies(self):
        '''获取 cookies'''

        # 初始化浏览器对象
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        sel = webdriver.Chrome('D:\Program Files\python\Scripts\chromedriver.exe',chrome_options=chrome_options)
        # sel = webdriver.Chrome()
        sel.maximize_window()
        sel.get(Login_Url)
        sel.implicitly_wait(3)
        # sel.find_element_by_xpath('//div[@class="authcenter-body-login"]/ul[@class="ui-nav"]/li')
        # 找到用户名字输入框
        # uname = sel.find_element_by_id('J-input-user')
        # uname.clear()
        # print('正在输入账号.....')
        # self.wait_input(uname, self.user)
        # time.sleep(1)
        # # 找到密码输入框
        # upass = sel.find_element_by_id('password_rsainput')
        # upass.clear()
        # print('正在输入密码....')
        # self.wait_input(upass, self.passwd)
        # 截图查看
        sel.save_screenshot('1.png')
        print("请30S内扫描二维码")
        time.sleep(30)
        # 找到登录按钮
        # butten = sel.find_element_by_id('J-login-btn')
        # time.sleep(1)
        # butten.click()
        # userStatus = input("请输入用户身份（个人/支付宝商家/口碑商家）：")
        # if userStatus == "个人":
        #     sel.find_element_by_class_name("personal")
        # elif userStatus == "支付宝商家":
        #     sel.find_element_by_class_name("seller-entry alipay")
        # elif userStatus == "口碑商家":
        #     sel.find_element_by_class_name("seller-entry koubei")
        # else:
        #     print("请确认您的身份是否输入正确！")
        # # if sel.find_element_by_class_name("") and userStatus == "合作伙伴":
        # #     sel.find_element_by_class_name("")
        # # else:
        # #     print("请确认您的身份是否输入正确！")
        # sel.save_screenshot('2.png')
        # print(sel.current_url)
        # # 跳转到我的支付宝页面
        # print('正在跳转页面....')
        # sel.get(MyZfb_Url)
        # sel.implicitly_wait(3)
        # sel.save_screenshot('3.png')
        # sel.implicitly_wait(3)
        # # 跳转至充值页面
        # sel.get(reCharge_Url)
        # sel.save_screenshot("4.png")
        # time.sleep(3)
        # # 选择网银方式充值
        # sel.get(sel.find_element_by_xpath("//li[@class='more']/a[@class='J_XBox']").get_attribute("href"))
        # # print(sel.find_element_by_xpath("//li[@class='more']/a[@class='J_XBox']").get_attribute("href"))
        # # ActionChains(sel).double_click(sel.find_element_by_xpath("//li[@class='more']/a[@class='J_XBox']")).perform()
        # # sel.get(e_bank_Url)
        # time.sleep(5)
        # sel.save_screenshot("5.png")
        # sel.implicitly_wait(3)
        # time.sleep(3)
        # # 选择银行
        # ChooseBank = input("请输入银行名称")
        # if ChooseBank == "中国工商银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-icbc105-1")).perform()
        # elif ChooseBank == "中国建设银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-ccb103-2")).perform()
        # elif ChooseBank == "中国农业银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-abc101-3")).perform()
        # elif ChooseBank == "中国邮政储蓄银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-psbcnucc103-4")).perform()
        #
        # elif ChooseBank == "交通银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-commnucc103-5")).perform()
        #
        # elif ChooseBank == "招商银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-cmb103-6")).perform()
        #
        # elif ChooseBank == "中国银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-boc102-7")).perform()
        #
        # elif ChooseBank == "中国光大银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-cebnucc103-8")).perform()
        #
        # elif ChooseBank == "中信银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-citicnucc103-9")).perform()
        #
        # elif ChooseBank == "浦发银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-spdbnucc103-10")).perform()
        #
        # elif ChooseBank == "中国民生银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-cmbcnucc103-11")).perform()
        #
        # elif ChooseBank == "兴业银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-cib102-12")).perform()
        #
        # elif ChooseBank == "平安银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-spabanknucc103-13")).perform()
        #
        # elif ChooseBank == "广发银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-gdbnucc103-14")).perform()
        #
        # elif ChooseBank == "上海农商银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-shrcbnucc103-15")).perform()
        #
        # elif ChooseBank == "上海银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-shbanknucc103-16")).perform()
        #
        # elif ChooseBank == "宁波银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-nbbanknucc103-17")).perform()
        #
        # elif ChooseBank == "杭州银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-hzcbnucc103-18")).perform()
        #
        # elif ChooseBank == "北京银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-bjbanknucc103-19")).perform()
        #
        # elif ChooseBank == "北京农商银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-bjrcbnucc103-20")).perform()
        #
        # elif ChooseBank == "富滇银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-fdbnucc103-21")).perform()
        #
        # elif ChooseBank == "温州银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-wzcbnucc103-22")).perform()
        #
        # elif ChooseBank == "成都银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-cdcbnucc103-23")).perform()
        #
        # elif ChooseBank == "常熟农商银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-csrcbnucc103-24")).perform()
        #
        # elif ChooseBank == "华夏银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-hxbanknucc103-25")).perform()
        #
        # elif ChooseBank == "南京银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-njcbnucc103-26")).perform()
        #
        # elif ChooseBank == "吴江农村商业银行":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-wjrcbnucc103-27")).perform()
        #
        # elif ChooseBank == "浙江农信（丰收卡）":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2c_ebank-zjnxnucc103-28")).perform()
        #
        # elif ChooseBank == "中国工商银行（企业）":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2b_ebank-icbcnucc104-29")).perform()
        #
        # elif ChooseBank == "中国建设银行（企业）":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2b_ebank-ccb104-30")).perform()
        #
        # elif ChooseBank == "中国农业银行（企业）":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2b_ebank-abcnucc104-31")).perform()
        #
        # elif ChooseBank == "招商银行（企业）":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2b_ebank-cmbnucc104-32")).perform()
        #
        # elif ChooseBank == "中国银行（企业）":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2b_ebank-bocnucc104-33")).perform()
        #
        # elif ChooseBank == "浦发银行（企业）":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2b_ebank-spdbnucc104-34")).perform()
        #
        # elif ChooseBank == "广发银行（企业）":
        #     ActionChains(sel).double_click(sel.find_element_by_id("J-b2b_ebank-gdbnucc104-35")).perform()
        #
        # else:
        #     print("没有该银行请重新选择")
        # sel.implicitly_wait(3)
        # # 选择银行完毕，点击下一步
        # ActionChains(sel).double_click(sel.find_element_by_xpath("//input[@class='ui-button ui-button-lblue']")).perform()
        # sel.implicitly_wait(3)
        # # 输入充值金额
        # moneyNumber = sel.find_element_by_id('J-depositAmount')
        # moneyNumber.clear()
        # number = input("请输入充值金额")
        # self.wait_input(moneyNumber, number)
        # sel.save_screenshot("6.png")
        # sel.implicitly_wait(3)
        # time.sleep(30)
        # # 登录到网上银行进行充值，开始显示页面
        # ActionChains(sel).double_click(sel.find_element_by_id("J-deposit-submit")).perform()
        # sel.save_screenshot("7.png")


        # 获取 cookies 并转换为字典类型
        cookies = sel.get_cookies()
        print(cookies)
        cookies_dict = {}
        for cookie in cookies:
            print(cookie)
            if 'name' in cookie and 'value' in cookie:
                cookies_dict[cookie['name']] = cookie['value']

        print(cookies_dict)

        return cookies_dict

        # 关闭浏览器
        sel.close()

    def set_cookies(self):
        '''将获取到的 cookies 加入 session'''
        c = self.get_cookies()
        print(c)
        self.session.cookies.update(c)
        print(self.session.cookies)

    def login_status(self):
        '''判断登录状态'''
        # 添加 cookies
        self.set_cookies()
        status = self.session.get(
            MyZfb_Url, timeout=5, allow_redirects=False).status_code
        print(status)
        if status == 200:
            return True
        else:
            return False

    def Recharge(self):
        '''
        点击充值并跳转至充值页面
        :return:
        '''
        status = self.login_status()
        if status:
            pass

    # 获取账单信息并存入数据库中
    def get_data(self):
        '''
        利用 bs4 库解析 html
        并抓取数据，
        数据以字典格式保存在列表里
        '''
        status = self.login_status()
        print(status)
        if status:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            sel = webdriver.Chrome('D:\Program Files\python\Scripts\chromedriver.exe',chrome_options=chrome_options)
            sel.get(Bill_Url)
            sel.implicitly_wait(3)
            time.sleep(2)
            try:
                sel.find_element_by_xpath('//*[@id="J-item-1"]')
            except:
                print("登录出错！")
                sel.close()
                return
            # db = DbHandle()
            # sql = "SELECT set_date FROM ali_pay_bill ORDER BY bid DESC LIMIT 1"
            # print(sql)
            # dateline = db.select_one(sql)
            # result = dateline['set_date']
            # result = result.replace('.', '')
            # result = result.replace('-', '')
            # result = result.replace(':', '')
            # dateline = int(result[2:])
            # print(dateline)
            global N
            for num in range(10):
                num = num + 1
                al_day_xpath = '//*[@id="J-item-' + str(num) + '"]/td[2]/p[1]'     # //*[@id="J-item-1"]/td[2]/p[1]    日期
                al_time_xpath = '//*[@id="J-item-' + str(num) + '"]/td[2]/p[2]'    # //*[@id="J-item-1"]/td[2]/p[2]    时刻
                al_way_xpath = '//*[@id="J-item-' + str(num) + '"]/td[3]/p[1]'     # //*[@id="J-item-1"]/td[3]/p[1]    方式
                al_payee_xpath = '//*[@id="J-item-' + str(num) + '"]/td[3]/p[2]'   # //*[@id="J-item-1"]/td[3]/p[2]/span 收款人
                al_snum_xpath = '//*[@id="J-tradeNo-' + str(num) + '"]'            # //*[@id="J-tradeNo-1"] 号#.get_attribute("title")
                al_figure_xpath = '//*[@id="J-item-' + str(num) + '"]/td[4]/span'  # //*[@id="J-item-1"]/td[4]/span    金额
                al_status_xpath = '//*[@id="J-item-' + str(num) + '"]/td[6]/p[1]'  # //*[@id="J-item-1"]/td[6]/p[1]    交易状态

                al_time = sel.find_element_by_xpath(al_time_xpath).text
                al_way = sel.find_element_by_xpath(al_way_xpath).text
                al_payee = sel.find_element_by_xpath(al_payee_xpath).text
                al_snum = sel.find_element_by_xpath(al_snum_xpath).text
                al_figure = sel.find_element_by_xpath(al_figure_xpath).text
                al_status = sel.find_element_by_xpath(al_status_xpath).text
                al_day = al_snum[:7]
                print(str(N) + '.' + '日期' + ':' + al_day + '\t时间' + ':' + al_time + '\t方式' + ':' + al_way + '\t收款人' + ':' + al_payee + '\t流水号' + ':' + al_snum + '\t金额' + ':' + al_figure + '\t交易状态' + ':' + al_status)
                N = N +1
                # single_data = self.handle_text(al_day, al_time, al_way, al_payee, al_snum, al_figure, al_status)
                # print(single_data)
                # if (single_data['set_time'] <= dateline):
                #     break
                # sql = "INSERT INTO ali_pay_bill (set_date, \
                #                other, amount, sign,statu,way,code) \
                #                VALUES ('%s', '%s', %s, %s, %s, '%s', '%s' )" % \
                #       (single_data['set_date'], single_data['other'], single_data['amount'], \
                #        single_data['sign'], single_data['statu'], single_data['way'], single_data['code'])
                # print(sql)
                # db.update(sql)
            sel.close()

if __name__ == "__main__":

    test = Alipay_Bill_Info(HEADERS, USERNMAE, PASSWD)

    data = test.get_data()

# print(data)