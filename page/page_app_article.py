from base.base_app import BaseApp
import page


class PageAppArticle(BaseApp):
    # 查找频道
    def page_find_chanel(self, click_channel_text):
        self.base_right_swipe_left(page.app_channel_area, click_channel_text)

    # 查找文章
    def page_find_article(self, click_article_text):
        self.base_down_swipe_up(page.app_article_area, click_article_text)

    # 查找文章业务方法
    def page_article(self, click_channel_text="python", click_article_text="模块"):
        self.page_find_chanel(click_channel_text)
        self.page_find_article(click_article_text)