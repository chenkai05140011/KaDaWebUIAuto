
class MixCourseListPageLocs(object):

    """
    互动课列表页面要操作的元素的定位规则
    """

    # 付费类型
    loc_ke_select_type = ("css", ".query-form form>div:nth-child(1) input")
    loc_ke_select_type_all = ("xpath", "(//span[text()='全部'])[2]")
    loc_ke_select_type_pay = ("xpath", "//span[text()='付费']")
    loc_ke_select_type_free = ("xpath", "//span[text()='免费']")
    # 课程状态
    loc_ke_select_status = ("css", ".query-form form>div:nth-child(2) input")
    loc_ke_select_status_all = ("xpath", "(//span[text()='全部'])[2]")
    loc_ke_select_status_put = ("xpath", "//span[text()='已上架']")
    loc_ke_select_status_off = ("xpath", "//span[text()='已下架']")
    loc_ke_select_status_wait = ("xpath", "//span[text()='待上架']")
    # 课程名称
    loc_ke_select_name = ("css", ".query-form form>div:nth-child(3) input")
    # 课程id
    loc_ke_select_id = ("xpath", "(//input[@class='el-input__inner'])[4]")
    # 是否精品
    loc_ke_select_boutique = ("css", ".query-form form>div:nth-child(5) input")
    loc_ke_select_boutique_all = ("xpath", "(//span[text()='全部'])[2]")
    loc_ke_select_boutique_yes = ("xpath", "//span[text()='是']")
    loc_ke_select_boutique_no = ("xpath", "//span[text()='否']")
    # 搜索框内清除按钮
    loc_ke_select_clear = ("css", ".el-input__suffix .el-icon-circle-close")
    # 查询按钮
    loc_ke_select_button = ("xpath", "//span[text()=' 查询 ']")
    # 查询结果-第1个课程的id
    loc_ke_select_result_first = ("xpath", "(//td[@colspan='1']//div)[1]")

    # 新增互动课程
    loc_ke_add_button = ("xpath", "//span[text()=' 新增互动课程 ']")

    # 第1个课程-管理按钮
    loc_ke_manage_button = ("css", ".el-table__fixed-right tbody tr:nth-child(1) .el-button--info")

    # 互动课程上架
    loc_ke_put_y = ("css", ".el-dialog__footer .el-button--primary")
    loc_ke_put_n = ("css", ".query-form form>div:nth-child(2) input")