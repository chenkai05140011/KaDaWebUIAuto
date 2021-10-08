import datetime
from selenium.webdriver.common.keys import Keys
from tools.basepage import BasePage
from pagelocators.mixcourse.mix_course_list_page_locs import MixCourseListPageLocs as mclpl
from pagelocators.mixcourse.mix_course_edit_page_locs import MixCourseEditPageLocs as mcepl

from tools.base_mysql import select_sql

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

closing_time = (datetime.datetime.now() + datetime.timedelta(days=+30)).strftime('%Y-%m-%d %H:%M:%S')

project_root_path = BasePage.project_root_path()


class MixCourseEditPage(BasePage):

    def add_mix_course(self, mix_name="",
                       file_cover=project_root_path + "data\img_coures\\before_purchase_transverse.png",
                       file_transverse=project_root_path + "data\img_coures\\after_purchase_transverse.png",
                       file_perpendicular=project_root_path + "data\img_coures\\purchase_perpendicular.png",
                       mp3=project_root_path + "data\mp3\yp_2.mp3",
                       recommendation="推荐语_zdh1",
                       subscription="3306",
                       pay_type=0,
                       original_price=200,
                       non_vip_price=99,
                       vip_price=79,
                       is_limit_free=0,
                       ):
        """
        新建/编辑课程
        @param mix_name:课程名称
        @param file_cover:封面图或购买前横版封面
        @param file_transverse:购买后横版封面
        @param file_perpendicular:购买前或购买后竖版封面
        @param mp3:介绍音频
        @param recommendation:推荐语
        @param subscription:基础订阅量
        @param pay_type:付费类型,0-付费，1-免费
        @param original_price: 原价
        @param non_vip_price: 非会员价
        @param vip_price: 会员价
        @param is_limit_free: 是否限免，默认0-非限免，1-限免
        @return:
        """
        # 偶现元素不可点击异常，多用例执行时alert遮住按钮，故用js点击
        self.execute_script_with_element("arguments[0].click();", mclpl.loc_ke_add_button, "点击新增互动课节按钮")
        self.input_text(mcepl.loc_mix_name, "输入课程名称", mix_name)
        self.input_text(mcepl.loc_cover, "上传封面图", file_cover)
        self.input_upload_file(mcepl.loc_cover2, file_cover, "上传购买前横版封面")
        self.input_upload_file(mcepl.loc_cover3, file_perpendicular, "上传购买前竖版封面")
        self.input_upload_file(mcepl.loc_cover4, file_transverse, "上传购买后横版封面")
        self.input_upload_file(mcepl.loc_cover5, file_perpendicular, "上传购买后竖版封面")
        self.input_upload_file(mcepl.loc_mp3, mp3, "上传介绍音频")

        self.click_element(mcepl.loc_teacher, "打开老师入口")
        self.click_element(mcepl.loc_adviser, "打开宣传片")
        self.click_element(mcepl.loc_new_product, "打开新品")
        self.webdriver_wait_clickable(mcepl.loc_course_color, "等待课程配色可用")
        self.click_element(mcepl.loc_course_color, "点击课程配色")
        # 偶现下拉选项出现但不可点击，这里增加稳定性
        self.sleep(1)
        self.webdriver_wait_clickable(mcepl.loc_course_color_option_first, "等待课程配色下拉选项-第1个选项可用")
        self.click_element(mcepl.loc_course_color_option_first, "点击课程配色下拉选项-第1个选项")

        self.input_text(mcepl.loc_course_tag, "输入课程标签", "逻辑能力")
        self.input_text(mcepl.loc_course_tag, "模拟按ENTER键", Keys.ENTER)
        self.input_text(mcepl.loc_course_target, "输入课程目标", "这里是课程目标")
        self.input_text(mcepl.loc_recommendation, "输入推荐语", recommendation)
        self.input_text(mcepl.loc_subscription, "输入基础订阅量", subscription)
        self.input_text(mcepl.loc_tag, "输入标签", "K12")
        self.input_text(mcepl.loc_course_tag, "模拟按ENTER键", Keys.ENTER)

        # 判断付费类型
        if pay_type == 0:
            self.input_text(mcepl.loc_original, "输入原价", original_price)
            self.input_text(mcepl.loc_non_vip_price, "输入非会员价", non_vip_price)
            self.input_text(mcepl.loc_vip_price, "输入会员价", vip_price)
            self.click_element(mcepl.loc_deduction_type_default_scale, "红包类型选择默认比例")
            if is_limit_free != 0:
                self.click_element(mcepl.loc_join_limit_free, "打开限免")
                self.webdriver_wait_clickable(mcepl.loc_limit_start_time, "等待起始时间输入框可用")
                self.input_text(mcepl.loc_limit_start_time, "输入起始时间", now_time)
                self.input_text(mcepl.loc_limit_closing_time, "输入结束时间", closing_time)
                self.click_element(mcepl.loc_limit_confirm, "点击确定")
        else:
            self.click_element(mcepl.loc_payment_no, "打开免费")
        self.click_element(mcepl.loc_is_prompt_update, "点击是否提示更新")
        self.click_element(mcepl.loc_is_prompt_update_yes, "选择更新课程")
        self.input_text(mcepl.loc_course_edition, "输入课程版本号", "v5.5.22")

        self.click_element(mcepl.loc_detail_tab, "点击详情页管理tab")
        self.click_element(mcepl.loc_course_details_markdown, "点击markdown选项")
        self.input_text(mcepl.loc_markdwon_edit, "这里是markdown编辑器文本", "在markdown编辑器输入文本")
        self.click_element(mcepl.loc_save_button, "提交保存")
        # 偶现元素定位不到问题
        self.sleep(1)
        self.webdriver_wait_visibility(mclpl.loc_ke_select_result_first, "等待第1个课程出现")
        actual = self.get_text(mclpl.loc_ke_select_result_first, "第1个课程的id")
        return actual


if __name__ == '__main__':
    sql = f'SELECT * from course_info WHERE name="课程2.6";'
    a = select_sql(sql)
    print(a)
    text = a[0]['id']
    print(text)
