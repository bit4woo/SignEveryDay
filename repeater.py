# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'


import parser
import myrequest
import sys

if __name__ == "__main__":

    if len(sys.argv) >=3:
        httpservice = sys.argv[1]
        file = sys.argv[2]
        rows = open(file,"r")
        method, url, header_map, data = parser.request_parser(httpservice,rows)

        if method =="POST":
            response = myrequest.http_request_post(url,header_map,data)
            print response.content
        elif method == "GET":
            response = myrequest.http_request_get(url,header_map)
            print response.content