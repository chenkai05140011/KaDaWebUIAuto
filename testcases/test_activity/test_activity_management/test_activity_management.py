from time import sleep

import allure
import pytest

from pageobjects.activity.activity_list_page import ActivityListPage


@allure.epic("KaDa故事运营后台")
@allure.feature("活动")
@pytest.mark.ui_test
class TestActivityManagement:
    @allure.title("成功进入【活动列表】页面")
    def test_activity_config_success(self, login_k):    # login_k由conftest直接引入无需导包
        driver = login_k
        # sleep(3)
        ActivityListPage(driver).activity_management_menu_expand()
        ActivityListPage(driver).activity_list()
        sleep(3)
        text = ActivityListPage(driver).get_activity_config_verify_text()
        assert text == '活动配置'

    @allure.title("成功进入【活动配置-手机号领福利】页面")
    def test_activity_config_button_success(self, login_k):
        driver = login_k
        web = ActivityListPage(driver)
        web.activity_management_menu_expand()
        web.activity_list()
        web.activity_config_button()
        sleep(3)
        text = web.get_activity_config_button_title_verify_text()
        print(text)
        assert text == '活动配置 - 手机号领福利'

    @allure.title("成功进入【活动统计-手机号领福利】页面")
    def test_activity_static_button_success(self, login_k):
        driver = login_k
        ActivityListPage(driver).activity_management_menu_expand()
        ActivityListPage(driver).activity_list()
        ActivityListPage(driver).activity_static_button()
        sleep(3)
        text = ActivityListPage(driver).get_activity_static_button_title_verify_text()
        print(text)
        assert text == '活动统计 - 手机号领福利'


if __name__ == '__main__':
    pytest.main(["-s", "test_activity_management"])
