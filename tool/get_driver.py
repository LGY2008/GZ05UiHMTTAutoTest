from selenium import webdriver
import appium.webdriver
import page


class GetDriver:
    __driver = None
    __app_driver = None

    # 获取 web driver
    @classmethod
    def get_web_driver(cls, url):
        if cls.__driver is None:
            # 获取浏览器对象
            cls.__driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__driver.maximize_window()
            # 打开url
            cls.__driver.get(url)
        return cls.__driver

    # 关闭 web driver
    @classmethod
    def quit_web_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            # 吭
            cls.__driver = None

    # 获取 app driver
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # server 启动参数
            desired_caps = {}
            # 设备信息
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'emulator-5554'
            # app的信息 /
            desired_caps['appPackage'] = page.appPackage
            desired_caps['appActivity'] = page.appActivity
            # 中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 不重置应用
            desired_caps['noReset'] = False
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls.__app_driver

    # 关闭 app driver
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            # 置空
            cls.__app_driver = None
