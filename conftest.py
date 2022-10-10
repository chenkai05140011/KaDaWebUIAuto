
import os
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="https://pwebdev.bojx.com:6443",
        help="test case project host address"
    )

@pytest.fixture(scope="session",autouse=True)
def host(request):
    """获取命令行参数"""
    #获取命令行参数给环境变量
    os.environ["host"] = request.config.getoption("--cmdhost")
    print("当前用例运行测试环境：%s"%os.environ["host"])