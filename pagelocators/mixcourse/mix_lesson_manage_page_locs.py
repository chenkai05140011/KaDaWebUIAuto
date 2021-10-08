class MixLessonManagePageLocs(object):

    """
    互动课节管理页面要操作的元素的定位规则
    """
    # =====单元=====
    # 互动单元管理
    loc__mix_unit = ("xpath", "//span[text()=' 互动单元管理 ']")
    # 新增互动单元
    loc_mix_unit_add = ("xpath", "//span[text()=' 新增互动单元 ']")
    # 互动单元名称
    loc_unit_name = ("css", "form>div:nth-child(1) input")
    # 互动单元序号
    loc_unit_sort = ("css", "form>div:nth-child(2) input")
    # 是否显示单元名称-是
    loc_unit_name_y = ("css", "form>div:nth-child(3) label:nth-child(2) .el-radio__input")
    # 是否显示单元名称-否
    loc_unit_name_n = ("css", "form>div:nth-child(3) label:nth-child(1) .el-radio__input")
    # 新增互动单元-保存按钮
    loc_unit_save = ("xpath", "(//span[text()='确 定'])[1]")
    # 单元列表-第1条数据
    loc_unit_list_first = ("xpath", "(//td[@colspan='1']//div)[5]")

    # =====课节=====
    # 新增互动课节
    loc_add_mix_lesson = ("xpath", "//span[text()=' 新增互动课节 ']")
    # 课节名称
    loc_lesson_name = ("css", "[placeholder='建议输入15字以内']")
    # 封面
    loc_lesson_cover = ("xpath", "//div[@class='upload-icon-cont']//i[1]")
    # 课程单元
    loc_lesson_unit = ("xpath", "(//input[@placeholder='请选择'])[1]")
    # # 课程单元-第1个选项
    # loc_lesson_unit_first = ("css", "[x-placement='bottom-start'] ul li:nth-child(1)")
    # 课程单元-最后1个选项
    loc_lesson_unit_last = ("xpath", "(//span[starts-with(text(), '单元')])[last()]")
    # 是否试学
    loc_lesson_is_try = ("css", "[role='switch'] span")
    # 课节背景
    # loc_lesson_background = ("xpath", "(//label[text()='课节背景:']/following::input)[1]")
    # 是否引导添加老师
    loc_lesson_add_teacher = ("xpath", "(//label[text()='是否引导添加老师:']/following::input)[1]")
    # 是否引导添加老师-提示引导
    loc_lesson_add_teacher_tips = ("xpath", "//span[text()='提示引导']")
    # 课节类型
    loc_lesson_type = ("xpath", "(//label[text()='课节类型:']/following::input)[1]")
    # 课节类型-混编课节
    loc_lesson_type_blend = ("xpath", "//span[text()='混编课节']")
    # 课节类型-互动视频课节
    loc_lesson_mix_video = ("xpath", "//span[text()='互动视频课节']")
    # 版权号
    loc_lesson_copyright = ("xpath", "(//label[text()='版权号:']/following::input)[1]")
    # 新增互动课节-保存
    loc_lesson_save = ("xpath", "//span[text()=' 保存 ']")
    # 新增课节成功
    loc_lesson_save_success = ("xpath", "//p[text()='创建成功']")
    # 新增互动课节-第1条数据_编辑按钮
    loc_lesson_list_edit_first = ("css", ".el-table__fixed-body-wrapper tbody>tr:nth-child(1) td:nth-child(11) "
                                         ".top-btn-cont button:nth-child(1)")
    # 新增互动课节-最后1条数据_编辑按钮
    loc_lesson_list_edit_last = ("xpath", "(//span[text()=' 编辑 '])[last()]")

    # =====互动课节文件管理=====
    # 互动课节文件管理
    loc_lesson_file_manage = ("xpath", "//span[text()=' 互动课节文件管理 ']")
    # 选择文件
    loc_lesson_select_file = ("xpath", "(//button[@type='button']//span)[2]")
    # 开始上传
    loc_lesson_start_upload = ("xpath", "//span[text()=' 开始上传 ']")
    # 上传状态
    loc_lesson_upload_status = ("xpath", "//span[text()='上传状态：文件上传完毕']")

    # =====环节=====
    # 新增环节
    loc_source_add = ("xpath", "(//button[@type='button']//i)[4]")
    # 环节名称
    loc_source_name = ("xpath", "(//label[text()='环节名称:']/following::input)[1]")
    # 环节名称_看一看
    loc_source_name_look = ("xpath", "//span[text()='看一看']")
    # 环节名称_练一练
    loc_source_name_practice = ("xpath", "//span[text()='练一练']")
    # 环节名称_玩一玩
    loc_source_name_play = ("xpath", "//span[text()='玩一玩']")
    # 环节名称_说一说
    loc_source_name_talk = ("xpath", "//span[text()='说一说']")
    # 环节类型
    loc_source_type = ("xpath", "(//label[text()='环节类型:']/following::input)[1]")
    # 环节类型_视频互动课
    loc_source_type_mix_video = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(2)")
    # 环节类型_录音题
    loc_source_type_record = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(3)")
    # 环节类型_选择题
    loc_source_type_select = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(4)")
    # 环节类型_拼图题
    loc_source_type_jigsaw_puzzle = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(5)")
    # 环节类型_纯视频2.0
    loc_source_type_video = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(6)")
    # 环节类型_拍摄题
    loc_source_type_video_record = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(7)")
    # 环节类型_KaDa协议
    # loc_source_type_kada = ("xpath", "//span[text()='KaDa协议")
    loc_source_type_kada = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(8)")
    # KaDa协议输入框
    loc_kada_input = ("xpath", "//input[@placeholder='输入kada协议']")
    # 环节类型_语音AI评测题
    # loc_source_type_ai_record = ("xpath", "//span[text()='语音AI评测题")
    loc_source_type_ai_record = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(9)")
    # 环节类型_拖拽题
    # loc_source_type_drag = ("xpath", "//span[text()='语音AI评测题")
    loc_source_type_drag = ("css", "body>div:nth-last-of-type(1) ul li:nth-child(10)")
    # 新增环节_保存
    loc_source_save = ("xpath", "//span[text()=' 保存 ']")
    # 新增环节成功
    loc_source_save_success = ("xpath", "//p[text()='创建成功']")





