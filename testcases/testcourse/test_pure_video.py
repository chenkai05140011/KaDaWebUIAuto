import time
import pytest
import allure

from tools.base_mysql import select_sql
from pageobjects.course.pure_video_course_page import PureVideoCoursePage


@allure.epic("KaDa故事运营后台")
@allure.feature("纯视频课")
@pytest.mark.ui_test
class Test_pure_video():
    rq = time.strftime('%m%d%H%M%S', time.localtime(time.time()))  # 获取当前系统时间
    rq_1 = time.strftime('%M%S', time.localtime(time.time()))  # 获取当前系统时间
    rq_2 = time.strftime('%H%M%S', time.localtime(time.time()))  # 获取当前系统时间
    @allure.title("纯视频课——查询")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    @pytest.mark.parametrize("pure_id", ["90333"])
    def test_select_pure_video(self, login_k, pure_id):
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
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        text = web.select_pure_video(id=pure_id)
        assert text == pure_id

    @allure.title("纯视频课——新增课程")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    @pytest.mark.parametrize("video_name", [('x' + rq_2)])
    def test_add_pure_video(self, login_k, video_name):
        '''
        :param login_k: 登录
        1、查询纯视频课
        name="纯视频"
        update=1、2 更新 不更新
        version="5.5.20"
        :return:
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        web.add_pure_video(name=video_name)
        # 等待一下入库
        time.sleep(1)
        sql = f'SELECT * from course_info WHERE name="{video_name}";'
        a = select_sql(sql)
        text = a[0]['name']
        assert text == video_name

    @allure.title("纯视频课——编辑课程")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    @pytest.mark.parametrize("b_video_name", [('b' + rq_1)])
    def test_edit_pure_video(self, login_k, b_video_name):
        '''
        :param login_k: 登录
        name="e"
        update=2
        version="5.5.20"
        unit_name="单元二"
        :return:
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        web.edit_pure_video(name=b_video_name)
        # 等待一下入库
        time.sleep(1)
        sql = f'SELECT * from course_info WHERE name="{b_video_name}";'
        a = select_sql(sql)
        text = a[0]['name']
        assert text == b_video_name

    @allure.title("纯视频课——课节配置——新增课节")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    @pytest.mark.parametrize("lesson_name", [('课节' + rq_1)])
    def test_add_lesson_pure_video(self, login_k, lesson_name):
        '''
        :param login_k: 登录
        name="课节"
        mp4="E:\kada_gs\kada_ui\mp4\lesson01.mp4"
        number="KDBQ100033"
        :return:
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        web.add_lesson_pure_video(name=lesson_name)
        # 等待一下入库
        time.sleep(1)
        sql = f'SELECT * from mix_lesson_info WHERE name="{lesson_name}";'
        a = select_sql(sql)
        text = a[0]['name']
        assert text == lesson_name

    @allure.title("纯视频课——课节配置——编辑课节")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("secret", yaml.safe_load("a.yaml"))
    @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_edit_lesson_pure_video(self, login_k, lesson_name):
        '''
        :param login_k: 登录
        name="课节"
        mp4="E:\kada_gs\kada_ui\mp4\lesson01.mp4"
        number="KDBQ100033"
        :return:
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        web.edit_lesson_pure_video(name=lesson_name)
        # 等待一下入库
        time.sleep(1)
        sql = f'SELECT * from mix_lesson_info WHERE name="{lesson_name}";'
        a = select_sql(sql)
        text = a[0]['name']
        assert text == lesson_name

    @allure.title("纯视频课——课节配置——课节试学")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_learn_lesson_pure_video(self, login_k):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        text = web.learn_lesson_pure_video()
        assert text == "全部试学" or "取消全部试学"



    @allure.title("纯视频课——运营配置")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    @pytest.mark.parametrize("subscription", [rq_1])
    def test_add_yy_config_pure_video(self, login_k, subscription):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        web.yy_config_lesson_pure_video(subscription=subscription)
        # 等待一下入库
        time.sleep(1)
        sql = f'SELECT * from course_info WHERE subscribeInitCount="{subscription}";'
        a = select_sql(sql)
        text = a[0]['subscribeInitCount']
        assert str(text) in subscription

    @allure.title("纯视频课——课节配置——课节上架")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_online_lesson_pure_video(self, login_k):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        status = web.online_lesson_pure_video()
        time.sleep(3)
        assert status == "上架成功" or "下架成功"

    @allure.title("纯视频课——课节配置——课节批量上架")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_batch_online_lesson_pure_video(self, login_k):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        status = web.lesson_batch_online_pure_video()
        time.sleep(3)
        assert status == "批量上架成功"

    @allure.title("纯视频课——课节配置——课节批量下架")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_batch_off_lesson_pure_video(self, login_k):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        status = web.lesson_batch_off_pure_video()
        time.sleep(3)
        assert status == "批量下架成功"

    @allure.title("纯视频课——课节配置——课节批量设置单元")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_batch_unit_lesson_pure_video(self, login_k):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        status = web.lesson_batch_unit_pure_video()
        time.sleep(3)
        assert status == "保存成功"

    @allure.title("纯视频课——课节配置——课节批量设置版权号")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_batch_number_lesson_pure_video(self, login_k):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        status = web.lesson_batch_number_pure_video()
        time.sleep(3)
        assert status == "设置成功"

    @allure.title("纯视频课——课程上架")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_online_pure_video(self, login_k):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web = PureVideoCoursePage(driver)
        web.menu_pure_video()
        status = web.online_pure_video()
        assert status == "上架成功" or "下架成功"

    @allure.title("纯视频课——复制地址")
    # @allure.testcase("http://jira.icinfo.co/browse/ZJXZZF-349#")
    # @allure.issue("http://jira.icinfo.co/browse/ZJXZZF-315")
    # @allure.description("case描述：添加岗位类别")
    # @allure.severity("blocker")
    # @pytest.mark.parametrize("lesson_name", [('编辑课节' + rq_1)])
    def test_copy_address_pure_video(self, login_k):
        '''
        :param
        login_k: 登录
        :return:
        name
        '''
        driver = login_k
        web =PureVideoCoursePage(driver)
        web.menu_pure_video()
        text = web.copy_lesson_pure_video()
        assert text == "复制成功"

if __name__ == '__main__':
    pytest.main(["-s", "test_pure_video.py"])