# -*- coding=utf-8-*-

class ActivityListPageLocs:
    """活动列表主页【活动配置】页面元素"""

    # 【活动配置页】页面元素
    # 配置按钮
    loc_activity_config_config_button = ("xpath", "//span[text()=' 配置 ']")
    # 统计按钮
    loc_activity_config_static_button = ("xpath", "//span[text()=' 统计 ']")

    # 【活动配置页】验证元素
    loc_activity_config_verify_text = ("xpath", "//h3[text()='活动配置']")
    # 【活动配置 - 手机号领福利】验证元素
    loc_activity_config_button_title_verify_text = ("xpath", "//h3[text()='活动配置 - 手机号领福利']")
    # 【活动统计 - 手机号领福利】验证元素
    loc_activity_static_button_title_verify_text = ("xpath", "//h3[text()='活动统计 - 手机号领福利']")
