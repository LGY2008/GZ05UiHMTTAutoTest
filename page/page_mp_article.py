from time import sleep

from base.base import Base
import page
from tool.get_log import GetLog

log = GetLog.get_log()


class PageMpArticle(Base):
    # 点击内容管理
    def page_click_content_manage(self):
        sleep(2)
        self.base_click(page.mp_content_manage)

    # 点击发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)

    # 输入文章标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)

    # 输入文章内容
    def page_input_content(self, content):
        sleep(2)  # 切换iframe
        frame = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(frame)
        # 输入内容
        self.base_input(page.mp_content, content)
        # 回到默认目录
        self.driver.switch_to.default_content()

    # 选择封面
    def page_click_cover(self):
        self.base_click(page.mp_auto)

    # # 选择频道  （7:为数据库）
    # def page_click_channel(self):
    #     # 点击最外侧 请选择
    #     self.base_click(page.mp_channel)
    #     sleep(1)
    #     # 具体内容 数据库
    #     self.base_click(page.mp_click_channel)

    # 点击发表
    # 选择频道  （7:为数据库）
    def page_click_channel(self):
        self.base_click_input_click_text("请选择",page.channel)

    def page_click_confirm(self):
        self.base_click(page.mp_confirm)

    # 获取发表提示信息 （新增文章成功
    def page_get_msg(self):
        return self.base_get_text(page.mp_result)

    # 组合业务方法
    def page_article(self, title, content):
        log.info("正在调用输入文章业务方法，文章标题：{} 文章内容：{}".format(title, content))
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_confirm()
