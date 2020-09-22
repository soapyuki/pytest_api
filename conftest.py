import pytest, os


def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store", default="http://127.0.0.1:7777",
        help="test case project host address"
    )


@pytest.fixture(scope="session", autouse=True)
def host_fix(request):
    '''获取命令行参数 给到环境变量'''
    os.environ["admin_host"] = request.config.getoption("--cmdhost")
    print('当前运行环境: %s' % os.environ["admin_host"])
