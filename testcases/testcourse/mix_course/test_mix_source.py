import allure
import pytest
from hamcrest import assert_that, equal_to

from pageobjects.course.menu.menu_page import MenuPage
from pageobjects.course.mix_course.mix_course_list_page import MixCourseListPage
from pageobjects.course.mix_course.mix_lesson_manage_page import MixLessonManagePage


@allure.epic("KaDa故事运营后台")
@allure.feature("AI互动课")
class TestMixLesson(object):

    @allure.title("AI互动课——新增互动环节")
    @pytest.mark.parametrize("source_type", [1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_add_mix_source(self, login_k, source_type):
        driver = login_k
        mp = MenuPage(driver)
        mp.menu_mix_course()
        mclp = MixCourseListPage(driver)
        mclp.click_manage_button()

        mlmp = MixLessonManagePage(driver)
        actual_text = mlmp.add_mix_source(source_type)
        assert_that(actual_text, equal_to("创建成功"))




