#使用urllib来获取百度首页源码
import urllib.request
#定义一个url
url="http://www.baidu.com"

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(url)

#获取响应中的页面的源码
#read方法 返回的是字节形式的二进制数据
#将二进制的数据转换为字符串 解码decode('')
content=response.read().decode("utf-8")



#打印数据
print(content)