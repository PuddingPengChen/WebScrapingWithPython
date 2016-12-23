# -*- coding: utf-8 -*-

import argparse
import sys
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

DEFAULT_HOST='127.0.0.1'
DEFAULT_PORT='8080'

class RequestHandler(BaseHTTPRequestHandler):
    #自定义的请求处理函数

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write("Hello from server")
        return

class CustomHTTPServer(HTTPServer):

    def __init__(self,host,port):
        server_address = (host,port)
        HTTPServer.__init__(self,server_address,RequestHandler)

def run_server(port):
    try:
        server = CustomHTTPServer(DEFAULT_HOST,port)
        print "Custom HTTP server started on port: %s" % port
        server.serve_forever()
    except Exception ,err:
        print "Error :%s" %err

    except KeyboardInterrupt:
        print "Server interrupt and is shutting down..."
        server.socket.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Simple HTTP Server Example")
    parser.add_argument('--port',action='store',dest='port',type=int,default=DEFAULT_PORT)
    given_args = parser.parse_args()
    port = given_args.port
    run_server(port)
