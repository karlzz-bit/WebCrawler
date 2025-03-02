'''
xpath解析原理
    -实例化一个etree的对象
    -调用etree对象中的xpath
实例化一个etree对象
    -将本地的html文档加载到etree对象中
        etree.parse(filePath)
    -可以将从互联网上获取的源码数据加载该对象中
        etree.HTML('page_text')
xpath表达式
    - / 表示的是从根节点开始定位，表示的是一个层级
    - // 表示的是多个层级 可以表示从任意位置开始定位
    -属性定位  //tag[@attrName="attrValue"]
    -索引定位   //tag[@attrName="attrValue"]p[1] 索引时从1开始的
    -取文本
        - /text()  标签的直系内容
        - //text() 标签中所有的内容
    -取属性
        -/@attrName

'''
from lxml import etree
tree=etree.parse('sogou.html',etree.HTMLParser())
r=tree.xpath('//div[@class="top-nav"]//li/a//@href')
print(r)