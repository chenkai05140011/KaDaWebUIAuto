# -*- coding=utf-8-*-
# @author:Jake Lee
# @file:handle_configer.py
# @time:2021/7/31 0:28
# @software:PyCharm

from configparser import ConfigParser

from tools.handle_path import ini_file


class HandleConfiger(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        # 读取配置文件
        self.read(filename, encoding="utf-8")


configer = HandleConfiger(ini_file)


