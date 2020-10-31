import time
from selenium.webdriver.common.by import By
from element_info.login_page import LoginPage
from common.logger import logger


class MainPage:
    def __init__(self):
        # 把界面的控件元素作为属性
        loginpag = LoginPage()
        loginpag.input_username('test01')
        loginpag.input_password('newdream123')
        loginpag.click_login()
        self.driver = loginpag.driver
        self.company_name = self.driver.find_element(By.XPATH, "//h1[@id='companyname']")
        self.my_dipan = self.driver.find_element(By.XPATH, "//li[@data-id='my']")
        self.product = self.driver.find_element(By.XPATH, "//a[contains(@href,'/zentao/www/index.php?m=product')]")
        self.my_imfomation = self.driver.find_element(By.XPATH, "//span[@class='user-name']")

    def get_company_name(self):  # 方法就是控件的操作
        get_company_name = self.company_name.get_attribute('title')
        return get_company_name

    def goto_mydipan(self):  # 进入我的地盘
        self.my_dipan.click()
        logger.log_info('成功进入我的地盘')

    def goto_product(self):  # 进产品
        self.product.click()
        logger.log_info('成功进入产品界面')

    def get_myusername(self):
        self.my_imfomation.click()
        get_username = self.my_imfomation.text


if __name__ == '__main__':
    mainpage = MainPage()
    company_name = mainpage.get_company_name()
    print(company_name)
    mainpage.goto_product()
    time.sleep(3)
    print(mainpage.get_myusername())
    time.sleep(3)
    mainpage.goto_mydipan()
