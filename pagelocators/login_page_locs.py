# -*- coding=utf-8-*-
# @author:Jake Lee
# @file:login_page_locs.py
# @time:2021/7/30 0:04
# @software:PyCharm

from selenium.webdriver.common.by import By


class LoginPageLocs(object):
    """
    登录页面要操作的元素的定位规则
    """
    # 用户名输入框
    loc_user = ("css", 'input[placeholder="请输入用户名"]')
    # 密码输入框
    loc_password = ("css", 'input[placeholder="请输入登录密码"]')
    # 登录按钮
    loc_button = ("css", "button[type=button]")
    # 错误提示
    loc_assert = ("css", "span.no-redirect")

