#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-09-11 22:05:58
# @Last Modified by:   anchen
# @Last Modified time: 2016-09-12 21:37:29

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(articleUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 说明遇到新的页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                # 使用递归继续爬下去
                getLinks(newPage)

getLinks("")
