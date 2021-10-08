from time import sleep

from tools.basepage import BasePage
from pagelocators.index_page_locs import MenuCourse as mloc
from pagelocators.activity.Activity_list_page_locs import ActivityListPageLocs as adLoc
from testcases.conftest import login_k


class ActivityListPage(BasePage):
    # 点击展开活动管理二级菜单
    def activity_management_menu_expand(self):
        self.click_element(mloc.loc_menu_activity_management, "展开【活动管理】二级菜单")

    # 点击进入活动配置页
    def activity_list(self):
        self.click_element(mloc.loc_menu_activity_lists, "进入【活动列表】页面")

    # 点击进入活动配置-手机号领福利
    def activity_config_button(self):
        self.click_element(adLoc.loc_activity_config_config_button, "进入【活动配置 - 手机号领福利】页面")

    # 点击进入活动配置-手机号领福利
    def activity_static_button(self):
        self.click_element(adLoc.loc_activity_config_static_button, "进入【活动统计 - 手机号领福利】页面")

    # 获取【活动配置】标题验证元素
    def get_activity_config_verify_text(self):

        return self.get_text(adLoc.loc_activity_config_verify_text, "获取验证文本【活动配置】")

    # 获取【活动配置 - 手机号领福利】标题验证元素
    def get_activity_config_button_title_verify_text(self):
        return self.get_text(adLoc.loc_activity_config_button_title_verify_text, "获取验证文本【活动配置-手机号领福利】")

    # 获取【活动配置 - 手机号领福利】标题验证元素
    def get_activity_static_button_title_verify_text(self):
        return self.get_text(adLoc.loc_activity_static_button_title_verify_text, "获取验证文本【活动统计-手机号领福利】")


if __name__ == '__main__':

    driver = login_k()
    sleep(3)
    ActivityListPage(driver).activity_management_menu_expand()
    ActivityListPage.activity_list(driver)
