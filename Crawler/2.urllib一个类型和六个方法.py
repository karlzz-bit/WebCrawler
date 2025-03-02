import urllib.request

url="http://www.baidu.com"

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(url)

#一个类型和六个方法
print(type(response))#<class 'http.client.HTTPResponse'>

#按照一个字节一个字节的去读
# content=response.read()
# print(content)


#返回多少个字节
content=response.read(5)
print(content)

#读取一行
content=response.readline()
print(content)

#读取一行到结束
# content=response.readlines()
# print(content)


#返回状态码
print(response.getcode())
#返回的是url的地址
print(response.geturl())
#返回状态信息
print(response.getheaders())