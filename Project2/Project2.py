import wordcloud

myWordCloud = wordcloud.WordCloud()
with open('trump.txt', encoding='utf-8') as f:
    myWordCloud.generate(f.read())
myWordCloud.to_file('twitter.png')

myWordCloud = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='white',
    font_path='msyh.ttc'
)

import imageio
myMask = imageio.imread("twitter.png")
myWordCloud = wordcloud.WordCloud(mask=myMask)