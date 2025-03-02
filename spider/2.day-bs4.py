'''
聚焦爬虫
    -编码流程
        -指定url
        -发起请求
        -获取相应数据
        -数据解析
        -持久化存储

数据解析分类
    -正则
    -bs4
    -xpath(***)

数据解析原理概述

'''

'''
bs4进行数据解析
    -数据解析原理
        -标签定位
        -提取标签，标签属性中存储的数据值
    -bs4数据解析的原理
        -实例化一个BeautifulSoup对象，并且将页面源码加载到该对象中
        -通过调用BeautifulSoup对象中相关的属性或方法进行标签定位和数据提取
    -如何实例化BeautifulSoup
        -将本地的html文档加载
        -将互联网中的html文档加载
'''
import requests
import lxml
from bs4 import BeautifulSoup
fp=open('./sogou.html','r',encoding='utf-8')
soup=BeautifulSoup(fp,'lxml')
print(soup.find("a"))
print(soup.a)
print(soup.find_all(class_="header"))
print(soup.select('.top-nav>ul>li>a')[0].text)#某种选择器
print("====================================")
print(soup.select('.top-nav>ul>li>a')[0].string)#某种选择器
print(soup.select('.top-nav>ul>li>a')[0].get_text())#某种选择器
