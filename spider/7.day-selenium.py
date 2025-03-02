'''
便捷地获取网站中动态加载的数据
便捷地实现模拟登录
selenium
    基于浏览器自动化的一个模块
selenium使用流程;
    -下载浏览器的驱动程序
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# 设置选项，如启用静默模式等
# options.add_argument("--headless")

bro = webdriver.Chrome('./chromedriver.exe')
