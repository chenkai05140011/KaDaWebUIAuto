# -*- coding=utf-8-*-

class PureVideoCoursePageLocs:
    """
    课堂主页页面要操作的元素的定位规则
    """
    # 纯视频课查询
    loc_pure_video_select_name = ("css", "form>div:nth-child(1) input")
    loc_pure_video_select_id = ("css", "form>div:nth-child(2) input")
    loc_pure_video_select_input_text = ("css", "form>div:nth-child(3) input")
    loc_pure_video_select_state = ("css", "form>div:nth-child(4) input")
    loc_pure_video_select_button = ("css", "form>div:nth-child(5) button")
    loc_pure_video_select_reset = ("css", "form>div:nth-child(6) button")
    # 下拉选项
    loc_pure_video_select_drop_1 = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(1)")
    loc_pure_video_select_drop_2 = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(2)")
    loc_pure_video_select_drop_3 = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(3)")
    loc_pure_video_select_drop_4 = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(4)")
    loc_pure_video_select_drop_1_1 = ("css", "[x-placement='bottom-start'] ul li:nth-child(1)")
    loc_pure_video_select_drop = ("css", "[x-placement='bottom-start']")
    loc_pure_video_select_assert = ("xpath", "(//td[@colspan='1']//div)[1]")
    # 纯视频课-新建课程
    loc_pure_video_add_button = ("css", ".white-bg>button")
    loc_pure_video_add_name = ("css", "input[maxlength='15']")
    loc_pure_video_add_sj_bj = ("css", "form>div>div:nth-child(2) [tabindex='0']")
    loc_pure_video_add_ipad_bj = ("css", "form>div>div:nth-child(3) [tabindex='0']")
    loc_pure_video_add_update = ("css", "[placeholder='请选择']")
    loc_pure_video_add_drop_1 = ("css", ".el-popper ul li:nth-child(1)")
    loc_pure_video_add_drop_2 = ("css", ".el-popper ul li:nth-child(2)")
    loc_pure_video_add_version = ("css", "[placeholder='请输入课程对应的APP版本号']")
    loc_pure_video_add_button_n = ("css", "[id='foot-button-cell'] .el-button--default")
    loc_pure_video_add_button_y = ("css", "[id='foot-button-cell'] .el-button--primary")
    loc_pure_video_add_drop = ("css", "[x-placement='bottom-start']")
    # 纯视频课-列表操作loc_pure_video_online
    loc_pure_video_online = ("css", ".el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td:nth-child(17) span:nth-child(1)")
    loc_pure_video_edit = ("css", ".el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td:nth-child(17) span:nth-child(2)")
    loc_pure_video_lesson = ("css", ".el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td:nth-child(17) span:nth-child(3)")
    loc_pure_video_yy_config = ("css", ".el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td:nth-child(17) span:nth-child(4)")
    loc_pure_video_copy_address = ("css", ".el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td:nth-child(17) span:nth-child(5)")
    loc_pure_video_delete = ("css", ".is-scrolling-right tbody>tr:nth-child(1)>td:nth-child(17) span:nth-child(6)")

    # 纯视频课-添加单元
    loc_pure_video_add_unit = ("css", ".common-title-cont button")
    loc_pure_video_add_unit_name = ("css", "[placeholder='只能8字以内']")
    loc_pure_video_add_unit_y = ("xpath", "(//span[text()='确 定'])[3]")
    loc_pure_video_add_name_clear = ("css", ".el-input__suffix .el-icon-circle-close")




    # 纯视频课-课节配置
    loc_pure_video_lesson_add = ("css", ".btn-con .el-button--primary")
    loc_pure_video_lesson_add_unit = ("css", ".btn-con .el-button--default")
    loc_pure_video_lesson_learn_y = ("css", ".btn-con .el-button--success")
    loc_pure_video_lesson_learn_n = ("css", ".btn-con .el-button--danger")
    loc_pure_video_lesson_unit = ("css", "form .el-col>div:nth-child(1) input")
    loc_pure_video_lesson_sort = ("css", "form .el-col>div:nth-child(2) input")
    loc_pure_video_lesson_name = ("css", "form .el-col>div:nth-child(3) input")
    loc_pure_video_lesson_fm = ("css", "form .el-col>div:nth-child(4) input")
    loc_pure_video_lesson_try_to_learn = ("css", "form .el-col>div:nth-child(5) input")
    loc_pure_video_lesson_file = ("css", "form .el-col>div:nth-child(6) button")
    loc_pure_video_lesson_number = ("css", "form .el-col>div:nth-child(7) input")
    loc_pure_video_lesson_file_assert = ("css", "form .el-col>div:nth-child(7) input")
    loc_pure_video_lesson_y = ("xpath", "//span[text()=' 保存 ']")



    loc_pure_video_lesson_learn_text = ("xpath", "//span[text()=' 全部试学 ']")
    loc_pure_video_lesson_learn_yes = ("xpath", "(//span[text()='确 定'])[1]")



    loc_pure_video_lesson_learn = ("xpath", "//label[text()='是否试学:']")
    loc_pure_video_lesson_edit = ("css", ".el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td:nth-child(11) span:nth-child(2)")



    loc_pure_video_lesson_online_1 = ("css", ".el-notification .el-notification__title")
    loc_pure_video_lesson_online_y = ("css", ".class-cont .el-button--primary")
    loc_pure_video_lesson_online = ("css", ".el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td:nth-child(11) span:nth-child(1)")


    # 基础信息
    loc_pure_video_yy_config_subscription = ("css", "[placeholder='配置后将影响已购人数：基础订阅+实际订阅']")
    loc_pure_video_yy_config_time = ("css", "[placeholder='自动全屏时间（秒）']")
    loc_pure_video_yy_config_fm_1 = ("xpath", "(//input[@accept='.png,.gif'])[1]")
    loc_pure_video_yy_config_fm_2 = ("xpath", "(//input[@accept='.png,.gif'])[2]")
    loc_pure_video_yy_config_fm_3 = ("xpath", "(//input[@accept='.png,.gif'])[3]")
    loc_pure_video_yy_config_fm_4 = ("xpath", "(//input[@accept='.png,.gif'])[4]")
    loc_pure_video_yy_config_fm_5 = ("xpath", "(//input[@accept='.png,.gif'])[5]")
    loc_pure_video_yy_config_fm_6 = ("xpath", "(//input[@accept='.png,.gif'])[6]")

    # 价格信息
    loc_pure_video_yy_config_price_1 = ("xpath", "(//input[@placeholder='请输入'])[1]")
    loc_pure_video_yy_config_price_2 = ("xpath", "(//input[@placeholder='请输入'])[2]")
    loc_pure_video_yy_config_price_3 = ("xpath", "(//input[@placeholder='请输入'])[3]")

    # 详情页信息
    loc_pure_video_yy_config_recommendation = ("css", "[placeholder='配置后，将会在详情页显示']")
    loc_pure_video_yy_config_tag = ("css", "[placeholder='每个标签长度不超过6个字，以回车隔开']")
    loc_pure_video_yy_config_format = ("xpath", "(//input[@placeholder='请选择'])[5]")
    loc_pure_video_yy_config_format_1 = ("xpath", "//span[text()='markdown']")
    loc_pure_video_yy_config_format_markdown = ("css", "[placeholder='开始编辑...']")
    loc_pure_video_yy_config_map_1 = ("css", ".flex-cont>div:nth-child(1) .el-upload")
    loc_pure_video_yy_config_ct = ("xpath", "//section[@id='app-main']/div[1]/form[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]")
    loc_pure_video_yy_config_ct_1 = ("xpath", "//div[text()=' 仅支持.png、.gif格式图片，10M内 ']")
    loc_pure_video_yy_config_y = ("xpath", "//span[text()=' 提交 ']")

    loc_pure_video_lesson_copy_text = ("css", ".el-message .el-message__content")

    loc_pure_video_online_y = ("xpath", "//span[text()='确 定']")

    # 课节批量操作
    loc_pure_video_lesson_batch = ("xpath", "(//span[@class='el-checkbox__inner'])[1]")
    loc_pure_video_lesson_batch_online = ("xpath", "//span[text()=' 批量上架 ']")
    loc_pure_video_lesson_batch_assert = ("css", "[role='alert'] p")

    loc_pure_video_lesson_batch_y_1 = ("xpath", "(//span[text()='确 定'])[1]")
    loc_pure_video_lesson_batch_y_2 = ("xpath", "(//span[text()='确 定'])[2]")
    loc_pure_video_lesson_batch_y_3 = ("xpath", "(//span[text()='确 定'])[3]")
    loc_pure_video_lesson_batch_y_4 = ("xpath", "(//span[text()='确 定'])[4]")

    loc_pure_video_lesson_batch_off = ("xpath", "//span[text()=' 批量下架 ']")

    loc_pure_video_lesson_batch_unit = ("xpath", "//span[text()=' 批量设置单元 ']")
    loc_pure_video_lesson_batch_unit_1 = ("xpath", "(//input[@placeholder='请选择课节所属单元'])[1]")
    loc_pure_video_lesson_batch_unit_2 = ("xpath", "(//input[@placeholder='请选择课节在单元内的顺序'])")

    loc_pure_video_lesson_batch_number = ("xpath", "//span[text()=' 批量设置版权号 ']")
    loc_pure_video_lesson_batch_number_input = ("css", "[placeholder='回车确认查询版权信息']")




