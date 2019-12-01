#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:03:39 2019

@author: xingjiawen
"""
#%%
# 爬取12345建议网站
# Part I 爬取前一千条的标题、详情、回复时间、提问时间、回复内容、部门
# Part II Version 1 爬取现在到2019/1/1的、标题含垃圾二字的标题、详情、回复时间、提问时间、回复内容、部门
# Part II Version 2 爬取现在到2019/1/1的、内容含垃圾二字的标题、详情、回复时间、提问时间、回复内容、部门

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json
#%%
# 获取索引页的信息
base_url = 'http://www.sh12345.gov.cn/selectPublicRpinfo.jspx?page='
page = 1

# 设置 Response Headers 的 Referer。
headers = {}
headers['Referer'] = 'http://www.sh12345.gov.cn/r/cms/www/shline12345/appeal_public.html'
#%%
#############################################################
# Part I 爬取前一千条的标题、详情、回复时间、提问时间、回复内容、部门 #
#############################################################
number = 1000 # 爬取问题条数
titles = [] # 问题标题
contents = [] # 问题详情
ftimes = [] # 回复时间
stimes = [] # 提问时间
replies = [] # 回复内容
depts = [] # 部门

while len(titles) < number:
    url = base_url + str(page)
    page = page + 1
    res = requests.get(url, headers = headers)
    res.encoding = 'UTF-8'
    if res.status_code == 200:
        html = res.text
        myjson = json.loads(html) # 一个json对象。
        rl = myjson['returnList']
        for i in rl:
            # each i is a dict
            titles.append(i['relTitle'])
            contents.append(i['content'])
            ftimes.append(i['createTime'])
            stimes.append(i['startTime'])
            replies.append(i['reply'])
            depts.append(i['struName'])

print('Get',len(titles), 'suggestions !') # 

#%%
# 储存上一部分爬取的内容
with open('/Users/xingjiawen/OneDrive/文档/SJTU/2019-2020Autumn/大数据分析/12345.txt','w') as f:
    i = 0
    while i < len(titles):
        f.writelines([titles[i], ';', contents[i], ';', ftimes[i],';', stimes[i], ';', replies[i], ';', depts[i], '\n'])
        i = i + 1
print('Finished.', len(titles),'questions crawled.')

#%%
#############################################################################################
# Part II Version 1 爬取现在到2019/1/1的、标题含垃圾二字的标题、详情、回复时间、提问时间、回复内容、部门 #
#############################################################################################
# 到第32页
ttitles = [] # 问题标题
tcontents = [] # 问题详情
tftimes = [] # 回复时间
tstimes = [] # 提问时间
treplies = [] # 回复内容
tdepts = [] # 部门
page = 1

while page < 33:
    url = base_url + str(page)
    page = page + 1
    res = requests.get(url, headers = headers)
    res.encoding = 'UTF-8'
    if res.status_code == 200:
        html = res.text
        myjson = json.loads(html) # 一个json对象。
        rl = myjson['returnList']
        for i in rl:
            # each i is a dict
            if '垃圾' in i['relTitle']:
                ttitles.append(i['relTitle'])
                tcontents.append(i['content'])
                tftimes.append(i['createTime'])
                tstimes.append(i['startTime'])
                treplies.append(i['reply'])
                tdepts.append(i['struName'])

print('Get',len(ttitles), 'suggestions !') # Get 60 suggestions !
print('从2019/1/1至今，共有',len(ttitles),'条标题含有“垃圾”二字的建议。') # 从2019/1/1至今，共有 60 条标题含有“垃圾”二字的建议。

#%%
# 储存上一部分爬取的内容。存入txt。
with open('/Users/xingjiawen/OneDrive/文档/SJTU/2019-2020Autumn/大数据分析/12345垃圾in标题.txt','w') as f:
    i = 0
    while i < len(ttitles):
        f.writelines([ttitles[i], ';', tcontents[i], ';', tftimes[i],';', tstimes[i], ';', treplies[i], ';', tdepts[i], '\n'])
        i = i + 1
print('Finished.', len(ttitles),'questions crawled.') # Finished. 60 questions crawled.

#%%
#############################################################################################
# Part II Version 2 爬取现在到2019/1/1的、内容含垃圾二字的标题、详情、回复时间、提问时间、回复内容、部门 #
#############################################################################################
# 到第32页
tttitles = [] # 问题标题
ttcontents = [] # 问题详情
ttftimes = [] # 回复时间
ttstimes = [] # 提问时间
ttreplies = [] # 回复内容
ttdepts = [] # 部门
page = 1

while page < 33:
    url = base_url + str(page)
    page = page + 1
    res = requests.get(url, headers = headers)
    res.encoding = 'UTF-8'
    if res.status_code == 200:
        html = res.text
        myjson = json.loads(html) # 一个json对象。
        rl = myjson['returnList']
        for i in rl:
            # each i is a dict
            if '垃圾' in i['content']:
                tttitles.append(i['relTitle'])
                ttcontents.append(i['content'])
                ttftimes.append(i['createTime'])
                ttstimes.append(i['startTime'])
                ttreplies.append(i['reply'])
                ttdepts.append(i['struName'])

print('Get',len(tttitles), 'suggestions !') # Get 79 suggestions !
print('从2019/1/1至今，共有',len(tttitles),'条内容含有“垃圾”二字的建议。') # 从2019/1/1至今，共有 79 条内容含有“垃圾”二字的建议。
#%%
# 储存上一部分爬取的内容。存入txt。
with open('/Users/xingjiawen/OneDrive/文档/SJTU/2019-2020Autumn/大数据分析/12345垃圾in内容.txt','w') as f:
    i = 0
    while i < len(tttitles):
        f.writelines([tttitles[i], ';', ttcontents[i], ';', ttftimes[i],';', ttstimes[i], ';', ttreplies[i], ';', ttdepts[i], '\n'])
        i = i + 1
print('Finished.', len(tttitles),'questions crawled.') # Finished. 79 questions crawled.
