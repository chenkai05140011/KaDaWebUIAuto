# -*- coding=utf-8-*-
# @author:chen kai
# @file:basepage.py
# @time:2021/7/30 0:26
# @software:PyCharm

"""
每个方法：要有日志输出,要有异常捕获，要有异常截图
"""
import os.path
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.action_chains import ActionChains

from tools.handle_logger import logger
from tools.handle_path import screenshot_path
from testdatas.global_data import GlobalData as GD


class BasePage:
    def __init__(self, driver: webdriver.Chrome, timeout=15):
        self.driver = driver
        self.timeout = timeout
        self.driver.maximize_window()
        self.ac = ActionChains(driver=self.driver)

    def find_element(self, loc, page_name_action):
        """
        函数功能:返回元素对象
        :param page_name_action:截图作用, 提供页面和动作的提示
        """
        by = loc[0]
        value = loc[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            try:
                if by == 'id':
                    element = self.driver.find_element(By.ID, value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element(By.CSS_SELECTOR, value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    logger.error('Not find the element')
                logger.info("元素  {} 可见并返回了元素对象".format(loc))
                return element
            # except NoSuchElementException as e:
            #     logger.error("NoSuchElementException %s " % e)
            #     self.get_img()  # 调用截图
            # else:
            #     logger.error('Please enter a valid type of targeting elements')

            # if all is True:
            #     ele = WebDriverWait(driver=self.driver, timeout=self.timeout).until(EC.visibility_of_all_elements_located(loc))
            #     logger.info("元素 {} 全部可见并返回了元素对象列表".format(loc))
            # else:
            #     # 调用的方法找到的话会返回元素本身
            #     ele = WebDriverWait(driver=self.driver, timeout=self.timeout).until(EC.visibility_of_element_located(loc))
            #     logger.info("元素 {} 可见并返回了元素对象".format(loc))
            #
            # return ele
            except:
                # 失败截图,异常详情写入日志,抛出异常
                logger.exception("等待元素{}出现失败".format(loc))
                # 失败截图-页面名字_行为名字_当前时间.png
                self._save_page_shot(page_name_action)
                raise

    def click_element(self, loc, page_name_action):
        """
        函数功能:获取元素并点击操作
        :param loc:
        :param page_name_action:
        :return:
        """
        ele = self.find_element(loc=loc, page_name_action=page_name_action)
        try:
            ele.click()
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("点击元素失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def input_text(self, loc, page_name_action, text):
        """
        函数功能:发送文本内容
        :param loc:
        :param page_name_action:
        :param text:
        :return:
        """
        ele = self.find_element(loc=loc, page_name_action=page_name_action)
        try:
            ele.send_keys(text)
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("元素输入失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def get_text(self, loc, page_name_action):
        """
        函数功能:获取元素对象文本
        :param loc:
        :param page_name_action:
        :return:
        """
        ele = self.find_element(loc, page_name_action)
        try:
            value = ele.text
            logger.info("获取元素：{}的文本值：{}".format(loc, value))

            return value
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("获取元素的文本值失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def get_attr(self, loc, page_name_action):
        """
        函数功能:获取元素属性
        :param loc:
        :param page_name_action:
        :return:
        """
        ele = self.find_element(loc, page_name_action)
        try:
            value = ele.get_attribute()
            logger.info("获取元素：{}的属性值：{}".format(loc, value))
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("获取元素的属性值失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def switch_to_iframe(self, iframe_loc, page_name_action):
        """
        函数功能:iframe切换
        EC.frame_to_be_available_and_switch_to_it：直接一步到位找到iframe并切换到iframe
        :param iframe_loc: iframe定位
        :param page_name_action: 页面操作说明
        :return:
        """
        try:
            WebDriverWait(driver=self.driver, timeout=self.timeout).until(EC.frame_to_be_available_and_switch_to_it(
                locator=iframe_loc))
            time.sleep(1)
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("切换到iframe失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def exit_iframe(self):
        """
        函数功能:退出iframe
        :return:
        """
        self.driver.switch_to.default_content()

    def current_window_handle(self):
        """获取当前窗口句柄"""
        return self.driver.current_window_handle

    def window_handles(self):
        """获取当前窗口句柄"""
        return self.driver.window_handles

    def switch_to_window(self, window_name):
        """切换至指定名称的窗口"""
        self.driver.switch_to.window(window_name)

    def switch_to_new_window(self, page_name_action):
        """
        函数功能:浏览器窗口切换到新打开的窗口
        :return:
        """
        current_window_name = self.current_window_handle()
        all_window_names = self.driver.window_handles
        try:
            for window_name in all_window_names:
                if window_name != current_window_name:
                    self.switch_to_window(window_name)
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("切换到窗口失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def input_upload_file(self, loc, file, page_name_action):
        """
        上传文件操作:selenium只支持input元素的上传，直接使用send_keys将文件绝对地址写入元素即可
        :param loc:上传按钮的定位位置
        :param file 要上的文件的绝对路径
        :param page_name_action:
        :return:
        """
        # 找到上传按钮并点击
        input_btn = self.find_element(loc=loc, page_name_action=page_name_action)
        try:
            input_btn.send_keys(file)
            time.sleep(1)
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("上传文件操作失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def upload_file(self, loc, file, page_name_action):
        """
        上传文件操作:非input元素的上传，使用pywinauto.keyboard模块的send_keys将文件绝对地址写入元素即可
        :param loc:上传按钮的定位规则
        :param file:
        :param page_name_action:
        :return:
        """
        # 点击上传文件
        self.mouse_left_click_element(loc=loc, page_name_action=page_name_action)
        try:
            time.sleep(1)
            # 上传文件
            logger.info("点击上传文件{}".format(file))
            send_keys(file)
            time.sleep(0.5)
            # 点击回车
            send_keys('{VK_RETURN}')
            time.sleep(0.5)
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("上传文件操作失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def autoit_upload_file(self, file_url, page_name_action):
        """
        函数功能：单个文件上传
        @param file_url: 文件在项目下的url
        """
        try:
            root_path = self.project_root_path()
            os.system(r"{}\tools\upload.exe {}".format(root_path, root_path + file_url))
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("上传文件操作失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def mouse_left_click_element(self, loc, page_name_action):
        """
        函数功能：获取元素并模拟单击鼠标左键
        :return:
        """
        ele = self.find_element(loc=loc, page_name_action=None)
        try:
            self.ac.click(on_element=ele).perform()
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("鼠标点击指定元素操作失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def mouse_move_to_element(self, loc, page_name_action):
        """
        函数功能：模拟鼠标移动到要定位的元素
        :param loc:
        :param page_name_action:
        :return:
        """
        ele = self.find_element(loc=loc, page_name_action=page_name_action)
        try:
            logger.info("鼠标移动到元素 {}".format(loc))
            self.ac.move_to_element(to_element=ele).perform()
            return self
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("鼠标移动到指定元素失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def mouse_move_to_element_and_click(self, loc, page_name_action):
        """
        函数功能:模拟鼠标移动到要定位的元素并点击
        :param loc:
        :param page_name_action:
        :return:
        """
        ele = self.find_element(loc=loc, page_name_action=page_name_action)
        try:
            logger.info("鼠标移动到元素 {} 并点击".format(loc))
            self.ac.move_to_element(to_element=ele).click(ele).perform()
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("鼠标移动到指定元素并点击操作失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def execute_script_with_element(self, script, loc, page_name_action):
        """
        函数功能：执行js命令,带元素对象
        @param loc:
        @param script: 点击：arguments[0].click();
        @param page_name_action:
        """
        ele = self.find_element(loc=loc, page_name_action=page_name_action)
        try:
            logger.info("执行js命令 {}.".format(script))
            self.driver.execute_script(script, ele)
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("执行js命令操作失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def execute_script(self, script, page_name_action):
        """
        函数功能：执行js命令，不带元素对象
        @param script: 滚动至底部："window.scrollTo(0,document.body.scrollHeight)"
        @param page_name_action:
        @return:
        """
        try:
            logger.info("执行js命令 {}.".format(script))
            self.driver.execute_script(script=script)
        except:
            # 失败截图,异常详情写入日志,抛出一场
            logger.exception("执行js命令操作失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def _save_page_shot(self, page_name_action):
        current_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        filename = "{}_{}.png".format(page_name_action, current_time)
        filepath = os.path.join(screenshot_path, filename)
        self.driver.save_screenshot(filename=filepath)
        # 添加截图到allure报告中
        with open(filepath, 'rb') as fp:
            file = fp.read()
        allure.attach(body=file, name=filename, attachment_type=allure.attachment_type.PNG)
        logger.info("当前页面的截图存储在：{}".format(filepath))

    def webdriver_wait_visibility(self, locator, page_name_action):
        """显示等待判断是否可见"""
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of(self.find_element(locator, page_name_action)))
            logger.info("等待元素可见：{}, 最长等待时间: {}秒.".format(locator, self.timeout))
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("等待元素{}可见失败".format(locator))
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def webdriver_wait_clickable(self, locator, page_name_action):
        """显示等待判断是否可见并可用"""
        by = locator[0]
        value = locator[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            try:
                if by == 'id':
                    element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.ID, value)))
                elif by == 'name':
                    element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.NAME, value)))
                elif by == 'class':
                    element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, value)))
                elif by == 'tag':
                    element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.TAG_NAME, value)))
                elif by == 'link':
                    element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.LINK_TEXT, value)))
                elif by == 'plink':
                    element = WebDriverWait(self.driver, self.timeout).until(
                        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, value)))
                elif by == 'css':
                    element = WebDriverWait(self.driver, self.timeout).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, value)))
                elif by == 'xpath':
                    element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH, value)))
                else:
                    logger.error('Not find the element')
                logger.info("元素 {} 可见并可用，返回了元素对象".format(locator))
                return element
            except:
                # 失败截图,异常详情写入日志,抛出异常
                logger.exception("等待元素{}出现并可用失败".format(locator))
                # 失败截图-页面名字_行为名字_当前时间.png
                self._save_page_shot(page_name_action)
                raise

    def is_text_in_element(self, locator, text, page_name_action):
        """
        函数功能：检查给定文本是否存在于元素中
        @param locator:
        @param text:
        @param page_name_action:
        @return: true or false
        """
        try:
            result = WebDriverWait(self.driver, self.timeout).until(EC.text_to_be_present_in_element(locator, text))
            logger.info("指定文本：{}是否存在于元素中： ".format(text, result))
            return result
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("元素未加载出来")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    def is_alert_present(self, page_name_action):
        """
        函数功能：弹出框是否存在，如果是，切换到alert，否则返回false
        @param page_name_action:
        @return:
        """
        try:
            result = WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            logger.info("alert弹框存在，切换到alert")
            return result
        except:
            # 失败截图,异常详情写入日志,抛出异常
            logger.exception("切换到alert弹框失败")
            # 失败截图-页面名字_行为名字_当前时间.png
            self._save_page_shot(page_name_action)
            raise

    @staticmethod
    def sleep(seconds):
        """强制等待"""
        time.sleep(seconds)
        logger.info('Sleep for %d seconds' % seconds)

    def open_url(self, url):
        self.driver.get(url)

    def forward(self):
        """浏览器前进"""
        self.driver.forward()
        logger.info("Click forward on current page.")

    def back(self):
        """浏览器后退"""
        self.driver.back()
        logger.info("Click back on current page.")

    def close(self):
        """关闭当前浏览器"""
        self.driver.close()
        logger.info("Closes the current window")

    def wait(self, seconds):
        """隐式等待"""
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    @staticmethod
    def project_root_path():
        """
        获取当前项目根路径
        @return:
        """
        project_path = os.path.abspath(os.path.dirname(__file__)).split("tools")[0].replace("/", "\\")
        logger.info("当前项目根路径：{}".format(project_path))
        return project_path


if __name__ == '__main__':
    print("== =" + os.path.abspath(os.path.dirname(__file__)).split("tools")[0].replace("/", "\\"))

if __name__ == '__main__':
    # 上下文管理器
    with webdriver.Chrome() as driver_gc:
        driver_gc.get(GD.login_url)
        # driver_gc.maximize_window()
        bp = BasePage(driver=driver_gc)
        # 用户名输入框
        user_input = (By.XPATH, '//input[@placeholder="邮箱/账号/手机号"]')
        bp.input_text(loc=user_input, page_name_action="登录页面_输入账号", text=GD.stu_account[0])
        # 密码输入框
        passwd_input = (By.XPATH, '//input[@placeholder="密码"]')
        bp.input_text(loc=passwd_input, page_name_action="登录页面_输入密码", text=GD.stu_account[1])
        # 登录按钮
        login_button = (By.XPATH, '//div[contains(@class,"pt-login")]//a[text()="登录"]')
        bp.click_element(loc=login_button, page_name_action="登录页面_点击登录")
        muke_loc = (By.XPATH, '//a[text()="精品慕课"]')
        bp.mouse_left_click_element(loc=muke_loc, page_name_action="主页-慕课网")
        time.sleep(20)
