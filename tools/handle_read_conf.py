# -*- coding=utf-8-*-
# @author:Jake Lee
# @file:handle_read_conf.py
# @time:2021/7/31 0:24
# @software:PyCharm


from tools.handle_configer import configer

# log配置信息
log_info = dict(configer.items("log"))
# # 报告配置信息
# report_info = dict(configer.items("report"))
# # mysql配置信息
# mysql_info = dict(configer.items('mysql'))
# # 用例excel相关配置信息
# sheet_info = dict(configer.items('sheet'))


if __name__ == '__main__':
    print(log_info)

