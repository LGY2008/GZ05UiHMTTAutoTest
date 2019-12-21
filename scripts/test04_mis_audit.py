import sys
import os

sys.path.append(os.getcwd())
from tool.get_log import GetLog
from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


class TestMisAudit:
    # 初始化
    @classmethod
    def setup_class(cls):
        # 获取PageIn实例对象
        cls.pageIn = PageIn()
        # 调用后台管理登录业务成功方法
        cls.pageIn.page_get_PageMisLogin().page_mis_login_success()
        # 获取PageMisAudit对象
        cls.audit = cls.pageIn.page_get_PageMisAudit()

    # 结束
    @classmethod
    def teardown_class(cls):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 文章审核测试方法
    def test_article_audit(self):
        # 调用 审核业务方法
        self.audit.page_audit()
        try:
            # 判断是否审文章是否成功
            result = self.audit.page_assert_audit()
            assert result, "审核文章失败！，没有在审核通过中发现审核文章id"
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.audit.base_get_image()
            # 抛异常
            raise