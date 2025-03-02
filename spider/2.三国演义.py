import requests
from bs4 import BeautifulSoup
url='https://www.shicimingju.com/book/sanguoyanyi.html'
headers={'User-Agent':'Mozilla/5.0 ( 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
response = requests.get(url,headers=headers).content
soup = BeautifulSoup(response,'lxml')
li_list=soup.select('.book-mulu>ul>li')
fp=open('./book.txt','w',encoding='utf-8')
for li in li_list:
    title=li.a.string
    detail_url='https://www.shicimingju.com/'+li.a['href']
    detail_page=requests.get(url=detail_url,headers=headers).content
    detail_soup = BeautifulSoup(detail_page,'lxml')
    div_tag=detail_soup.find('div',class_='chapter_content')
    content=div_tag.text
    fp.write(title+'\t'+content+'\n')
    print(title+'   爬取成功')