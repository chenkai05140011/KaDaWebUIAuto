import time

import allure
import pytest
from hamcrest import equal_to
from hamcrest.core import assert_that

from pageobjects.course.menu.menu_page import MenuPage
from pageobjects.course.mix_course.mix_course_edit_page import MixCourseEditPage
from pageobjects.course.mix_course.mix_course_list_page import MixCourseListPage
from tools.base_mysql import select_sql

rq_2 = time.strftime('%H%M%S', time.localtime(time.time()))  # 获取当前系统时间


@allure.epic("KaDa故事运营后台")
@allure.feature("AI互动课")
class TestMixVideo(object):

    @allure.title("AI互动课——查询")
    @pytest.mark.parametrize("pure_id", ["90563"])
    def test_select_mix_course(self, login_k, pure_id):
        driver = login_k
        mp = MenuPage(driver)
        mp.menu_mix_course()
        mlp = MixCourseListPage(driver)

        actual_text = mlp.select_mix_course(mix_id=pure_id)
        assert_that(actual_text, equal_to(pure_id))

    @allure.title("AI互动课——新增付费课程、限免课程、免费课程")
    @pytest.mark.parametrize("mix_name, pay_type, is_limit_free", [('付费互动课' + rq_2, 0, 0),
                                                                   ('限免互动课' + rq_2, 0, 1),
                                                                   ('免费互动课' + rq_2, 1, 1)
                                                                   ])
    def test_add_mix_course(self, login_k, mix_name, pay_type, is_limit_free):
        driver = login_k
        mp = MenuPage(driver)
        mp.menu_mix_course()
        mcep = MixCourseEditPage(driver)

        actual_text = mcep.add_mix_course(mix_name=mix_name, pay_type=pay_type, is_limit_free=is_limit_free)
        sql = f'SELECT * from course_info WHERE name="{mix_name}";'
        expect_text = select_sql(sql)[0]['id']
        assert_that(actual_text, equal_to(str(expect_text)))