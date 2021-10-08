from tools.basepage import BasePage
from pagelocators.index_page_locs import MenuCourse as mloc


class MenuPage(BasePage):

    def menu_mix_course(self):
        """
        进入互动课程管理页
        """
        self.click_element(mloc.loc_menu_content, "菜单-点击内容管理")
        self.click_element(mloc.loc_menu_mix_course, "菜单-互动课程管理")

    def menu_pure_video(self):
        """
        进入纯视频课管理页
        """
        self.click_element(mloc.loc_menu_content, "点击内容管理")
        self.click_element(mloc.loc_menu_pure_video, "视频课程管理")

    def menu_hd(self):
        """
        进入课程管理列表页
        """
        self.click_element(mloc.loc_menu_content, "点击内容管理")
        self.click_element(mloc.loc_menu_hd, "课程管理列表")
