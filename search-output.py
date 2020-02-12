# coding=utf8

import os
import sys
import time
import unittest

sys.path.append(os.path.dirname(__file__))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.services.test.testcase_base import TestCaseBase


class Testcase(unittest.TestCase):

    def setUp(self):
        TestCaseBase.setUp()

        self.driver = webdriver.Chrome(
            executable_path='/YY/YY/projects/automation/study/uiat/core/common/../../core/services/engine/driver/chromedriver')

    def test_case(self):
        self.driver.get('https://www.baidu.com/s')

        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('测试')
        self.driver.find_element_by_id('su').click()
        time.sleep(5)
        assert self.driver.find_element_by_css_selector(
            'table.c-table.opr-toplist1-table>tbody:nth-child(1)>tr:nth-child(1)>td:nth-child(1)').text == "1科比遗体已安葬"
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.opr-recommends-merge-mask')))

        from functions import test_function
        test_function(x=1, y=2)

    def tearDown(self):
        self.driver.close()

        TestCaseBase.tearDown()


if __name__ == '__main__':
    unittest.main()
