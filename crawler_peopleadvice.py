#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:03:39 2019

@author: xingjiawen
"""

# 爬取人民建议征集网站
# Part I 爬取前一千条的标题、超链接、时间
# Part II 爬取现在到2019/1/1的、标题含垃圾二字的标题、超链接、时间

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

u21 = 'http://wsxf.sh.gov.cn/xf_rmyjzj/list.aspx?nav=&pageindex='
index = 1
u22 = '&pagesize=20' # 第一页的网址： u21 + str(index) + u22

######################################
# Part I 爬取前一千条的标题、超链接、时间 #
######################################
titles2 = [] # 接收标题
hrefs2 = [] # 接收超链接
finishtimes2 = [] # 接收完结时间
number = 1000 # 想爬取的问题数目
while len(titles2) < number:
    url = u21 + str(index) + u22
    index = index + 1
    res = requests.get(url)
    if res.status_code == 200:
        html = res.text
        mysoup = BeautifulSoup(html,'lxml')
        question_list = mysoup.find('ul', attrs = {'class':'list'}).find_all('li') # 包含了当前页面所有的问题相关的信息

        for item in question_list:
            # 提取建议标题
            title2 = item.find('a').getText()  # 提取标题
            titles2.append(title2)
            # 提取建议超链接
            href2 = item.find('a')['href'] # 提取超链接
            hrefs2.append('http://wsxf.sh.gov.cn/xf_rmyjzj/' + href2)
            # 提取时间
            time2 = item.find('span').next_sibling.next_sibling.getText()
            finishtimes2.append(time2)

print('Get',number, 'suggestions !') # Get 1000 suggestions !

# 储存上一部分爬取的内容
with open('/Users/xingjiawen/OneDrive/文档/SJTU/2019-2020Autumn/大数据分析/renminjianyi.txt','w') as f:
    i = 0
    # 第 i 次写入第 i 个问题的三个属性
    # titles2 = []，hrefs2 = []，finishtimes2 = []
    while i < len(titles2):
        f.writelines([titles2[i], ';', hrefs2[i], ';', finishtimes2[i], '\n'])
        i = i + 1
print('Finished.', len(titles2),'questions crawled.')

############################################################
# Part II 爬取现在到2019/1/1的、标题含垃圾二字的标题、超链接、时间 #
############################################################
trashtitles = []
trashhrefs = []
trashfinishtimes = []

while index < 88:
    url = u21 + str(index) + u22
    index = index + 1
    res = requests.get(url)
    if res.status_code == 200:
        html = res.text
        mysoup = BeautifulSoup(html,'lxml')
        question_list = mysoup.find('ul', attrs = {'class':'list'}).find_all('li') # 包含了当前页面所有的问题相关的信息

        for item in question_list:
            # 提取建议标题
            title = item.find('a').getText()
            if '垃圾' in title: # 只针对标题中含有垃圾二字的进行操作
                trashtitles.append(title)
                # 提取建议超链接
                href = item.find('a')['href'] # 提取超链接
                trashhrefs.append('http://wsxf.sh.gov.cn/xf_rmyjzj/' + href)
                # 提取时间
                time = item.find('span').next_sibling.next_sibling.getText()
                trashfinishtimes.append(time)

print('Get',len(trashtitles), 'suggestions !') # Get 162 suggestions !

# 爬取垃圾相关问题的二级网页。
for u in trashhrefs:
    trashres = requests.get(u)
    if trashres.status_code == 200:
        trashhtml = trashres.text
        trashsoup = BeautifulSoup(trashhtml, 'lxml')
        # ……没写完
############################################################以下是参考的代码。
        # 进入二级网页提取问题类别、阅读数
        for href in q_href:
            q_res = requests.get(href)
            if q_res.status_code == 200:
                q_html = q_res.text
                q_soup = BeautifulSoup(q_html, 'lxml')
                # 提取问题类别
                type_of_q = q_soup.find('ul', attrs = {'class':'label detail-tag'}).find_all('li')
                tq = []
                for i in type_of_q:
                    t = i.getText()
                    tq.append(t)
                types.append(tq)
                # 提取问题阅读数
                reader = q_soup.find('span', attrs = {'class':'absoulte-img'}).find('a').getText()
                readers.append(reader)


            else:
                print(page, res.status_code)
                break
