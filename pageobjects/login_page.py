from tools.basepage import BasePage
import allure
from pagelocators.login_page_locs import LoginPageLocs as loc
from testdatas.global_data import GlobalData
import os

@allure.feature("登入模块")
class LoginPage(BasePage):
    # 登入
    login_url = "/#/login"
    @allure.step("输入用户名")
    def input_user(self, username):
        self.input_text(loc.loc_user, "输入用户名", username)

    @allure.step("输入密码")
    def input_psw(self, psw):
        self.input_text(loc.loc_password, "输入密码", psw)

    @allure.step("点击登录按钮")
    def click_button(self):
        self.click_element(loc.loc_button, "点击登录按钮")

    @allure.step("验证是否登入成功")
    def is_login_success(self):
        text = self.get_text(loc.loc_assert, "验证是否登入成功")
        print(text)
        return text == "首页"

    @allure.step("登录")
    def login(self, username='chenxiaokai', psw='hhdd1209'):
        self.open_url(os.environ["host"]+self.login_url)
        self.input_user(username)
        self.input_psw(psw)
        self.click_button()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web =LoginPage(driver)
    web.open_url('http://ales.pre.icinfo.co/')
    driver.maximize_window()
    web.login('18395948730', '1', '1')
    web.wait(3)
    result = web.is_login_success()
    web.quit()



