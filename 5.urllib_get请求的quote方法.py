import urllib.request
import urllib.parse

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
name=urllib.parse.quote('周杰伦')
print(name)
url='https://www.baidu.com/s?wd={}'.format(name)
request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)




