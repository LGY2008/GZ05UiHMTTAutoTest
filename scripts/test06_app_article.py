import sys, os
from time import sleep

sys.path.append(os.getcwd())
import pytest

from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_log import GetLog

log = GetLog.get_log()


class TestAppArticle:
    # 初始化
    @classmethod
    def setup_class(cls):
        # 获取统一入口类对象
        cls.pageIn = PageIn()
        # 调用登录成功方法
        cls.pageIn.page_get_PageAppLogin().page_app_login_success()
        # 获取PageAppArticle对象
        cls.article = cls.pageIn.page_get_PageAppArticle()

    # 结束
    @classmethod
    def teardown_class(cls):
        sleep(5)
        # 关闭driver
        GetDriver.quit_app_driver()

    # 测试方法
    @pytest.mark.parametrize("click_channel_text,click_article_text", read_yaml("app_article.yaml"))
    def test_app_article(self, click_channel_text, click_article_text):
        try:
            # 调用业务方法
            self.article.page_article(click_channel_text, click_article_text)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_image()
            # 抛异常
            raise
