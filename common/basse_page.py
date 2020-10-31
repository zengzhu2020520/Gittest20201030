import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common.logger import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def open_url(self, url):
        self.driver.get(url)

    def set_browner_max_windows(self):
        self.driver.maximize_window()

    # {'elemen_name': '用户输入框', 'locat_type': 'XPATH',
    #  'locate_value': '//input[@id="account"]', 'time_out': '2'}
    def find_elements(self, ele_infos):
        ele_locat_type = ele_infos['locat_type']
        ele_locate_value = ele_infos['locate_value']
        ele_time_out = ele_infos['time_out']
        if ele_locat_type == 'id':
            locat_type = By.ID
        elif ele_locat_type == 'xpath':
            locat_type = By.XPATH
        elif ele_locat_type == 'name':
            locat_type=By.NAME
        elif ele_locat_type == 'class':
            locat_type = By.CSS_SELECTOR
        element = WebDriverWait(self.driver, ele_time_out).until(lambda x: x.find_element(locat_type, ele_locate_value))
        if element:
            logger.log_info('元素%s定位成功' % element)
        return element

    def click(self, ele_infos):
        ele = self.find_elements(ele_infos)
        ele.click()
        logger.log_info('成功点击%s这个元素' % ele_infos['elemen_name'])

    def input(self, ele_info, conent):
        input_ele = self.find_elements(ele_info)
        input_ele.send_keys(conent)
        logger.log_info('%s输入成功' % ele_info['elemen_name'])
