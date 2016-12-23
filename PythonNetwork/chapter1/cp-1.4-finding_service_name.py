# -*- coding: utf-8 -*-
#通过指定的端口和协议找到服务名


import socket

def find_servive_name():
    protocolname = 'tcp'
    for port in [80,25]:
        print "Port %s => service name %s " %(port,socket.getservbyport(port,protocolname))

    print "Port %s => service name %s" %(53,socket.getservbyport(53,'udp'))

if __name__ =='__main__':
    find_servive_name()