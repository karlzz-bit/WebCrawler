import os
import requests
from lxml import etree
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def rebuilt_Language(url, headers):
    response = requests.get(url=url, headers=headers, verify=False)
    return response


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    src_list = []
    img_name_list = []

    for pageNum in range(1, 3):
        new_url = url % pageNum
        page_text = rebuilt_Language(url=new_url, headers=headers).text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="wrap clearfix"]//li')
        for li in li_list:
            src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
            src_list.append(src)
            img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            img_name_list.append(img_name)

    for i, img_url in enumerate(src_list):
        try:
            img_data = requests.get(url=img_url, headers=headers).content
            img_name = img_name_list[i]
            img_path = os.path.join('picLibs', img_name)
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name + '下载成功！')
        except Exception as e:
            print(f"下载 {img_name} 时出现异常：{e}")
