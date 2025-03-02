'''
异步爬虫的方式
    -多线程，多进程（不建议）
        -好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞操作就可以异步进行
        -弊端：无法无限制的开启多线程或多进程
    -进程池，线程池（适当使用）
        -好处：我们可以降低系统对进程或者线程创建和销毁的一个频率，从而很好的降低系统的开销
        -弊端：池中线程或进程的数量是有上限的


'''
#线程池的基本使用
#原则：线程池处理阻塞且耗时的操作
import requests
from lxml import etree
from multiprocessing.dummy import Pool
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
url='https://www.pearvideo.com/category_1'
page_text=requests.get(url=url,headers=headers).text
tree =etree.HTML(page_text)
# 获取每个视频链接的a标签
video_links = tree.xpath('//div[@class="vervideo-bd"]//a[@class="vervideo-lilink actplay"]')

for link in video_links:
    # 提取a标签中的唯一文本
    name = link.xpath('string()').strip()
    # 获取视频链接
    detail_url = 'https://www.pearvideo.com/' + link.xpath('@href')[0]+'.mp4'
    detail_page_text=response = requests.get(detail_url,headers=headers).text
    detail_tree = etree.HTML(detail_page_text)
    video_url = detail_tree.xpath('//div[@id="JprismPlayer"]/video/@src')
    print(video_url)