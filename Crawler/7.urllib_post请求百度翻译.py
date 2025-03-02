#post请求
import urllib.request

url='https://fanyi.baidu.com/sug'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
data={
    'kw':'spider'
}
#post请求的参数    必须要进行编码
data=urllib.parse.urlencode(data).encode('utf-8')
#post的请求的参数  是不会拼接在url的后面的  而是需要放在请求对象定制的参数中
#post请求的参数必须进行编码字节码
request=urllib.request.Request(url=url,data=data,headers=headers)
print(request)
response = urllib.request.urlopen(request)
print(response)
content=response.read().decode('utf-8')
print(content)
print(type(content))
import json
obj=json.loads(content)
print(obj)#字符串-->json