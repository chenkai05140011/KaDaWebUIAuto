# -*- coding=utf-8-*-
# @author:CHEN XIAO KAI
# @file:pure_video_course_page.py
# @time:2021/7/27 23:21
# @software:PyCharm

from tools.basepage import BasePage
from pagelocators.course.Pure_video_course_page_locs import PureVideoCoursePageLocs as loc
from pagelocators.index_page_locs import MenuCourse as mloc
from tools.handle_logger import logger
import time
import os
# 使用键盘按键方法要导入下面的类
from selenium.webdriver.common.keys import Keys


class PureVideoCoursePage(BasePage):
    # 导航栏切换
    logger.info("课堂页面_根据传入的名字切换导航栏")

    def menu_pure_video(self):
        """

        """
        self.click_element(mloc.loc_menu_content, "点击内容管理")
        self.click_element(mloc.loc_menu_pure_video, "视频课程管理")

    def select_pure_video(self, name="", id="90333", input_text="", state=""):
        """
        @param name:
        @param id:
        @param input_text:
        @param state:
        @return:
        """
        logger.info("互动课程查询")
        self.sleep(1)
        self.input_text(loc.loc_pure_video_select_name, "输入课程名称", name)
        self.input_text(loc.loc_pure_video_select_id, "输入课程ID", id)
        self.click_element(loc.loc_pure_video_select_input_text, "点击付费类型")
        self.webdriver_wait_visibility(loc.loc_pure_video_select_drop, "点击提交按钮")
        if input_text == 1:
            self.click_element(loc.loc_pure_video_select_drop_1, "全部")
        elif input_text == 2:
            self.click_element(loc.loc_pure_video_select_drop_2, "付费")
        elif input_text == 3:
            self.click_element(loc.loc_pure_video_select_drop_3, "免费")
        else:
            print("请输入正确的类型")
        self.click_element(loc.loc_pure_video_select_state, "课程状态")
        self.webdriver_wait_visibility(loc.loc_pure_video_select_drop, "点击提交按钮")
        if state == 1:
            self.click_element(loc.loc_pure_video_select_drop_1, "全部")
        elif state == 2:
            self.click_element(loc.loc_pure_video_select_drop_2, "已上架")
        elif state == 3:
            self.click_element(loc.loc_pure_video_select_drop_3, "已下架")
        elif state == 4:
            self.click_element(loc.loc_pure_video_select_drop_4, "待上架")
        else:
            print("请输入正确的input_text")
        self.click_element(loc.loc_pure_video_select_button, "点击查询按钮")
        self.sleep(1)
        text = self.get_text(loc.loc_pure_video_select_assert, "校验查询正确性")
        self.mouse_move_to_element(loc.loc_pure_video_select_id, "清除查询内容")
        self.click_element(loc.loc_pure_video_add_name_clear, "点击清除")
        return text

    def add_pure_video(self, name="纯视频", update=1, version="5.5.20"):
        """

        @param name:
        @param update:
        @param version:
        """
        self.click_element(loc.loc_pure_video_add_button, "点击新建课程")
        self.sleep(1)
        self.input_text(loc.loc_pure_video_add_name, "输入课程名称", name)
        # , sj_bj = "E:\kada_gs\kada_ui\img_coures\sjbj.png", ipad_bj = "E:\kada_gs\kada_ui\img_coures\ipadjb.png"
        # self.click(self.loc_pure_video_add_sj_bj)
        # # 上传文件
        # self.sleep(1)
        # os.system(r"E:\kada_gs\kada_ui\common\upload111.exe %s" % sj_bj)
        # self.click(self.loc_pure_video_add_ipad_bj)
        # # 上传文件
        # self.sleep(1)
        # os.system(r"E:\kada_gs\kada_ui\common\upload111.exe %s" % ipad_bj)
        self.click_element(loc.loc_pure_video_add_update, "点击是否提示更新")
        self.webdriver_wait_visibility(loc.loc_pure_video_add_drop, "点击提交按钮")
        self.sleep(1)
        if update == 1:
            self.click_element(loc.loc_pure_video_add_drop_1, "点击更新")
            self.webdriver_wait_visibility(loc.loc_pure_video_add_version, "点击提交按钮")
            self.input_text(loc.loc_pure_video_add_version, "输入课程版本", version)
        elif update == 2:
            self.click_element(loc.loc_pure_video_add_drop_2, "点击不更新")
        else:
            print("请输入正确的type")
        self.click_element(loc.loc_pure_video_add_button_y, "点击提交按钮")

    def edit_pure_video(self, name="edit", unit_name="单元二"):
        self.click_element(loc.loc_pure_video_edit, "点击课程编辑按钮")
        self.mouse_move_to_element(loc.loc_pure_video_add_name, "定位课程名称")
        self.click_element(loc.loc_pure_video_add_name_clear, "清除课程名称")
        self.input_text(loc.loc_pure_video_add_name, "修改课程名称", name)
        self.click_element(loc.loc_pure_video_add_update, "点击是否提示更新")
        self.webdriver_wait_visibility(loc.loc_pure_video_add_drop, "点击提交按钮")
        # if update == 1:
        #     self.click(self.loc_pure_video_add_drop_1)
        #     self.webdriver_wait_visibility(seconds=10, locator=self.loc_pure_video_add_version)
        #     self.type(self.loc_pure_video_add_version, version)
        # elif update == 2:
        #     self.click(self.loc_pure_video_add_drop_2)
        # else:
        #     print("请输入正确的type")
        self.click_element(loc.loc_pure_video_add_unit, "点击新增单元按钮")
        self.input_text(loc.loc_pure_video_add_unit_name, "输入单元名称", unit_name)
        self.click_element(loc.loc_pure_video_add_unit_y, "点击确定按钮")
        self.click_element(loc.loc_pure_video_add_button_y, "点击提交按钮")

    def add_lesson_pure_video(self, name="课节", mp4="data\mp4\ms.mp4", number="KDBQ100033"):
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson, "点击提交按钮")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_add, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson_add, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson_unit, "点击提交按钮")
        self.webdriver_wait_visibility(loc.loc_pure_video_select_drop, "点击提交按钮")
        self.click_element(loc.loc_pure_video_select_drop_1, "点击提交按钮")
        self.sleep(1)
        self.click_element(loc.loc_pure_video_lesson_sort, "点击提交按钮")
        self.webdriver_wait_visibility(loc.loc_pure_video_select_drop, "点击提交按钮")
        self.click_element(loc.loc_pure_video_select_drop_1, "点击提交按钮")
        self.input_text(loc.loc_pure_video_lesson_name, "点击提交按钮", name)
        self.click_element(loc.loc_pure_video_lesson_try_to_learn, "点击提交按钮")
        self.webdriver_wait_visibility(loc.loc_pure_video_select_drop_1, "点击提交按钮")
        self.click_element(loc.loc_pure_video_select_drop_2, "点击提交按钮")
        self.sleep(1)
        self.input_text(loc.loc_pure_video_lesson_number, "点击提交按钮", number)
        self.sleep(1)
        self.click_element(loc.loc_pure_video_lesson_file, "点击提交按钮")
        self.sleep(1)
        pwd = self.project_root_path()
        os.system(r"{}\tools\upload.exe {}".format(pwd, pwd+mp4))
        self.webdriver_wait_visibility(loc.loc_pure_video_lesson_file_assert, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson_y, "点击提交按钮")

    def learn_lesson_pure_video(self):
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson, "点击提交按钮")
        text = self.get_text(loc.loc_pure_video_lesson_learn_text, "点击提交按钮")
        self.sleep(1)
        self.click_element(loc.loc_pure_video_lesson_learn_text, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson_learn_yes, "点击提交按钮")
        return text

    def edit_lesson_pure_video(self, name="课节编辑"):
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson, "点击提交按钮")
        self.webdriver_wait_visibility(loc.loc_pure_video_lesson_learn, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson_edit, "点击提交按钮")
        self.mouse_move_to_element(loc.loc_pure_video_lesson_name, "点击提交按钮")
        self.click_element(loc.loc_pure_video_add_name_clear, "点击提交按钮")
        self.input_text(loc.loc_pure_video_lesson_name, "点击提交按钮", name)
        self.click_element(loc.loc_pure_video_lesson_y, "点击提交按钮")

    def online_lesson_pure_video(self):
        self.sleep(2)
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson, "点击提交按钮")
        self.sleep(1)
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_online, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson_online, "点击提交按钮")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_online_y, "点击提交按钮")
        self.click_element(loc.loc_pure_video_lesson_online_y, "点击提交按钮")
        self.sleep(1)
        name = self.get_text(loc.loc_pure_video_lesson_online_1, "点击提交按钮")
        return name

    def yy_config_lesson_pure_video(self, subscription="1000", time="5", fm_1="data\img_coures\m_1.png", fm_2="data\img_coures\m_2.png", fm_3="data\img_coures\gmsb.png", fm_4="data\img_coures\m_4.png", fm_5="data\img_coures\m_5.png", fm_6="data\img_coures\m_6.png",
                                    price_1="0.1", price_2="0.1", price_3="0.1", recommendation="好好学习，天天向上", tag="v2.3", map_1="data\img_coures\lbt01.png"):
        self.click_element(loc.loc_pure_video_yy_config, "点击提交按钮")
        self.input_text(loc.loc_pure_video_yy_config_subscription, "点击提交按钮", subscription)
        self.input_text(loc.loc_pure_video_yy_config_time, "点击提交按钮", time)
        pwd = self.project_root_path()
        self.input_text(loc.loc_pure_video_yy_config_fm_1, "点击提交按钮", pwd+fm_1)
        self.input_text(loc.loc_pure_video_yy_config_fm_2, "点击提交按钮", pwd+fm_2)
        self.input_text(loc.loc_pure_video_yy_config_fm_3, "点击提交按钮", pwd+fm_3)
        self.input_text(loc.loc_pure_video_yy_config_fm_4, "点击提交按钮", pwd+fm_4)
        self.input_text(loc.loc_pure_video_yy_config_fm_5, "点击提交按钮", pwd+fm_5)
        self.input_text(loc.loc_pure_video_yy_config_price_1, "点击提交按钮", price_1)
        self.input_text(loc.loc_pure_video_yy_config_price_2, "点击提交按钮", price_2)
        self.input_text(loc.loc_pure_video_yy_config_price_3, "点击提交按钮", price_3)
        self.input_text(loc.loc_pure_video_yy_config_recommendation, "点击提交按钮", recommendation)
        self.input_text(loc.loc_pure_video_yy_config_tag, "点击提交按钮", tag)
        el = self.find_element(loc.loc_pure_video_yy_config_tag, "点击提交按钮")
        el.send_keys(Keys.ENTER)
        self.execute_script("var q=document.getElementById('app-main').scrollTop=1000", "点击提交按钮")
        # self.drag_and_drop(self.loc_pure_video_yy_config_recommendation, self.loc_pure_video_yy_config_ct_1)
        self.click_element(loc.loc_pure_video_yy_config_map_1, "点击提交按钮")
        self.sleep(1)
        os.system(r"{}\tools\upload.exe {}".format(pwd, pwd+map_1))
        self.sleep(2)
        self.click_element(loc.loc_pure_video_yy_config_ct, "点击提交按钮")
        self.sleep(1)
        os.system(r"{}\tools\upload.exe {}".format(pwd, pwd+fm_6))
        self.sleep(2)
        self.click_element(loc.loc_pure_video_yy_config_y, "点击提交按钮")
        self.sleep(1)
        text = self.get_text(loc.loc_pure_video_lesson_online_1, "点击提交按钮")
        return text

    def copy_lesson_pure_video(self):
        self.webdriver_wait_clickable(loc.loc_pure_video_copy_address, "点击提交按钮")
        self.click_element(loc.loc_pure_video_copy_address, "点击提交按钮")
        self.webdriver_wait_visibility(loc.loc_pure_video_lesson_copy_text, "点击提交按钮")
        text = self.get_text(loc.loc_pure_video_lesson_copy_text, "点击提交按钮")
        return text

    def online_pure_video(self):
        self.sleep(2)
        self.webdriver_wait_clickable(loc.loc_pure_video_online, "点击提交按钮")
        self.click_element(loc.loc_pure_video_online, "点击提交按钮")
        self.webdriver_wait_clickable(loc.loc_pure_video_online_y, "点击提交按钮")
        self.click_element(loc.loc_pure_video_online_y, "点击提交按钮")
        name = self.get_text(loc.loc_pure_video_lesson_online_1, "点击提交按钮")
        return name

    # 课节批量操作——批量上架
    def lesson_batch_online_pure_video(self):
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson, "点击课节配置")
        self.click_element(loc.loc_pure_video_lesson, "点击课节配置")
        self.sleep(1)
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch, "选择全部课节")
        self.click_element(loc.loc_pure_video_lesson_batch, "选择全部课节")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_online, "点击批量上架")
        self.click_element(loc.loc_pure_video_lesson_batch_online, "点击批量上架")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_y_1, "点击确定")
        self.click_element(loc.loc_pure_video_lesson_batch_y_1, "点击确定")
        self.webdriver_wait_visibility(loc.loc_pure_video_lesson_batch_assert, "验证上架成功")
        name = self.get_text(loc.loc_pure_video_lesson_batch_assert, "验证上架成功")
        return name

    # 课节批量操作——批量下架
    def lesson_batch_off_pure_video(self):
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson, "点击课节配置")
        self.click_element(loc.loc_pure_video_lesson, "点击课节配置")
        self.sleep(1)
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch, "选择全部课节")
        self.click_element(loc.loc_pure_video_lesson_batch, "选择全部课节")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_off, "点击批量下架")
        self.click_element(loc.loc_pure_video_lesson_batch_off, "点击批量下架")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_y_1, "点击确定")
        self.click_element(loc.loc_pure_video_lesson_batch_y_1, "点击确定")
        self.webdriver_wait_visibility(loc.loc_pure_video_lesson_batch_assert, "验证下架成功")
        name = self.get_text(loc.loc_pure_video_lesson_batch_assert, "验证下架成功")
        return name

    # 课节批量操作——批量设置单元
    def lesson_batch_unit_pure_video(self):
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson, "点击课节配置")
        self.click_element(loc.loc_pure_video_lesson, "点击课节配置")
        self.sleep(1)
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch, "选择全部课节")
        self.click_element(loc.loc_pure_video_lesson_batch, "选择全部课节")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_unit, "点击批量设置单元")
        self.click_element(loc.loc_pure_video_lesson_batch_unit, "点击批量设置单元")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_unit_1, "点击课节所属单元")
        self.click_element(loc.loc_pure_video_lesson_batch_unit_1, "点击课节所属单元")
        self.webdriver_wait_clickable(loc.loc_pure_video_select_drop_1, "下拉框选择第一个")
        self.click_element(loc.loc_pure_video_select_drop_1, "下拉框选择第一个")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_unit_2, "点击课节在单元内的顺序")
        self.click_element(loc.loc_pure_video_lesson_batch_unit_2, "点击课节在单元内的顺序")
        self.sleep(1)
        self.webdriver_wait_clickable(loc.loc_pure_video_select_drop_1, "下拉框选择第一个")
        self.click_element(loc.loc_pure_video_select_drop_1, "下拉框选择第一个")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_y_3, "点击确定")
        self.click_element(loc.loc_pure_video_lesson_batch_y_3, "点击确定")
        self.webdriver_wait_visibility(loc.loc_pure_video_lesson_batch_assert, "验证批量设置单元成功")
        name = self.get_text(loc.loc_pure_video_lesson_batch_assert, "验证批量设置单元成功")
        return name

    # 课节批量操作——批量设置单元
    def lesson_batch_number_pure_video(self, number_input='KDBQ100033'):
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson, "点击课节配置")
        self.click_element(loc.loc_pure_video_lesson, "点击课节配置")
        self.sleep(1)
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch, "选择全部课节")
        self.click_element(loc.loc_pure_video_lesson_batch, "选择全部课节")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_number, "批量设置版权号")
        self.click_element(loc.loc_pure_video_lesson_batch_number, "批量设置版权号")
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_number_input, "版权信息")
        self.input_text(loc.loc_pure_video_lesson_batch_number_input, "输入版权信息", number_input)
        el = self.find_element(loc.loc_pure_video_lesson_batch_number_input, "点击提交按钮")
        el.send_keys(Keys.ENTER)
        self.sleep(1)
        self.webdriver_wait_clickable(loc.loc_pure_video_lesson_batch_y_2, "点击确定")
        self.click_element(loc.loc_pure_video_lesson_batch_y_2, "点击确定")
        self.webdriver_wait_visibility(loc.loc_pure_video_lesson_batch_assert, "验证批量设置版权号成功")
        name = self.get_text(loc.loc_pure_video_lesson_batch_assert, "验证批量设置版权号成功")
        return name


    @staticmethod
    def update_loc_by_data(loc, data):
        """
        :param loc:定位元素的字典, 如input_homework_btn
        :param data:要替换的参数
        :return:
        """
        loc[1] = loc[1].format(data)

        return loc



        




