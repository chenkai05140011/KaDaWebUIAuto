# -*- coding=utf-8-*-
# @author:Jake Lee
# @file:handle_logger.py
# @time:2021/5/19 22:57
# @software:PyCharm

import logging
from tools.handle_read_conf import log_info
from tools.handle_path import logfile


class HandleLogger(logging.Logger):
    def __init__(self, name, level=logging.INFO, file=None):
        # 调用父类初始化方法，设置日志级别、日志渠道、日志格式
        super().__init__(name=name, level=level)
        # 创建日志输出格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s[第%(lineno)d行] %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        # 创建控制台渠道:
        s_handler = logging.StreamHandler()
        # 绑定日志格式到控制台渠道
        s_handler.setFormatter(formatter)
        # 将控制台渠道和日志收集器绑定
        self.addHandler(s_handler)

        # 假如传入文件路径，则默认创建文件形式渠道
        try:
            if file:
                f_handler = logging.FileHandler(filename=file, encoding='utf-8')
                f_handler.setFormatter(formatter)
                self.addHandler(f_handler)
        except FileNotFoundError as e:
            print("File Not Found Error")
            raise e


logger = HandleLogger(name=log_info['logger_name'], file=logfile)

