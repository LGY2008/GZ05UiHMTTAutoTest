import sys
import os

sys.path.append(os.getcwd())
from tool.get_log import GetLog
import pytest

from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestMpLogin:
    # 初始化
    @classmethod
    def setup_class(cls):
        # 获取PageMpLogin对象
        cls.login = PageIn().page_get_PageMplogin()

    # 结束
    @classmethod
    def teardown_class(cls):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 登录测试方法
    @pytest.mark.parametrize("username,pwd,expect", read_yaml("mp_login.yaml"))
    def test_login(self, username, pwd, expect):
        # 调用登录业务方法
        self.login.page_mp_login(username, pwd)
        try:
            # 断言
            nickname = self.login.page_get_nickname()
            assert expect == nickname, "出错啦！预期登录用户昵称和实际显示不符合！"
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_image()
            # 抛异常
            raise