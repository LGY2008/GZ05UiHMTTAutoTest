from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tool.get_log import GetLog

log = GetLog.get_log()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info("获取driver对象：{}".format(driver))
        self.driver = driver

    # 查找 元素
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元祖或列表
        :param timeout:超时时间默认为30秒
        :param poll:访问频率
        :return:元素
        """
        log.info("正在查找：{} 元素".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入 封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        log.info("对：{}元素 执行清空操作".format(loc))
        # 清空
        el.clear()
        log.info("对：{}元素 执行输入：{}操作".format(loc, value))
        # 输入操作
        el.send_keys(value)

    # 点击 封装
    def base_click(self, loc):
        log.info("对：{}元素 执行点击操作".format(loc))
        self.base_find(loc).click()

    # 获取 文本
    def base_get_text(self, loc):
        log.info("执行对：{}元素 执行获取文本值 {}操作".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图方法
    def base_get_image(self):
        # 截图
        self.driver.get_screenshot_as_file("./image/err.png")
        log.error("出错啦！，正在截图操作，截图文件名为：err.png")
        # 调用将图片写入报告方法
        self.base_write_image_allure()
        log.info("将图片写入allure报告完成")

    # 写入报告方法
    def base_write_image_allure(self):
        log.info("正在将图片写入allur报告")
        with open("./image/err.png", "rb")as f:
            allure.attach("失败原因：", f.read(), allure.attach_type.PNG)

    # 下拉框（input+li）公共方法操作
    def base_click_input_click_text(self, placeholder_text, click_text):
        # 组合 输入框元素定位信息
        loc = By.XPATH, "//*[@placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        sleep(1)
        loc = By.XPATH, "//li//*[text()='{}']".format(click_text)
        self.base_click(loc)

    # 判断当前页面是否包换传入指定元素
    def base_if_text_element_exists(self, text):
        # 组合文本 定位配置数据
        loc = By.XPATH, "//*[contains(text(),'{}')]".format(text)
        try:
            # 调用查找方法  存在返回True
            self.base_find(loc, timeout=3)
            return True
        except:
            # 不存在返回False
            return False

