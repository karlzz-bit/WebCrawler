import requests
from lxml import etree
import os

url = 'http://pic.netbian.com/4kmeinv/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
page_text = response.text
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')

if not os.path.exists("./picLibs"):
    os.mkdir("./picLibs")

for li in li_list:
    img_src = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0] + ".jpg"
    img_name=img_name.encode('iso-8859-1').decode('gbk')
    # 使用 encode('iso-8859-1').decode('gbk') 处理中文乱码可能导致异常，可以直接使用 img_name
    img_data = requests.get(url=img_src, headers=headers).content
    # 处理文件名中的非法字符
    img_name = ''.join(c for c in img_name if c.isalnum() or c in [' ', '.', '_'])
    img_path = './picLibs/' + img_name
    with open(img_path, 'wb') as f:
        f.write(img_data)
    print("下载成功:", img_path)
