from base.base_app import BaseApp
import page
from tool.get_log import GetLog

log = GetLog.get_log()


class PageAppLogin(BaseApp):

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.app_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.app_pwd, pwd)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 判断是否登录成功
    def page_if_login_success(self):
        # 将查找元素结果返回 True / False
        return self.base_app_if_element_exists(page.app_me)

    # 组合登录业务方法
    def page_app_login(self, username, pwd):
        log.info("正在调用app登录业务方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 组合登录成功依赖方法
    def page_app_login_success(self, username="13812345678", pwd="246810"):
        log.info("正在调用app成功登录业务依赖方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()