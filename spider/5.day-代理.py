'''
什么是代理：
    -代理服务器
代理的作用：
    -突破自身IP访问的限制
    -隐藏自身真实的IP
代理相关网站：
代理ip的类型：
    -https
    -http
'''
import requests
url='https://www.baidu.com/s?wd=ip查询'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
page_text=requests.get(url,headers=headers).text
with open('ip.html','w',encoding='utf-8') as f:
    f.write(page_text)
