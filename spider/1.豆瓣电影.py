import requests
import json
url='https://movie.douban.com/j/chart/top_list'
param={
    'type': '24',
    'interval_id': '100:90',
    'action':' ',
    'start': '0',
    'limit': '20'
}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
response=requests.get(url=url,headers=headers,params=param)
list_data=response.json()
fp=open('./douban.json','w',encoding='utf-8')
json.dump(list_data,fp,ensure_ascii=False)
print('over!!!')