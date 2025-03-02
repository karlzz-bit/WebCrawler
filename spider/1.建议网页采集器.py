import requests
'''
UA:User-Agent (请求载体的身份标识)
UA检测---UA伪装



'''



if __name__ == '__main__':
    url='https://sogou.com/web'
    #处理url携带的参数：封装到字典中
    kw=input("enter a word：")
    param={
        'query':kw
    }
    #UA伪装
    headers={
        'User - Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 123.0.0.0Safari / 537.36'
    }
    response = requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as f:
        f.write(page_text)
    print(fileName,"保存成功！！！")