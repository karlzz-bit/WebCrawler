import requests
from bs4 import BeautifulSoup
url ="https://movie.douban.com/top250"
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
for start_num in range(0,250,25):
    re=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=headers)
    html=re.text
    soup=BeautifulSoup(html,"html.parser")
    sou=soup.find_all("span",attrs={"class":"title"})
    for it in sou:
        title=it.string
        if "/" not in title:
            print(it.string)