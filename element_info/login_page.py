import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.logger import logger
from common.basse_page import BasePage
from common import readExcel

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../driver/chromedriver.exe')
url = 'http://47.107.178.45/zentao/www/index.php?m=user&f=login'


# log_path = 'D:\\PycharmProjects\\PO_UI_Test_Framework\\common\\log_untls\\zengzhu.log'


class LoginPage(BasePage):
    def __init__(self, driver):
        # 把界面的控件元素作为属性
        super().__init__(driver)
        # self.username_inputbox = {'elemen_name': '用户输入框',
        #                           'locat_type': 'xpath',
        #                           'locate_value': '//input[@id="account"]',
        #                           'time_out': 2}
        # self.password_inputbox = {'elemen_name': '密码输入框',
        #                           'locat_type': 'xpath',
        #                           'locate_value': '//input[@name="password"]',
        #                           'time_out': 3}
        # self.login_button = {'elemen_name': '登录按钮',
        #                      'locat_type': 'xpath',
        #                      'locate_value': '//button[@id="submit"]',
        #                      'time_out': 4}
        ele_info = readExcel.read_excel(sheet_name='login_page')
        self.username_inputbox = ele_info['username_inputbox']
        self.password_inputbox = ele_info['password_inputbox']
        self.login_button = ele_info['login_button']

    def input_username(self, username):  # 方法就是控件的操作
        self.input(self.username_inputbox, username)
        logger.log_info('正确输入用户名%s' % str(username))

    def input_password(self, password):
        self.input(self.password_inputbox, password)
        logger.log_info('正确输入密码%s' % str(password))

    def click_login(self):
        self.click(self.login_button)
        logger.log_info('正确登录')


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page = LoginPage(driver)
    login_page.open_url(url)
    login_page.set_browner_max_windows()
    login_page.input_username('test02')
    login_page.input_password('newdream123')
    login_page.click_login()
