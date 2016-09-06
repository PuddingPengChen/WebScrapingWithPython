#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-09-06 22:40:02
# @Last Modified by:   anchen
# @Last Modified time: 2016-09-06 22:44:04
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

# find的具体用法，参照API文档或者在后面的项目中积累
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)