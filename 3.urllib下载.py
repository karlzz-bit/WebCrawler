import urllib.request

#下载一个网页
url_page="http://www.baidu.com"
urllib.request.urlretrieve(url_page,'baidu.html')
#下载图片
urm_img='https://n.sinaimg.cn/sinacn/w1920h1200/20180312/5770-fyscsmu5356120.jpg'
urllib.request.urlretrieve(url=urm_img,filename='lock.jpg')
#下载视频
url_video='https://vdept3.bdstatic.com/mda-qd1ehzbqmm1frnex/sc/cae_h264/1712053083600893164/mda-qd1ehzbqmm1frnex.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1713691885-0-0-a4a743a7b85c27fb4b02378057da8697&bcevod_channel=searchbox_feed&cr=2&cd=0&pd=1&pt=3&logid=1885158936&vid=15375334789626659061&klogid=1885158936&abtest='
urllib.request.urlretrieve(url_video,"video.mp4")
