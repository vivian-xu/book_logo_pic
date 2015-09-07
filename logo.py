# -*- Encoding: utf-8 -*-

from httplib2 import Http
import os
import re

h = Http()

#31个以书籍为主题的logo设计作品
url1 = "http://www.duidea.com/2012/1113/1877.html"
rsp,content = h.request(url1)

ptn1 = re.compile(ur'<div class="entry_content">(.*?)<div id="show-ad-3">',re.DOTALL)
pic_ptn = re.compile(ur'<img.*?src="(http.*?.jpg)".*?/>')
pic_ret1 = []

ret1 = ptn1.findall(content)

for i in ret1:
    ret2 = pic_ptn.findall(i)
    for j in ret2:
        pic_ret1.append(j)

# 保存在 pic_ret1中



# 以书为元素的logo

# 首页

url2 = "http://www.3lian.com/show/2011/04/5707.html"
rsp,content = h.request(url2)
pic_ret2 = []

ptn2 = re.compile(ur'<img border="0" src="(.*?)" alt',re.DOTALL)
pic_ret2 = ptn2.findall(content)

# 2-4页

for i in range(2,5):
    url2 = "http://www.3lian.com/show/2011/04/5707_%d.html" %i
    rsp,content = h.request(url2)
    for m in ptn2.findall(content):
        pic_ret2.append(m)

# 最终，输出在pic_ret2中


# Office Vectors
url3 = "http://www.webdesigndev.com/free-office-vectors/"
rsp,content = h.request(url3)
pic_ret3 = []

ptn3 =  re.compile(ur'<img.*?src="(http.*?jpg)" alt.*?/><noscript',re.DOTALL)
pic_ret3 = ptn3.findall(content)    #结果输出在pic_ret3中

# Professional PSD Cards

url4 = "http://www.webdesigndev.com/professional-psd-cards-download/"
rsp,content = h.request(url4)
pic_ret4 = []

ptn4 =  re.compile(ur'<img.*?src="(http.*?jpg)" alt.*?/><noscript')
pic_ret4 = ptn4.findall(content)    # 存在pic_ret4中



# 输出到子目录文件夹 logo 中。

pic_ret = [pic_ret1,pic_ret2,pic_ret3,pic_ret4]
if 'logo' not in os.listdir('./'):
    os.makedirs('logo')

for item in pic_ret:
    for purl in item:
        rs,content = h.request(purl)
        path =  os.path.basename(purl)
        if path not in os.listdir('./logo'):
            with open('logo'+'/'+path,'wb') as f:
                f.write(content)




