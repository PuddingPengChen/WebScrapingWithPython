# -*- coding: utf-8 -*-
# 通过代理发送请求
import urllib

URL = 'https://www.github.com'
PROXY_ADDRESS = '165.24.10.8:8080'

if __name__=='__main__':
    resp = urllib.urlopen(URL,proxies={"http":PROXY_ADDRESS})
    print "Proxy server return response headers:%s " %resp.headers