import requests
import json
import os
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
cookie_str = 'buvid3=A62BF59C-9D3C-9F01-830C-0B8A03CE8C6371193infoc; b_nut=1707140773; _uuid=655577F6-E75D-51101-261010-E38BCC55723B77455infoc; CURRENT_BLACKGAP=0; DedeUserID=169432525; DedeUserID__ckMd5=59a697c412a323c7; rpdid=0zbfAHP156|19zL3kT5M|21|3w1RwZlc; buvid4=22F3C5D8-5023-0DF1-C7AB-59672BCC917071193-024020513-%2BnMST1LsU9crlkXQNDIeLFSB3v2ps9theFiqVYkB8u%2FMFiizBaHzugcj3Tman3j%2B; enable_web_push=DISABLE; header_theme_version=CLOSE; buvid_fp_plain=undefined; FEED_LIVE_VERSION=V8; CURRENT_QUALITY=80; hit-dyn-v2=1; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQwMTEwNDUsImlhdCI6MTcxMzc1MTc4NSwicGx0IjotMX0.SNRIZYjNQo7ViJupaG5vWluijCgGy55rrWnkWCKh9ro; bili_ticket_expires=1714010985; SESSDATA=7cdd81eb%2C1729321511%2C8b8da%2A41CjAtoJFM7JfI5BVLfhRKj_Zz_JQ9A7_rIr5GsU-bPOobAPY9btw0EX7DjwxUMC_viYQSVkdEQlBGLTd3VDRJZUwwVHhaeV82TWVsUWhyOEY4Y1FqU1c3TEtBQVlpM3RKY1ZmbF9MMTBIaHRCMllscTcyNnVZaE5zOEdRUkx1Smhoc3ZlTHFSeDRnIIEC; bili_jct=7f24d75496fcaefa28563d0784eb7b16; PVID=1; fingerprint=54017f74e69e81a0bb37f29857bbd314; buvid_fp=54017f74e69e81a0bb37f29857bbd314; bp_video_offset_169432525=923514171630288944; b_lsid=23586C85_18F0B550C87; home_feed_column=4; browser_resolution=1023-983; sid=4vzh1h3l'
cookie_dict = {}
for item in cookie_str.split("; "):
    key, value = item.split("=")
    cookie_dict[key] = value
cookies=cookie_dict
a=int(input("请输入爬取的页数："))
for i in range(1, a):
        url = 'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={}&web_location=333.934&w_rid=769d396f9f77d59da71a1ed7276b89c0&wts=1713882341'.format(i)
        response = requests.get(url, cookies=cookies, headers=headers)
        data = json.loads(response.text)
        video_list = data.get('data', {}).get('list', [])
        for video in video_list:
            title = video.get('title', 'No Title')
            pic = video.get('pic', 'No Pic')
            # print("标题:", title)
            # print("封面图片:", pic)
            img_data = (
                requests.get(url=pic).content)
            folder_path = 'downloaded_images'
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_name = "".join([c for c in title if c.isalpha() or c.isdigit() or c == ' ']).rstrip()
            file_path = os.path.join(folder_path, f"{file_name}.jpg")
            with open(file_path, "wb") as f:
                f.write(img_data)
                print(f"已保存图片：{file_path}")