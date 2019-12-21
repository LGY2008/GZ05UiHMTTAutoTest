from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base.base import Base
from tool.get_log import GetLog

log = GetLog.get_log()


class BaseApp(Base):
    # 判断元素是否存在
    def base_app_if_element_exists(self, loc):
        try:
            self.base_find(loc, timeout=3)
            log.info("找到元素：{} 存在".format(loc))
            return True  # 返回True 存在
        except:
            log.error("没有找到元素：{} 存在".format(loc))
            return False  # 返回False 不存在

    # 从右向左滑动->查找频道
    def base_right_swipe_left(self, area_loc, click_text):
        # 定位区域元素
        el = self.base_find(area_loc)

        # 获取区域元素 位置
        x = el.location.get("x")
        y = el.location.get("y")

        # 获取预期元素 宽高
        width = el.size.get("width")
        height = el.size.get("height")

        # 计算 start_x,start_y,end_x,end_y
        start_x = x + width * 0.8
        start_y = y + height * 0.5
        end_x = x + width * 0.2
        end_y = y + height * 0.5

        # 获取当前页面结构
        self.page_source = self.driver.page_source
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(click_text)
        while True:
            try:
                # 找一次元素
                self.base_find(loc, timeout=2).click()
                print("找到元素啦！")
                break
            except:
                print("当前页面没有找到！")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 判断 是否滑到最后一屏幕
            if self.page_source == self.driver.page_source:
                print("滑不动啦！")
                # 抛出异常
                raise NoSuchElementException
            else:
                # 否则，更新下之前的变量值
                self.page_source = self.driver.page_source

    # 从上到下滑动 ->查找文章标题
    def base_down_swipe_up(self, area_loc, click_text):
        # 定位区域元素
        el = self.base_find(area_loc)

        # 获取预期元素 宽高
        width = el.size.get("width")
        height = el.size.get("height")

        # 计算 start_x,start_y,end_x,end_y
        start_x =width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2

        # 获取当前页面结构
        self.page_source = self.driver.page_source
        loc = By.XPATH, "//*[@bounds='[0,390][1080,1716]']//*[contains(@text,'{}')]".format(click_text)
        while True:
            try:
                # 找一次元素
                self.base_find(loc, timeout=2).click()
                print("找到元素啦！")
                break
            except:
                print("当前页面没有找到！")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 判断 是否滑到最后一屏幕
            if self.page_source == self.driver.page_source:
                print("滑不动啦！")
                # 抛出异常
                raise NoSuchElementException
            else:
                # 否则，更新下之前的变量值
                self.page_source = self.driver.page_source
