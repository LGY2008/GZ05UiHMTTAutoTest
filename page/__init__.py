from selenium.webdriver.common.by import By

from tool.read_yaml import read_yaml

"""url配置数据"""
# 自媒体
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"

"""app配置数据"""
appPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity"
"""用例依赖业务数据"""
# 文章title
title = read_yaml("mp_article.yaml")[0][0]
# 文章频道
channel = "数据库"
# 文章id
article_id = None

"""以下为mp页面配置数据"""
# 用户名
mp_username = By.CSS_SELECTOR, "[placeholder='请输入手机号']"
# 密码
mp_pwd = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录按钮
mp_login_btn = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"
# 点击内容管理
mp_content_manage = By.XPATH, "//ul[@role='menubar']//*[text()='内容管理']/.."
# 点击发布文章
mp_publish_article = By.XPATH, "//ul[@role='menubar']//*[contains(text(),'发布文章')]"
# 输入文章标题
mp_title = By.XPATH, "//*[@placeholder='文章名称']"
# 输入文章内容
# iframe id
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
mp_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面
mp_auto = By.XPATH, "//*[text()='自动']"
# 选择频道  （7:为数据库）
mp_channel = By.XPATH, "//*[@placeholder='请选择']"
# 选择具体频道
mp_click_channel = By.XPATH, "//*[text()='数据库']/.."
# 点击发表
mp_confirm = By.XPATH, "//*[text()='发表']/.."
# 获取发表提示信息 （新增文章成功)
mp_result = By.XPATH, "//*[text()='新增文章成功']"

"""以下为mis页面配置数据"""
# 用户名
mis_username = By.CSS_SELECTOR, "[placeholder='用户名']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[placeholder='密码']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 昵称
mis_nickname = By.CSS_SELECTOR, ".user_info>span"
# 信息管理
mis_info_manage = By.XPATH, "//a[text()='信息管理']"
# 点击内容审核
mis_manage_audit = By.XPATH, "//a[text()='内容审核']"
# 输入文章标题
mis_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 输入文章频道
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 查询按钮
mis_find = By.CSS_SELECTOR, ".find"
# 文章id
mis_article_id = By.CSS_SELECTOR, ".cell>span"
# 通过
mis_pass_btn = By.XPATH, "//span[text()='通过']/.."
# 确定
mis_confirm = By.CSS_SELECTOR, ".el-button--primary"

"""以下为app页面配置数据"""
# 用户名
app_username = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
# 密码
app_pwd = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
# 登录按钮
app_login_btn = By.XPATH, "//*[@class='android.widget.Button' and @text='登录']"
# 我的
app_me = By.XPATH, "//*[@index='3' and contains(@text,'我的')]"
# 频道区域
app_channel_area = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
# 文章区域
app_article_area = By.XPATH, "//*[@bounds='[0,390][1080,1716]']"