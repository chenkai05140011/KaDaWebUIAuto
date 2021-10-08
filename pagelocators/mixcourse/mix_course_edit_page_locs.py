
class MixCourseEditPageLocs(object):

    """
    互动课新增/编辑页面要操作的元素的定位规则
    """

    # 互动课程名称
    loc_mix_name = ("css", "input[placeholder='长度在 1 到 15 个字符']")
    # 封面
    loc_cover = ("css", ".el-col [accept='image/*']")
    # 购买前横版封面
    loc_cover2 = ("css", ".el-col div:nth-child(3) [accept='image/gif,image/png']")
    # 购买前竖版封面
    loc_cover3 = ("css", ".el-col div:nth-child(4) [accept='image/gif,image/png']")
    # 购买后横版封面
    loc_cover4 = ("css", ".el-col div:nth-child(5) [accept='image/gif,image/png']")
    # 购买后竖版封面
    loc_cover5 = ("css", ".el-col div:nth-child(6) [accept='image/gif,image/png']")
    # 介绍音频
    loc_mp3 = ("css", "[accept='.mp3']")
    # 老师入口
    loc_teacher = ("xpath", "(//label[text()='老师入口:']/following::span)[1]")
    # 是否使用宣传片
    loc_adviser = ("xpath", "(//label[text()='是否使用宣传片:']/following::span)[1]")
    # 是否新品
    loc_new_product = ("xpath", "(//label[text()='是否新品:']/following::span)[1]")
    # 课程配色
    loc_course_color = ("xpath", "//*[@placeholder='请选择课程主题配色']")
    # 课程配色下拉选项-第1个
    loc_course_color_option_first = ("xpath", "//span[text()='苹果绿']")
    # 课程标签
    loc_course_tag = ("xpath", "//input[starts-with(@placeholder, '请输入课程标签')]")
    # 课程目标
    loc_course_target = ("xpath", "//label[text()='课程目标:']/following::textarea")
    # 推荐语
    loc_recommendation = ("css", "[placeholder='建议输入21字以内']")
    # 基础订阅量
    loc_subscription = ("css", "[placeholder='基础订阅量']")
    # 标签
    loc_tag = ("css", "[placeholder='长度不超过6个字']")
    # 付费类型_付费
    # loc_payment_yes = ("xpath", "//span[text()=' 付费 ']")
    # 付费类型_免费
    loc_payment_no = ("xpath", "//span[text()=' 免费 ']")
    # 是否试学
    # loc_is_try_learn = ("xpath", "(//label[text()='是否试学:']/following::span)[1]")
    # 是否为精品内容
    loc_is_boutique = ("xpath", "(//label[text()='是否为精品内容:']/following::span)[1]")
    # 原价
    loc_original = ("xpath", "(//label[text()='原价:']/following::input)[1]")
    # 非会员价
    loc_non_vip_price = ("xpath", "(//label[text()='非会员价:']/following::input)[1]")
    # 会员价
    loc_vip_price = ("xpath", "(//label[text()='VIP会员价:']/following::input)[1]")
    # 红包抵扣类型_不参加活动
    # loc_deduction_type_default = ("xpath", "//span[text()=' 不参加活动 ']")
    # 红包抵扣类型_默认比例
    loc_deduction_type_default_scale = ("xpath", "//span[text()=' 默认比例 ']")
    # 红包抵扣类型_指定减免金额
    # loc_deduction_type_appoint = ("xpath", "//span[text()=' 指定减免金额 ']")
    # 是否提示更新
    loc_is_prompt_update = ("xpath", "//input[@placeholder='请选择']")
    # 是否提示更新-更新
    loc_is_prompt_update_yes = ("xpath", "//span[text()='更新']")
    # 是否提示更新-不更新
    # loc_is_prompt_update_no = ("xpath", "//span[text()='不更新']")
    # 课程版本
    loc_course_edition = ("xpath", "//input[@placeholder='请输入课程对应的APP版本号']")
    # 是否参加限免
    loc_join_limit_free = ("xpath", "(//label[text()='是否参加限免:']/following::span)[1]")
    # 限免起始时间
    loc_limit_start_time = ("xpath", "(//input[@placeholder='开始日期'])[1]")
    # 限免结束时间
    loc_limit_closing_time = ("xpath", "(//input[@placeholder='结束日期'])[1]")
    # 时间弹窗-确定
    loc_limit_confirm = ("xpath", "(//button[contains(@class,'el-button el-picker-panel__link-btn')]//span)[2]")
    # 详情页管理tab
    loc_detail_tab = ("id", "tab-2")
    # 课程详情-长图
    # loc_course_details = ("css", "form>div:nth-child(5) [tabindex='0'] input")
    # 课程详情-markdown
    loc_course_details_markdown = ("xpath", "//span[text()=' markdown ']")
    # markdown编辑器
    loc_markdwon_edit = ("xpath", "//textarea[@placeholder='开始编辑...']")
    # 保存
    loc_save_button = ("xpath", "//span[text()=' 保存 ']")

