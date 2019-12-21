import sys
import os
sys.path.append(os.getcwd())

import pytest

from tool.read_yaml import read_yaml

from tool.get_log import GetLog
from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestMpArticle:
    # 初始化
    @classmethod
    def setup_class(cls):
        # 获取统一入类实例
        cls.page = PageIn()
        # 调用登录方法
        cls.page.page_get_PageMplogin().page_mp_login_success()
        # 获取PageMpArticle实例对象
        cls.article = cls.page.page_get_PageMpArticle()

    # 结束
    @classmethod
    def teardown_class(cls):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 发布文章测试方法
    @pytest.mark.parametrize("title,content,expect", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content, expect):
        # 调用 发布文章业务方法
        self.article.page_article(title, content)
        try:
            # 断言
            assert expect == self.article.page_get_msg()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_image()
            # 抛异常
            raise
