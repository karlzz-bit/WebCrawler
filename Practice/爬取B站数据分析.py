import os
import re
from wordcloud import WordCloud

# 遍历文件夹，提取图片名称
image_folder = './downloaded_images'
image_names = []
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # 根据实际情况修改文件扩展名
        image_names.append(re.sub(r'\.jpg$|\.png$', '', filename))  # 提取文件名，去除扩展名

print("将图片名称保存到文本文件")
with open('downloaded_images.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(image_names))

print("使用词云生成工具生成词云")
text = ' '.join(image_names)
wordcloud = WordCloud().generate(text)
font_path = "C:/Windows/Fonts/msyh.ttc"  # Microsoft YaHei UI 字体文件路径
wordcloud = WordCloud(width=800, height=400, background_color="white", font_path=font_path).generate(text)
# 保存词云图片
wordcloud.to_file('downloaded_images_wordcloud.png')
