# -*- coding: utf-8 -*-
# 使用HEAD 来检查网页是否存在

import argparse
import httplib
import urlparse
import re
import urllib

DEFAULT_URL = 'http://www.python.org'
HTTP_GOOD_CODES = [httplib.OK,httplib.FOUND,httplib.MOVED_PERMANENTLY]

def get_server_status_code(url):
    """
    下载链接的头
    返回服务器的状态码
    """
    host,path = urlparse.urlparse(url)[1:3]
    try:
        conn = httplib.HTTPConnection(host)
        conn.request('HEAD',path)
        return conn.getresponse().status
    except StandardError:
        return None

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Example HEAD Request')
    parser.add_argument('--url',action='store',dest='url',default=DEFAULT_URL)
    given_args = parser.parse_args()
    url = given_args.url

    if get_server_status_code(url) in HTTP_GOOD_CODES:
        print "Server :%s status is OK" %url
    else:
        print "Server: %s status is NOT OK "%url