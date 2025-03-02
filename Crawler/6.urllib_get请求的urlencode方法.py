#urlencode 应用场景：多个参数的时候
import urllib.parse
# data={
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'台湾'
# }
# a=urllib.parse.urlencode(data)
# print(a)
import urllib.request
base_url="https://www.baidu.com/s?"
data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'台湾'
}
new_data=urllib.parse.urlencode(data)
print(new_data)
url=base_url+new_data
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)