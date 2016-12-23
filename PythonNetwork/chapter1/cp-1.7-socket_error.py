# -*- coding: utf-8 -*-
#处理socket的错误
# 学习使用了: 1. argparse 模块  2. try-except结构的使用技巧熟悉

import sys
import  socket
import argparse

def main():
    # 设置参数解析
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host',action='store',dest='host',required=False)
    parser.add_argument('--port',action='store',dest='port',type=int,required=False)
    parser.add_argument('--file',action='store',dest='file',required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # 第一个 try-except 模块，创建socket模块
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,e:
        print "Error creating socket %s" %e
        sys.exit(1)

    #第二个 try-except 模块，连接到指定的ip和端口
    try:
        s.connect((host,port))
    except socket.gaierror,e:
        print "Address-releated error connecting to server:%s" %e
        sys.exit(1)
    except socket.error,e:
        print "Connection error: %s" %e
        sys.exit(1)

    #第三个 try-except模块  ，发送数据
    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n"%filename)
    except socket.error,e:
        print "Error sending data: %s" %e
        sys.exit(1)

    while 1:
        try:
            buf = s.recv(2048)
        except socket.error,e:
            print "Error receiving data %s"% e
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf)

if __name__=='__main__':
    main()
