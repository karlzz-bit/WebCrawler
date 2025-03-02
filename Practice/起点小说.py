import requests
from bs4 import BeautifulSoup
fileWriter = open("./my.txt","w")

cookies = {
    'w_tsfp': 'ltvgWVEE2utBvS0Q6KjulUOpHjE7Z2R7xFw0D+M9Os09AqQjU56E2YVzudfldCyCt5Mxutrd9MVxYnGDUdQkfRAcQ86Ub5tH1VPHx8NlntdKRQJtA57aWgYecb93uDJAdD9bLBS0ij52LNcUnrE1iA8O4CR237ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgWyEtBu/eRlhAcxD0Eab1CweCXkm9BPNc+FeNh+pJMarTe9Gvy/hk2upNdLxiEox60I3sB49AtX02TXKL3ZEIAtrZViygr4ke66rNuYluTEZXL5TWwpN/FxC9qdk605dDS20YnyGDawpsQcIQPRb+8+ueCzAh5nuJQxQ74kuxA4l9g==',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

def save_article(charpterName, content_elements):
    fileWriter.write(charpterName+"\n")
    for element in content_elements:
        line = element.get_text()
        fileWriter.write(line+"\n")
    fileWriter.write("\n\n\n")

def get_page(href):
    response = requests.get(href, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    charpterName = soup.select("h1.title")[0].get_text()
    print(charpterName)
    content_elements = soup.select("main p")
    save_article(charpterName,content_elements)
    buttons = soup.select("a.nav-btn")
    for button in buttons:
        if(button.get_text()=="下一章"):
            next_href = "https:" + button['href']
            get_page(next_href)

get_page("https://www.qidian.com/chapter/1039141715/783334210/")
fileWriter.close()
