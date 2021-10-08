# -*- coding=utf-8-*-

class MenuCourse:
    """
    菜单页面要操作的元素的定位规则
    """
    # 内容管理
    loc_menu_content = ("xpath", "//span[text()='内容管理']")
    # 视频课程管理
    loc_menu_pure_video = ("xpath", "//span[text()='视频课程管理']")
    # hd课程管理
    loc_menu_hd = ("xpath", "(//span[text()='课程管理列表'])[1]")
    # 互动课程管理
    loc_menu_mix_course = ("xpath", "//span[text()='互动课程管理']")
    # 活动管理【一级】
    loc_menu_activity_management = ("xpath", "//span[text()='活动管理']")
    # 活动列表【二级】
    loc_menu_activity_lists = ("xpath", "//span[text()='活动列表']")
