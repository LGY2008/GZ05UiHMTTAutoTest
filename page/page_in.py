from page.page_app_article import PageAppArticle
from page.page_app_login import PageAppLogin
from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin
from tool.get_driver import GetDriver
import page


class PageIn:
    """统一入口类 page页面对象进行管理"""

    # 获取PageMpLogin对象
    def page_get_PageMplogin(self):
        return PageMpLogin(GetDriver.get_web_driver(page.url_mp))

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(GetDriver.get_web_driver(page.url_mp))

    # 获取PageMisLogin对象
    def page_get_PageMisLogin(self):
        return PageMisLogin(GetDriver.get_web_driver(page.url_mis))

    # 获取PageMisAudit对象
    def page_get_PageMisAudit(self):
        return PageMisAudit(GetDriver.get_web_driver(page.url_mis))

    # 获取PageAppLogin对象
    def page_get_PageAppLogin(self):
        return PageAppLogin(GetDriver.get_app_driver())

    # 获取PageAppArticle对象
    def page_get_PageAppArticle(self):
        return PageAppArticle(GetDriver.get_app_driver())