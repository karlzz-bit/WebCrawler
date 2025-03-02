import requests
'''
requests 模块
    -urllib模块
    -requests模块!!!
    模拟浏览器发请求
如何使用
    -指定url
    -发起请求   get post
    -获取响应数据
    -持久化存储
'''
'''
if __name__ == '__main__':
    url = 'https://www.sogou.com/'
    response=requests.get(url)
    print(response)
    page_text=response.text#字符串形式的响应数据
    print(page_text)
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")
'''