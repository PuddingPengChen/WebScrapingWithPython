# -*- coding: utf-8 -*-
#request库是一个非常强大的库，这个demo只能简单的运行而已，更多
#更详细的说明，要参考request的官方说明文档。
#http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

import requests
import urllib
import urllib2

ID_USERNAME = 'signup-user-name'
ID_EMAIL = 'signup-user-email'
ID_PASSWORD = 'signup-user-password'
USERNAME = 'username'
EMAIL = 'you@email.com'
PASSWORD = 'yourpassword'
SIGNUP_URL = 'https://twitter.com/account/create'

def submit_form():

    payload = {ID_USERNAME: USERNAME,
        ID_EMAIL   : EMAIL,
        ID_PASSWORD: PASSWORD,}

    resp = requests.get(SIGNUP_URL)
    print "Request to GET request:%s" %resp.content

    resp = requests.post(SIGNUP_URL,payload)
    print "Headers from a POST request response: %s " %resp.headers

if __name__ =='__main__':
    submit_form()
