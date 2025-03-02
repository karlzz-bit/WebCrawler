import requests
from lxml import etree
from bs4 import BeautifulSoup
url='https://www.zhihu.com/hot'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
r=requests.get(url,headers=headers)
tree=etree.HTML(r.text)
title=tree.xpath('//div/a/text()')
print(title)
# soup = BeautifulSoup(r.text, 'html.parser')
#
# # 使用BeautifulSoup提取标题文本
# titles = soup.select('.HotItem-content > a > h2')
# for title in titles:
#     print(title.get_text())
