import page
from base.base import Base
from tool.get_log import GetLog

log = GetLog.get_log()


class PageMpLogin(Base):
    # 输入 用户名
    def page_input_username(self, username):
        self.base_input(page.mp_username, username)

    # 输入 密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mp_pwd, pwd)

    # 点击 登录按钮
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取 昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法
    def page_mp_login(self, username, pwd):
        log.info("正在执行登录业务方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 组合业务方法 解决登录依赖
    def page_mp_login_success(self, username="13812345678", pwd="246810"):
        log.info("正在执行登录业务方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
