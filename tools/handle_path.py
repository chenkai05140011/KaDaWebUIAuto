# -*- coding=utf-8-*-
# @author:Jake Lee
# @file:handle_path.py
# @time:2021/7/31 0:24
# @software:PyCharm

import os
import time
# 项目根目录
rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件目录
confdir = os.path.join(rootdir, "conf")
ini_file = os.path.join(rootdir, 'conf', 'conf.ini')

# 日志文件目录
log_file_name = time.strftime("%Y%m%d_%H%M", time.localtime()) + '.log'
logfile = os.path.join(rootdir, "outputs", 'logfiles', log_file_name)

# 报告文件目录
allure_file_dir = os.path.join(rootdir, "outputs", "allure-files")

# 测试数据目录
testdata_dir = os.path.join(rootdir, "testdatas")

# 测试用例目录
testcase_dir = os.path.join(rootdir, "testcases")

# 截图保存路径
screenshot_path = os.path.join(rootdir, "outputs", 'screenshots')

# 上传作业测试文件
homework_file = os.path.join(testdata_dir, r'course\homework_upload_file.py')


if __name__ == '__main__':
    print(homework_file)
