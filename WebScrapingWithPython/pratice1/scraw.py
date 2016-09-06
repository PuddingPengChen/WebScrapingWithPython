#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-09-05 00:19:36
# @Last Modified by:   anchen
# @Last Modified time: 2016-09-06 22:36:03
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObject = BeautifulSoup(html.read())
        title = bsObject.body.h1
    except AttributError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title==None:
    print("Title could not be found")
else:
    print(title)