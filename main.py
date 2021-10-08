# -*- coding=utf-8-*-
# @author:Jake Lee
# @file:main.py
# @time:2021/8/7 21:35
# @software:PyCharm

import pytest
from tools.handle_path import allure_file_dir

pytest.main(["-s", "-v", "--reruns", "2", "--reruns-delay", "5", "--alluredir={}".format(allure_file_dir), "-p", "no:faulthandler"])

# -m 选项通过标签来筛选要执行的用例
# pytest.main(["-s", "-v", "--reruns", "2", "--reruns-delay", "5", "--alluredir={}".format(allure_file_dir), "-m", "demo"])
# -m 选项支持条件运算 and/or/not, 但是要注意需写在同一个选项中
# pytest.main(["-s", "-v", "--reruns", "2", "--reruns-delay", "5", "--alluredir={}".format(allure_file_dir), "-m demo and test"])
