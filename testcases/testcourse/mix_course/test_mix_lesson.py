import allure
import pytest
from hamcrest import assert_that, equal_to

from pageobjects.course.menu.menu_page import MenuPage
from pageobjects.course.mix_course.mix_course_list_page import MixCourseListPage
from pageobjects.course.mix_course.mix_lesson_manage_page import MixLessonManagePage


@allure.epic("KaDa故事运营后台")
@allure.feature("AI互动课")
class TestMixLesson(object):

    @allure.title("AI互动课——新增互动单元")
    @pytest.mark.parametrize("unit_name, unit_order", [("第一单元", "单元一")])
    def test_add_mix_unit(self, login_k, unit_name, unit_order):
        driver = login_k
        mp = MenuPage(driver)
        mp.menu_mix_course()
        mclp = MixCourseListPage(driver)
        mclp.click_manage_button()

        mlmp = MixLessonManagePage(driver)
        actual_text = mlmp.add_mix_unit(unit_name, unit_order)
        assert_that(actual_text, equal_to(unit_name))

    @allure.title("AI互动课——新增互动课节")
    @pytest.mark.parametrize("lesson_name, file_cover, lesson_type, copyright",
                             [("第一课节", "data\img_coures\lesson_cover.png", 1, "KDBQ100033")
                              ])
    def test_add_mix_lesson(self, login_k, lesson_name, file_cover, lesson_type, copyright):
        driver = login_k
        mp = MenuPage(driver)
        mp.menu_mix_course()
        mclp = MixCourseListPage(driver)
        mclp.click_manage_button()

        mlmp = MixLessonManagePage(driver)
        actual_text = mlmp.add_mix_lesson(lesson_name, file_cover, lesson_type, copyright)
        assert_that(actual_text, equal_to("创建成功"))

    @allure.title("AI互动课——上传互动课节视频文件")
    @pytest.mark.parametrize("video_file", ["data\mp4\source_video.mp4"])
    def test_upload_mix_lesson_video(self, login_k, video_file):
        driver = login_k
        mp = MenuPage(driver)
        mp.menu_mix_course()
        mlp = MixCourseListPage(driver)
        mlp.click_manage_button()

        mlmp = MixLessonManagePage(driver)
        actual_text = mlmp.add_upload_video(video_file)
        assert_that(actual_text, equal_to("上传状态：文件上传完毕"))




