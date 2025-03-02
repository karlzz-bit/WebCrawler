import requests
from bs4 import BeautifulSoup

url = "https://www.163.com/money/article/GJM85863002580S6.html"
# 添加伪装的浏览器头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

print("==========================================")
# 获取新闻标题
titles = soup.select(".post_main .post_title")
print("标题：" + titles[0].text)

# 获取新闻来源
print("==========================================")
sources = soup.select(".post_info a")
print("来源：" + sources[0].text)

# 获取新闻发布时间
print("==========================================")
date = soup.select(".post_info")
all_text = date[0].text
date_text =all_text.strip().split(' ')
print("时间：" + date_text[0])

# 获取新闻正文
print("==========================================")
bodies = soup.select(".post_body p")
for p in bodies:
    print("正文：" + p.text.strip())

# 获取新闻发布人
print("==========================================")
publishers = soup.select(".post_author")
publishers_str = publishers[0].text.split("责任编辑：")
print("发布人：" + publishers_str[1].strip())


