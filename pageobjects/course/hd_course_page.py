# -*- coding=utf-8-*-
# @author:CHEN XIAO KAI
# @file:pure_video_course_page.py
# @time:2021/9/14 23:21
# @software:PyCharm

from tools.basepage import BasePage
from pagelocators.course.hd_course_page_locs import HdCoursePageLocs as loc
from tools.handle_logger import logger
import time
import os
# 使用键盘按键方法要导入下面的类
from selenium.webdriver.common.keys import Keys

class HdCoursePage(BasePage):
    def select_hd(self, id="90427"):
        """
        @param id:
        @return:
        """
        logger.info("hd课程查询")
        time.sleep(1)
        self.input_text(loc.loc_hd_video_select_id, "输入hd课程ID", id)
        self.webdriver_wait_clickable(loc.loc_hd_video_select_button, "点击查询按钮")
        self.click_element(loc.loc_hd_video_select_button, "点击查询按钮")
        time.sleep(1)
        text = self.get_text(loc.loc_hd_video_select_assert, "校验查询正确性")
        self.mouse_move_to_element(loc.loc_hd_video_select_id, "清除查询内容")
        self.webdriver_wait_clickable(loc.loc_hd_clear, "点击清除")
        self.click_element(loc.loc_hd_clear, "点击清除")
        return text

    def add_hd(self, name="hd课程", cover1="data\img_coures\\before_purchase_transverse.png", recommendation="推荐语", subscription="111", tag="tag", markdown="markdown"):
        """
        @param id:
        @return:
        """
        logger.info("hd课程新增")
        self.webdriver_wait_clickable(loc.loc_hd_add_button, "点击添加课程按钮")
        self.click_element(loc.loc_hd_add_button, "点击添加课程按钮")
        self.webdriver_wait_visibility(loc.loc_hd_add_name, "点击提交按钮")
        pwd = self.project_root_path()
        self.webdriver_wait_clickable(loc.loc_hd_add_name, "输入名称")
        self.input_text(loc.loc_hd_add_name, "输入名称", name)
        self.webdriver_wait_clickable(loc.loc_hd_add_class, "点击课程分类")
        self.click_element(loc.loc_hd_add_class, "点击课程分类")
        self.sleep(2)
        self.webdriver_wait_clickable(loc.loc_hd_add_class_4, "选择内部课程")
        self.click_element(loc.loc_hd_add_class_4, "选择内部课程")
        self.webdriver_wait_clickable(loc.loc_hd_add_form, "点击课程形式")
        self.click_element(loc.loc_hd_add_form, "点击课程形式")
        self.webdriver_wait_clickable(loc.loc_hd_add_form_2, "选择视频课程")
        self.click_element(loc.loc_hd_add_form_2, "选择视频课程")
        self.webdriver_wait_clickable(loc.loc_hd_add_type, "点击课程分类")
        self.click_element(loc.loc_hd_add_type, "点击课程分类")
        self.webdriver_wait_clickable(loc.loc_hd_add_type_2, "选择科学探索")
        self.click_element(loc.loc_hd_add_type_2, "选择科学探索")
        self.input_text(loc.loc_hd_add_cover1, "封面1", pwd+cover1)
        self.input_text(loc.loc_hd_add_recommendation, "推荐语", recommendation)
        self.input_text(loc.loc_hd_add_subscription, "基础订阅量", subscription)
        self.input_text(loc.loc_hd_add_tag, "标签", tag)
        el = self.find_element(loc.loc_hd_add_tag, "标签")
        el.send_keys(Keys.ENTER)
        self.click_element(loc.loc_hd_add_tab2, "点击tab2")
        self.input_text(loc.loc_hd_add_markdown, "输入markdown", markdown)
        self.click_element(loc.loc_hd_add_save, "保存按钮")
        # return text
