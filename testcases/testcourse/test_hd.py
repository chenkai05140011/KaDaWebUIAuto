import time
import pytest
import allure
from tools.base_mysql import select_sql
from pageobjects.course.hd_course_page import HdCoursePage
from pageobjects.course.menu.menu_page import MenuPage


@allure.epic("KaDa故事运营后台")
@allure.feature("HD_课程")
@pytest.mark.ui_test
class Test_Hd():
    rq = time.strftime('%m%d%H%M%S', time.localtime(time.time()))  # 获取当前系统时间
    rq_1 = time.strftime('%M%S', time.localtime(time.time()))  # 获取当前系统时间
    rq_2 = time.strftime('%H%M%S', time.localtime(time.time()))  # 获取当前系统时间
    @allure.title("HD课程——查询")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    @pytest.mark.parametrize("hd_id", ["90427"])
    def test_select_hd(self, login_k, hd_id):
        '''
        :param login_k: 登录
        1、查询纯视频课
        name="纯视频"
        id="90333"
        type=1、2、3 全部、付费、免费
        state=1、2、3、4 全部、已上架、已下架、待上架
        :return:
        '''
        driver = login_k
        menu = MenuPage(driver)
        menu.menu_hd()
        web = HdCoursePage(driver)
        text = web.select_hd(id=hd_id)
        assert text == hd_id

    @allure.title("HD课程——新增")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    @pytest.mark.parametrize("hd_name", [('x' + rq_2)])
    def test_add_hd(self, login_k, hd_name):
        '''
        :param login_k: 登录
        1、查询纯视频课
        name="纯视频"
        id="90333"
        type=1、2、3 全部、付费、免费
        state=1、2、3、4 全部、已上架、已下架、待上架
        :return:
        '''
        driver = login_k
        menu = MenuPage(driver)
        menu.menu_hd()
        web = HdCoursePage(driver)
        web.add_hd(name=hd_name)
        time.sleep(2)
        sql = f'SELECT * from course_info WHERE name="{hd_name}";'
        a = select_sql(sql)
        text = a[0]['name']
        assert text == hd_name
