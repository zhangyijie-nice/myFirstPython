#练习用，非商业
# 导入库
import requests  # 请求库,通过该库进行网络操作  属性第三方库，要安装
import re  # 正则库 内置库，不需要安装
#我进行了一次修改git
# 明确访问的网页
url = 'http://category.tudou.com/category/c_97_p_1.html?spm=a2h28.8514923.category.5!4~1~3!11~A'
datas = requests.get(url).text  # 获取网页的文本数据
title_urls = re.findall('title="(.*?)"', datas)[1::2]  # 获得所有标题,然后去重,2代表切片步长
# print(datas)  #打印测试
# 筛选出所有的src=后边的字符串
image_urls = re.findall('src="(.*?)"', datas)  # .表示匹配任意一个字符,*贪婪符,表示匹配任意次,?代表非贪婪符
# print(image_urls)
# 定义空列表存储真正的图片下载地址
image_list = []
for image_url in image_urls:
    # print(image_url)
    # 判断image_url是否以http开头
    if image_url.startswith("http"):
        # print(image_url)
        # 每次循环的值都添加到列表中
        image_list.append(image_url)
# 对列表进行切片,切掉第一张小图标
image_list = image_list[1:]
# print(image_list)
n = len(title_urls)
# print(title_urls)
for i in title_urls:  # range(n)一组数字
    # print(title_urls[i])
    # print(image_list[i])
    image_u = image_list[i]
    image = requests.get(image_u).content
    name = title_urls[i]
# print(n,len(image_list))
    # 存储文件
    # ./表示当前目录 %s表示字符串 as后是取名为file
    with open('./%s.jpg' % name, 'wb') as file:
        file.write(image)
