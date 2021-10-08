from tools.basepage import BasePage
from pagelocators.mixcourse.mix_course_list_page_locs import MixCourseListPageLocs as mclpl


class MixCourseListPage(BasePage):

    def select_mix_course(self, mix_name="", mix_id="90563", select_type=1, select_status=1, select_boutique=1):
        """
        互动课程列表-查询功能
        @param mix_name:
        @param mix_id:
        @param select_type: 付费类型
        @param select_status:课程状态
        @param select_boutique:是否精品
        """
        self.click_element(mclpl.loc_ke_select_type, "点击付费类型选项按钮")
        if select_type == 1:
            self.click_element(mclpl.loc_ke_select_type_all, "点击付费类型-全部")
        elif select_type == 2:
            self.click_element(mclpl.loc_ke_select_type_pay, "点击付费类型-付费")
            self.webdriver_wait_clickable(mclpl.loc_ke_select_boutique, "等待是否精品选项按钮可用")
            self.click_element(mclpl.loc_ke_select_boutique, "点击是否精品选项按钮")
            if select_boutique == 1:
                self.click_element(mclpl.loc_ke_select_boutique_all, "点击是否精品-全部")
            elif select_boutique == 2:
                self.click_element(mclpl.loc_ke_select_boutique_yes, "点击是否精品-是")
            elif select_boutique == 3:
                self.click_element(mclpl.loc_ke_select_boutique_no, "点击是否精品-否")
            else:
                print("请输入正确的select_boutique")
        elif select_type == 3:
            self.click_element(mclpl.loc_ke_select_type_free, "点击付费类型-免费")
        else:
            print("请输入正确的select_type")

        self.webdriver_wait_clickable(mclpl.loc_ke_select_status, "等待程状态选项按钮可用")
        self.click_element(mclpl.loc_ke_select_status, "点击课程状态选项按钮")
        if select_status == 1:
            self.click_element(mclpl.loc_ke_select_status_all, "点击课程状态-全部")
        elif select_status == 2:
            self.click_element(mclpl.loc_ke_select_status_put, "点击课程状态-已上架")
        elif select_status == 3:
            self.click_element(mclpl.loc_ke_select_status_off, "点击课程状态-已下架")
        elif select_status == 4:
            self.click_element(mclpl.loc_ke_select_status_wait, "点击课程状态-待上架")
        else:
            print("请输入正确的select_type")
        self.input_text(mclpl.loc_ke_select_name, "输入课程名称", mix_name)
        self.input_text(mclpl.loc_ke_select_id, "输入课程id", mix_id)
        self.click_element(mclpl.loc_ke_select_button, "点击查询按钮")
        self.sleep(2)
        # 校验查询内容
        text = self.get_text(mclpl.loc_ke_select_result_first, "获取查询结果-第1个课程的id")
        # 因@pytest.fixture(scope="package")，需做用例衔接，清理输入框内容
        self.mouse_move_to_element(mclpl.loc_ke_select_id, "鼠标移动到课程id输入框")
        self.click_element(mclpl.loc_ke_select_clear, "点击清除")
        return text

    def click_manage_button(self):
        """
        互动课程列表-点击第1个课程
        """
        self.click_element(mclpl.loc_ke_manage_button, "点击课程列表第1个课程-管理按钮")
