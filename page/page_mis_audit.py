from time import sleep

from base.base import Base
import page
from tool.get_log import GetLog

log = GetLog.get_log()


class PageMisAudit(Base):
    # 点击信息管理
    def page_click_info_manage(self):
        sleep(1)
        self.base_click(page.mis_info_manage)

    # 点击内容审核
    def page_click_content_audit(self):
        sleep(1)
        self.base_click(page.mis_manage_audit)

    # 输入文章标题
    def page_input_title(self, title):
        self.base_input(page.mis_title, title)

    # 输入文章频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 选择状态
    def page_click_status(self, placeholder_text="请选择状态", click_text="待审核"):
        # 请选择状态 -> 待审核
        self.base_click_input_click_text(placeholder_text, click_text)

    # 查询按钮
    def page_click_search_btn(self):
        self.base_click(page.mis_find)
        sleep(2)
        page.article_id = self.page_get_article_id()
        print("审核的文章id为：", page.article_id)

    # 获取id方法
    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    # 通过
    def page_click_pass_btn(self):
        sleep(2)
        self.base_click(page.mis_pass_btn)

    # 确定
    def page_click_confirm_btn(self):
        sleep(1)
        self.base_click(page.mis_confirm)

    # 判断是否审核成功
    def page_assert_audit(self, title=page.title, channel=page.channel):
        log.info("正在判断文章是否审核成功..")
        # 刷新
        self.driver.refresh()
        sleep(3)
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status(click_text="审核通过")
        self.page_click_search_btn()
        # 判断页面是否包含文章id
        return self.base_if_text_element_exists(page.article_id)

    # 审核文章组合业务方法
    def page_audit(self, title=page.title, channel=page.channel):
        log.info("正在调用文章审核业务方法, 审核文章title:{} 审核文章id为：{}".format(page.title, page.article_id))
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_search_btn()
        self.page_click_pass_btn()
        self.page_click_confirm_btn()
