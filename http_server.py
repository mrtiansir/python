#!/usr/bin/python3
# _*_ coding=utf-8 _*_


from http.server import HTTPServer, CGIHTTPRequestHandler

port = 80

try:
    httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
    print('Starting simple httpd on port: ' + str(httpd.server_port))
    httpd.serve_forever()
except KeyboardInterrupt:
    print('收到ctrl + c信号')
    print('退出程序...')


    