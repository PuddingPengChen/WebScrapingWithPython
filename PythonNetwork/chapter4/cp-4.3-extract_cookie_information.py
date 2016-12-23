# -*- coding: utf-8 -*-

import cookielib
import urllib
import urllib2

ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = 'you@email.com'
PASSWORD = 'mypassword'
LOGIN_URL = 'http://bitbucket.org/account/signin/?next=/'
NORMAL_URL = 'http://bitbucket.org/'

def extract_cookie_info():

    #设置cookie-jar
    cj = cookielib.CookieJar()
    #记住urllib.urlencode这个API
    login_data = urllib.urlencode({ID_USERNAME : USERNAME,ID_PASSWORD : PASSWORD})

    #创建 url 的open
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    resp = opener.open(LOGIN_URL,login_data)

    #发送登陆信息
    for cookie in cj:
        print "+++++ First time cookie: %s --> %s" %(cookie.name,cookie.value)
    print "Header : %s " %resp.headers

    #再次登陆，不加入任何登陆信息
    resp = opener.open(NORMAL_URL)
    for cookie in cj:
        print "++++++ Second time cookie :%s ------> %s" %(cookie.name,cookie.value)

    print "Header :%s " % resp.headers

if __name__=='__main__':
    extract_cookie_info()
