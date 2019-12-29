#练习用，非商业

# 爬取网易云音乐
# 导入第三方库
import requests  # 网络库
from bs4 import BeautifulSoup  # 解析网页
from urllib.request import urlretrieve

# 访问指定网址，并下载到本地
# 爬取思路
# 1、明git 确目标
# https://music.163.com/#/playlist?id=2874240574
# 第一步
# url = 'https://link.hhtjim.com/163/141178409.mp3'
# result = requests.get(url).content
# # w保存到本地
# with open('欧若拉.mp3', 'wb') as file:
#     file.write(result)
# 歌单地址
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
# Accept: */*
# headers = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'
# # user-agent:Mozilla/5.0(windows.NT 10.0;WOW64) AppleWcbKit)
# url = 'https://music.163.com/playlist?id=3138801923'
# result = requests.get(url, headers).text
# print(result)
# r = BeautifulSoup(result, 'lxml')
# soup = r.find('ul',class_='f-hide').find_all_next('a')
# soup = r.find('ul', class_='f-hide').find_all_next('a')
# print(soup)
# for i in soup:
#     # print(i['href'][9:])
#     music_ulr = 'https://link.hhtjim.com/163/' + i['href'][9:] + '.mp3'
#     try:
#         urlretrieve(music_ulr, 'music/%s.mp3' % i.text)
#         print('true')
#     except:
#         print('fail')
