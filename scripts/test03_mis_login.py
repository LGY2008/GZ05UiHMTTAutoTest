import sys, os
from time import sleep

sys.path.append(os.getcwd())
import pytest

from tool.read_yaml import read_yaml
from tool.get_log import GetLog
from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestMisLogin:
    # 初始化
    @classmethod
    def setup_class(cls):
        # 获取PageMisLogin对象
        cls.login = PageIn().page_get_PageMisLogin()

    # 结束
    @classmethod
    def teardown_class(cls):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 登录测试方法
    @pytest.mark.parametrize("username,pwd,expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, pwd, expect):
        # 调用登录测试业务方法
        self.login.page_mis_login(username, pwd)
        try:
            # 获取昵称
            nickname = self.login.page_get_nickname()
            assert expect in nickname, "断言出错啦！登录的用户不是{}".format(expect)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_image()
            # 抛异常
            raise
