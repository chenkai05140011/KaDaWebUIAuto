# -*- coding=utf-8-*-

class HdCoursePageLocs:
    """
    课堂主页页面要操作的元素的定位规则
    """
    # hd课查询
    # 课程名称
    loc_hd_select_name = ("xpath", "(//input[@class='el-input__inner'])[5]")
    # 课程ID
    loc_hd_video_select_id = ("xpath", "(//input[@type='number'])[1]")
    # 查询按钮
    loc_hd_video_select_button = ("xpath", "//span[text()=' 查询 ']")
    # 校验查询是否正确
    loc_hd_video_select_assert = ("xpath", "(//td[@colspan='1']//div)[1]")
    # 清除输入项
    loc_hd_clear = ("css", ".el-input__suffix .el-icon-circle-close")

    # hd课程新增
    # hd添加课程按钮
    loc_hd_add_button = ("xpath", "//span[text()=' 新增课程 ']")
    # 课程名称
    loc_hd_add_name = ("xpath", "//input[@placeholder='长度在 1 到 15 个字符']")
    # 课程分类
    loc_hd_add_class = ("xpath", "(//input[@placeholder='请选择'])[1]")
    loc_hd_add_class_4 = ("xpath", "//span[text()='内部课程']")
    # 课程形式
    loc_hd_add_form = ("xpath", "(//input[@placeholder='请选择'])[2]")
    loc_hd_add_form_2 = ("xpath", "//span[text()='视频课程']")
    # 课程分类
    loc_hd_add_type = ("xpath", "(//input[@placeholder='请选择'])[3]")
    loc_hd_add_type_2 = ("xpath", "//span[text()='学科拓展']")
    # 课程封面
    loc_hd_add_cover1 = ("css", "[accept='image/*']")
    loc_hd_add_cover2 = ("css", ".el-row div:nth-child(6) [accept='image/gif,image/png']")
    loc_hd_add_cover3 = ("css", ".el-row div:nth-child(7) [accept='image/gif,image/png']")
    loc_hd_add_cover4 = ("css", ".el-row div:nth-child(8) [accept='image/gif,image/png']")
    loc_hd_add_cover5 = ("css", ".el-row div:nth-child(9) [accept='image/gif,image/png']")
    # 推荐语
    loc_hd_add_recommendation = ("xpath", "//input[@placeholder='建议输入21字以内']")
    # 基础订阅量
    loc_hd_add_subscription = ("xpath", "(//label[text()='基础订阅量:']/following::input)[1]")
    # 标签
    loc_hd_add_tag = ("xpath", "//input[@placeholder='长度不超过6个字']")
    # 原价
    loc_hd_add_price = ("xpath", "(//label[text()='原价:']/following::input)[1]")
    # 图文详情tab
    loc_hd_add_tab2 = ("id", "tab-2")
    # 图文详情封面
    loc_hd_add_cover6 = ("css", "[id='pane-2'] [accept='image/*']")
    # markdown
    loc_hd_add_markdown = ("css", "[placeholder='开始编辑...']")
    # 保存按钮
    loc_hd_add_save = ("xpath", "//span[text()=' 保存 ']")




