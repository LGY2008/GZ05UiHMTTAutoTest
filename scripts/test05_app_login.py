import sys, os

sys.path.append(os.getcwd())
import pytest

from tool.get_log import GetLog
from tool.read_yaml import read_yaml

from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 获取PageAppLogin对象
        self.login = PageIn().page_get_PageAppLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 登录测试方法
    @pytest.mark.parametrize("username,pwd", read_yaml("app_login.yaml"))
    def test_app_login(self, username, pwd):
        # 调用登录业务方法
        self.login.page_app_login(username, pwd)
        try:
            # 断言
            result = self.login.page_if_login_success()
            print("登录是否成功：", result)
            assert result, "断言错误！，没有发现登录成功后要找的元素！"
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_image()
            # 抛异常
            raise
