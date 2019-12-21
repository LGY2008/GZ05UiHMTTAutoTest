from base.base import Base
import page
from tool.get_log import GetLog

log = GetLog.get_log()


class PageMisLogin(Base):
    # 输入 用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 输入 密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 点击 登录按钮
    def page_click_login_btn(self):
        # 重点：必须使用js处理disabled属性
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        self.base_click(page.mis_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 组合登录业务方法
    def page_mis_login(self, username, pwd):
        log.info("正在执行后台管理登录业务方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 组合登录业务方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        log.info("正在执行后台管理登录业务依赖成功方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
