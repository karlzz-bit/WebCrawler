import json
import re
import requests
from bs4 import BeautifulSoup
# a=input("请输入BV号:")
a='BV1n1421d7e3/'
url = 'https://www.bilibili.com/video/{}'.format(a)
response = requests.get(url)
cookie = "buvid3=5C5D0069-031F-2213-8E11-3B17C971719F69389infoc; b_nut=1688698369; _uuid=7F76CBFD-ADE2-44103-424C-D73D5E9ACC2869255infoc; header_theme_version=CLOSE; CURRENT_FNVAL=4048; buvid4=780B8373-C6A6-6800-F372-7CF18F799AE570981-023070710-7YWVed7pFp%2FuoShCfdfYnQ%3D%3D; DedeUserID=175444232; DedeUserID__ckMd5=b4a676bf5d8afe1c; rpdid=|(k|)mum~~uJ0J'uY))~|uklm; LIVE_BUVID=AUTO5916888971292528; SESSDATA=6b25c9b2%2C1705192174%2Cba23f%2A71bQR5hFBMOt8AXYHjziKE4HOwWw6Ei8wrCIByshPnLAkTd2jwLJy4WYgVkViOyIUPNssSUQAAIAA; bili_jct=e29211bb7e88730fc2bc6691218d247e; sid=858nix09; FEED_LIVE_VERSION=V8; buvid_fp_plain=undefined; hit-new-style-dyn=1; hit-dyn-v2=1; i-wanna-go-back=-1; b_ut=5; fingerprint=b2371c9349b15d5ad60e75cd01f7dc55; buvid_fp=5b9a1047d9ef9ba48290adcd4ba39e58; share_source_origin=copy_web; bsource=share_source_copylink_web; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY0NzMzNjcsImlhdCI6MTY5NjIxNDEwNywicGx0IjotMX0.D2ixQib5vaXOyxTBLWhIR8KzpbGQloGjxzXDgnOum3E; bili_ticket_expires=1696473307; CURRENT_QUALITY=80; b_lsid=4F245FCD_18AFACA514A; home_feed_column=5; browser_resolution=1552-827; bp_video_offset_175444232=848638555060174904; PVID=1"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",

    # Referer: 防盗链。用于告诉服务器我是从哪个链接跳转来的。
    'Referer': 'https://www.bilibili.com/v/popular/all/?spm_id_from=333.1007.0.0',
    'Cookie': cookie
}
response=requests.get(url,headers=headers)

# print(response.text)
bs=BeautifulSoup(response.text,'lxml')
title=bs.findAll('h1',class_='video-title special-text-indent')[0].get("data-title")
print(title)
play_info=re.findall('<script>window.__playinfo__=(.*?)</script>',response.text)[0]
# print(play_info)
# print(type(play_info))
json_data=json.loads(play_info)
# print(json_data)
audio_url=json_data['data']['dash']['audio'][0]['baseUrl']
video_url=json_data['data']['dash']['video'][0]['baseUrl']
print(audio_url)
print(video_url)
audio_content=requests.get(url=audio_url,headers=headers).content
video_content=requests.get(url=video_url,headers=headers).content
with open(title+'.mp3','wb') as fa:
    fa.write(audio_content)
with open(title+'.mp4',mode='wb') as fv:
    fv.write(video_content)
print(title,'保存成功')
