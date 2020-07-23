# _*_ coding:utf-8 _*_
# 作者：Administrator
# 时间：2020/7/10 19:58
# 文件名：BasePage.py
# 开发工具：PyCharm
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):  # 这里要写成构造函数
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:  # 如果链式调用的时候加了返回值后还没有click方法，就添加类型
        # 这里做为一个参数传进来的，所以给的参数是一个元祖(By.XPATH, "//*[@text='%s']" % text)
        return self.driver.find_element(*kv)  # 要有返回值才可以链式调用，不然就没有click方法
        # *这里是把传进来的元祖拆分成两个参数传给self.driver.find_element方法。   *这里要进步验证  如果把上面的KV改带*会是怎么样

    def findByText(self, text):
        # return self.driver.find_element(By.XPATH, "//*[@text='%s'] " % text)
        return self.find((By.XPATH, "//*[@text='%s']" % text))
