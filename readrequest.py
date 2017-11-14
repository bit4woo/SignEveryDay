# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'


'''
POST /safebrowsing/downloads?client=navclient-auto-ffox&appver=56.0&pver=2.2&key=AIzaSyD_Drzahe4dBzGCZ9ArvowCvrPx_yFrlCM HTTP/1.1
Host: safebrowsing.google.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Length: 11516
Content-Type: text/plain
Connection: close
Cookie: NID=102=mOvY8DdHw1y3xOn1SY43rgfENNO3M1ok1bE4AIAs2YDlXW0ttsaiWuszCkV6hn61j81jorKWzG--pWNzXxFnfta2oUvqdHmT2_zwDNKlqquePVzFooSu86FWelT807i9
Pragma: no-cache
Cache-Control: no-cache

goog-badbinurl-shavar
'''
import httplib
import os
import sys

class signeveryday():
    def __init__(self):
        self.method = ""
        self.url = ""
        self.protocol = ""
        self.headers = {}
        self.data = ""

    def strip_list(self,inputlist):
        if isinstance(inputlist,list):
            resultlist =[]
            for x in inputlist:
                x = x.strip()
                resultlist.append(x)
            return resultlist
        else:
            print "the input should be a list"

    def readrequest(self,filename):
        fp = open(filename,"r")

        content = fp.readlines()
        lines = self.strip_list(content)
        for index in xrange(len(lines)):
            line = lines[index]
            if index == 0:
                self.method = line.split()[0]
                self.url = line.split()[1]
                self.protocol = line.split()[2]

            elif len(line.split(": ")) == 2:
                key, value = line.split(": ", 1)
                self.headers[key] = value

            elif len(line) != 0 and self.method != "GET":
                self.data = line

    def dorequest(self,ishttps=False):
        if ishttps:
            conn = httplib.HTTPSConnection(self.headers["Host"])
        else:
            conn = httplib.HTTPConnection(self.headers["Host"])
        print self.headers["Host"]
        print self.method
        #del self.headers['Host'];
        #print self.headers
        conn.request(self.method,self.url,self.data,self.headers)
        result = conn.getresponse()
        #print result.msg
        print result.status
        print result.reason
        #print result.read()
    def schedule(self):
        task = ""
        interval = 24 #hours
        times = 7
        file = os.path.join(os.getcwd(),"schedule.txt")
        fp = open(file,"a")
        fp.write("{0} {1} {2}".format(task,interval,times))

if __name__ == "__main__":
    x = signeveryday()
    path = os.path.join(os.getcwd(),"requests")
    x.readrequest(path+"\\baidu")
    x.dorequest(True)