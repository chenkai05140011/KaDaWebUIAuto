from selenium import webdriver
import pytest
import time
from pageobjects.login_page import LoginPage
import allure
from selenium.webdriver.chrome.options import Options


@allure.feature("设置driver")
@pytest.fixture(scope="package")
def driver(request):
    # # linux启动
    # chrome_options = Options()
    # chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
    # chrome_options.add_argument('--headless')  # 无界面
    # chrome_options.add_argument('--no-sandbox')  # 解决devtoolsactiveport文件不存在报错
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--disable-gpu')  # 禁用gpu硬件加速
    # _driver = webdriver.Chrome(chrome_options=chrome_options)
    # # 奇安信可信
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = r"C:\Users\kevin\AppData\Roaming\360se6\Application\360se.exe"  # 这里是360安全浏览器的路径
    # chrome_options.add_argument(r'--lang=zh-CN')  # 这里添加一些启动的参数
    # _driver = webdriver.Chrome(chrome_options=chrome_options)
    # window启动
    # _driver = webdriver.Firefox()
    _driver = webdriver.Chrome()
    _driver.implicitly_wait(15)
    _driver.maximize_window()

    def end():
        print("全部caes执行完退出游览器")
        _driver.quit()

    request.addfinalizer(end)  # 终结函数
    return _driver

@allure.feature("用户登录")
@pytest.fixture(scope="package")
def login_k(driver):
    web = LoginPage(driver)
    web.login()
    assert web.is_login_success()
    return driver
