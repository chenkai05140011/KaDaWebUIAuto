import time

from tools.basepage import BasePage

from pagelocators.mixcourse.mix_lesson_manage_page_locs import MixLessonManagePageLocs as mploc

project_root_path = BasePage.project_root_path()


class MixLessonManagePage(BasePage):

    def add_mix_unit(self, unit_name, unit_order):
        """
        新增互动单元
        @param unit_name: 单元名称
        @param unit_order: 单元序号
        """
        self.webdriver_wait_clickable(mploc.loc__mix_unit, "等待互动单元管理按钮可用")
        # 偶现元素不可点击异常，多用例执行时alert遮住按钮，故用js点击
        self.execute_script_with_element("arguments[0].click();", mploc.loc__mix_unit, "点击互动单元管理按钮")
        # self.click_element(mploc.loc__mix_unit, "点击互动单元管理")
        self.webdriver_wait_clickable(mploc.loc_mix_unit_add, "等待新增互动单元按钮可用")
        self.execute_script_with_element("arguments[0].click();", mploc.loc_mix_unit_add, "新增互动单元")
        self.input_text(mploc.loc_unit_name, "输入互动单元名称", unit_name)
        self.input_text(mploc.loc_unit_sort, "输入互动单元序号", unit_order)
        self.click_element(mploc.loc_unit_save, "点击保存按钮")
        self.webdriver_wait_visibility(mploc.loc_unit_list_first, "等待第1条数据的单元名称可见")
        actual_text = self.get_text(mploc.loc_unit_list_first, "获取单元列表-第1条数据的单元名称")
        return actual_text

    def add_mix_lesson(self, lesson_name, file_cover, lesson_type, copyright):
        """
        新增互动课节
        @param lesson_name: 课节名称
        @param file_cover: 课节封面
        @param lesson_type: 课节类型, 1是混编课节，2是视频互动课节
        @param copyright: 版权号
        """
        self.add_mix_unit("单元" + time.strftime('%M%S', time.localtime(time.time())), "序号" + time.strftime('%M%S', time.localtime(time.time())))
        # 返回互动课节列表页
        self.back()
        self.webdriver_wait_clickable(mploc.loc_add_mix_lesson, "等待新增互动课节按钮可用")
        # 偶现元素不可点击异常，多用例执行时alert遮住按钮，故用js点击
        self.execute_script_with_element("arguments[0].click();", mploc.loc_add_mix_lesson, "点击新增互动课节按钮")
        self.input_text(mploc.loc_lesson_name, "输入课节名称", lesson_name)
        self.upload_file(mploc.loc_lesson_cover, project_root_path + file_cover, "上传文件")
        self.click_element(mploc.loc_lesson_unit, "点击课程单元")
        self.webdriver_wait_clickable(mploc.loc_lesson_unit_last, "等待最后1选项钮可用")
        # 单元数多时，li标签隐藏元素点击不到，使用js点击
        self.execute_script_with_element("arguments[0].click();", mploc.loc_lesson_unit_last, "点击课程单元-最后1个选项")
        # 偶现ElementClickInterceptedException，尝试js点击
        self.execute_script_with_element("arguments[0].click();", mploc.loc_lesson_is_try, "打开试学")
        self.click_element(mploc.loc_lesson_add_teacher, "点击是否引导添加老师")
        self.webdriver_wait_clickable(mploc.loc_lesson_add_teacher_tips, "等待设置提示引导可用")
        self.click_element(mploc.loc_lesson_add_teacher_tips, "设置提示引导")
        self.click_element(mploc.loc_lesson_type, "点击课节类型")
        if lesson_type == 1:
            self.click_element(mploc.loc_lesson_type_blend, "设置混编课节")
        elif lesson_type == 2:
            self.click_element(mploc.loc_lesson_mix_video, "设置视频互动课节")
        self.input_text(mploc.loc_lesson_copyright, "输入版权号", copyright)
        self.click_element(mploc.loc_lesson_save, "提交保存")
        self.webdriver_wait_visibility(mploc.loc_lesson_save_success, "等待课节列表alert提示信息可见")
        actual_text = self.get_text(mploc.loc_lesson_save_success, "获取课节列表alert提示信息")
        return actual_text

    def add_upload_video(self, video_file="data\imp4\source_video.mp4"):
        """
        互动课节文件管理-上传视频文件
        @param video_file:视频文件url
        @return:
        """
        self.webdriver_wait_clickable(mploc.loc_lesson_file_manage, "等待互动课节文件管理按钮可用")
        # 偶现元素不可点击异常，多用例执行时alert遮住按钮，故用js点击
        self.execute_script_with_element("arguments[0].click();", mploc.loc_lesson_file_manage, "点击互动课节文件管理")
        # 浏览器窗口切换到新打开的窗口
        self.switch_to_new_window("浏览器窗口切换到新打开的窗口")
        self.webdriver_wait_clickable(mploc.loc_lesson_select_file, "等待上传文件入口出现")
        self.upload_file(mploc.loc_lesson_select_file, project_root_path + video_file, "上传文件")
        # 偶现元素不可点击，这样增加稳定性
        self.sleep(0.5)
        self.webdriver_wait_clickable(mploc.loc_lesson_start_upload, "等待开始上传按钮可用")
        self.click_element(mploc.loc_lesson_start_upload, "点击开始上传按钮")
        self.webdriver_wait_visibility(mploc.loc_lesson_upload_status, "等待上传状态可见")
        actual_text = self.get_text(mploc.loc_lesson_upload_status, "获取上传状态")
        # 因@pytest.fixture(scope="package")，需做用例衔接，返回到课程列表页
        self.switch_to_window(self.window_handles()[0])
        return actual_text

    def click_edit_button(self):
        """
        互动课节列表-点击最后1个课节
        """
        self.click_element(mploc.loc_lesson_list_edit_last, "点击课节列最后1个课节-编辑按钮")

    def add_mix_source(self, source_type):
        """
        新增互动环节
        @param source_type: 1是纯视频2.0    2是视频互动课   3是录音题    4是语音AI评测题   5是选择题   6是拼图题
                            7是拖拽题   8是拍摄题   9是KaDa协议
        @return:
        """
        # 新增单元、课节
        self.add_mix_lesson("课节" + time.strftime('%M%S', time.localtime(time.time())), "data\img_coures\lesson_cover.png", 1, "KDBQ100033")
        self.click_edit_button()
        self.webdriver_wait_clickable(mploc.loc_source_add, "等待新增环节按钮可用")
        self.click_element(mploc.loc_source_add, "点击新增环节按钮")
        self.click_element(mploc.loc_source_name, "点击环节名称")
        # 在元素可见并可用情况下，偶现点击元素失败，这里增加稳定性
        self.sleep(1)

        if source_type == 1:
            self.webdriver_wait_clickable(mploc.loc_source_name_look, "等待环节名称-看一看")
            self.click_element(mploc.loc_source_name_look, "点击环节名称-看一看")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            # 在元素可见并可用情况下，偶现点击元素失败，这里增加稳定性
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_video, "等待环节类型-纯视频2.0选项可用")
            self.click_element(mploc.loc_source_type_video, "点击环节类型-纯视频2.0")
        elif source_type == 2:
            self.webdriver_wait_clickable(mploc.loc_source_name_look, "等待环节名称-看一看")
            self.click_element(mploc.loc_source_name_look, "点击环节名称-看一看")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_mix_video, "等待环节类型-视频互动课选项可用")
            self.click_element(mploc.loc_source_type_mix_video, "点击环节类型-视频互动课")
        elif source_type == 3:
            self.webdriver_wait_clickable(mploc.loc_source_name_talk, "等待环节名称-说一说")
            self.click_element(mploc.loc_source_name_talk, "点击环节名称-说一说")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_record, "等待环节类型-录音题选项可用")
            self.click_element(mploc.loc_source_type_record, "点击环节类型-录音题")
        elif source_type == 4:
            self.webdriver_wait_clickable(mploc.loc_source_name_talk, "等待环节名称-说一说")
            self.click_element(mploc.loc_source_name_talk, "点击环节名称-说一说")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_ai_record, "等待环节类型-语音AI评测题选项可用")
            self.click_element(mploc.loc_source_type_ai_record, "点击环节类型-语音AI评测题")
        elif source_type == 5:
            self.webdriver_wait_clickable(mploc.loc_source_name_practice, "等待环节名称-练一练")
            self.click_element(mploc.loc_source_name_practice, "点击环节名称-练一练")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_select, "等待环节类型-选择题选项可用")
            self.click_element(mploc.loc_source_type_select, "点击环节类型-选择题")
        elif source_type == 6:
            self.webdriver_wait_clickable(mploc.loc_source_name_play, "等待环节名称-玩一玩")
            self.click_element(mploc.loc_source_name_play, "点击环节名称-玩一玩")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_jigsaw_puzzle, "等待环节类型-拼图题选项可用")
            self.click_element(mploc.loc_source_type_jigsaw_puzzle, "点击环节类型-拼图题")
        elif source_type == 7:
            self.webdriver_wait_clickable(mploc.loc_source_name_play, "等待环节名称-玩一玩")
            self.click_element(mploc.loc_source_name_play, "点击环节名称-玩一玩")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_drag, "等待环节类型-拖拽题选项可用")
            self.click_element(mploc.loc_source_type_drag, "点击环节类型-拖拽题")

        elif source_type == 8:
            self.webdriver_wait_clickable(mploc.loc_source_name_play, "等待环节名称-玩一玩")
            self.click_element(mploc.loc_source_name_play, "点击环节名称-玩一玩")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_video_record, "等待环节类型-拍摄题选项可用")
            self.click_element(mploc.loc_source_type_video_record, "点击环节类型-拍摄题")
        elif source_type == 9:
            self.webdriver_wait_clickable(mploc.loc_source_name_look, "等待环节名称-看一看")
            self.click_element(mploc.loc_source_name_look, "点击环节名称-看一看")
            self.webdriver_wait_clickable(mploc.loc_source_type, "等待环节类型选项框可用")
            self.click_element(mploc.loc_source_type, "点击环节类型")
            self.sleep(1)
            self.webdriver_wait_clickable(mploc.loc_source_type_kada, "等待环节类型-KaDa协议选项可用")
            self.click_element(mploc.loc_source_type_kada, "点击环节类型-KaDa协议")
            self.input_text(mploc.loc_kada_input, "输入kada协议内容", "kada://openurl?url=http%3A%2F%2Fwlsq.lingdiantech.com%2Fapp%2Findex.php%3Fi%3D13%26c%3Dentry%26do%3Dindex%26m%3Dfy_ks_mechanism%26scid%3DMlgdO0O0OkO0O0Oj%26shenbaoid%3DNlDdEk3j&navBarType=3")

        self.click_element(mploc.loc_source_save, "点击保存按钮")
        # 这里立即创建下个环节用例时，前端页面偶现报路由错误，这样增加稳定性
        self.sleep(1)
        self.webdriver_wait_visibility(mploc.loc_source_save_success, "等待创建环节页alert提示信息可见")
        actual_text = self.get_text(mploc.loc_source_save_success, "获取创建环节页alert提示信息")
        return actual_text


