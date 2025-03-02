import requests
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
cookie_str = 'buvid3=A62BF59C-9D3C-9F01-830C-0B8A03CE8C6371193infoc; b_nut=1707140773; _uuid=655577F6-E75D-51101-261010-E38BCC55723B77455infoc; CURRENT_BLACKGAP=0; DedeUserID=169432525; DedeUserID__ckMd5=59a697c412a323c7; rpdid=0zbfAHP156|19zL3kT5M|21|3w1RwZlc; buvid4=22F3C5D8-5023-0DF1-C7AB-59672BCC917071193-024020513-%2BnMST1LsU9crlkXQNDIeLFSB3v2ps9theFiqVYkB8u%2FMFiizBaHzugcj3Tman3j%2B; enable_web_push=DISABLE; header_theme_version=CLOSE; buvid_fp_plain=undefined; FEED_LIVE_VERSION=V8; CURRENT_QUALITY=80; hit-dyn-v2=1; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQwMTEwNDUsImlhdCI6MTcxMzc1MTc4NSwicGx0IjotMX0.SNRIZYjNQo7ViJupaG5vWluijCgGy55rrWnkWCKh9ro; bili_ticket_expires=1714010985; SESSDATA=7cdd81eb%2C1729321511%2C8b8da%2A41CjAtoJFM7JfI5BVLfhRKj_Zz_JQ9A7_rIr5GsU-bPOobAPY9btw0EX7DjwxUMC_viYQSVkdEQlBGLTd3VDRJZUwwVHhaeV82TWVsUWhyOEY4Y1FqU1c3TEtBQVlpM3RKY1ZmbF9MMTBIaHRCMllscTcyNnVZaE5zOEdRUkx1Smhoc3ZlTHFSeDRnIIEC; bili_jct=7f24d75496fcaefa28563d0784eb7b16; PVID=1; b_lsid=2E5103586_18F0924D753; bp_video_offset_169432525=923445654051618825; fingerprint=54017f74e69e81a0bb37f29857bbd314; buvid_fp=54017f74e69e81a0bb37f29857bbd314; home_feed_column=5; browser_resolution=2048-983'
cookie_dict = {}
for item in cookie_str.split("; "):
    key, value = item.split("=")
    cookie_dict[key] = value
cookies=cookie_dict
with open("./title.txt", "w", encoding="utf-8") as fs:
    for i in range(1, 11):
            url = 'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={}&web_location=333.934&w_rid=769d396f9f77d59da71a1ed7276b89c0&wts=1713882341'.format(i)
            response = requests.get(url, cookies=cookies, headers=headers)
            data = json.loads(response.text)
            titles = [media.get('title', 'Title Not Found') for media in data['data'].get('medias', [])]
            fs.write("\n".join(titles) + "\n")
            print("第{}页完成".format(i))
# url = 'https://api.bilibili.com/x/v3/fav/resource/list?media_id=52586825&pn=1&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web'
# response = requests.get(url, cookies=cookies, headers=headers)
# data = json.loads(response.text)
# titles = [media.get('title', 'Title Not Found') for media in data['data'].get('medias', [])]
# print(titles)
#读取标题文件内容
with open("./title.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 生成词云
font_path = "C:/Windows/Fonts/msyh.ttc"  # Microsoft YaHei UI 字体文件路径
wordcloud = WordCloud(width=800, height=400, background_color="white", font_path=font_path).generate(text)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

