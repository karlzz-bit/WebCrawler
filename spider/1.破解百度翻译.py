import requests
import json
if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    word=input('enter a word:')
    data={
        'kw':word
    }
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    response=requests.post(url=post_url,data=data,headers=headers)
    #json()方法返回的是obj
    dic_obj=response.json()
    # print(dic_obj)
    filenName=word+'.json'
    fp=open(filenName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over')