# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'
import urlparse

def request_parser(httpservice,rows_list): #rows is a list

    url_part = urlparse.urlparse(httpservice)
    httpservice = url_part.scheme+"://"+url_part.netloc

    tmp_list =[]
    for x in rows_list:
        x = x.strip()
        tmp_list.append(x)
    rows = tmp_list
    print
    method = None
    url = None
    data = {}
    index =0
    header_map = {}
    for row in rows:
        if rows.index(row) ==0:# row = rows[0]
            method = row.split(" ")[0]
            url = row.split(" ")[1] #not full url address
            url = httpservice+url
        elif (row == "") and index == 0:# the line the split headers and data
            index = rows.index(row) #the first empty line is the line to split the headers and data
        elif method=="POST" and rows.index(row) == index+1 and index!= 0: #data
            try:
                for item in row.split("&"):
                    key = item.split("=")[0]
                    value = item.split("=")[1]
                    data[key] = value
            except:
                print ("Error encountered when parser data")

        elif ": " in row:
            key = row.split(": ")[0]
            value = row.split(": ")[1]
            header_map[key] = value
    return method,url,header_map,data

if __name__ == "__main__":
    x = '''POST /front/vote/saveVoteLog HTTP/1.1
Host: www.jxsoa.com
Content-Length: 424
Accept: */*
Origin: http://www.jxsoa.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 7.1.1; MX6 Build/NMF26O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043621 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/en
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://www.jxsoa.com/front/article/30520.html?from=singlemessage&isappinstalled=0
Accept-Language: en,en-US;q=0.8
Cookie: JSESSIONID=69A870008BE6ABF88990E59780180A77; openId=oWK1XwEge86uYpX2i2f632-Oj7bY
Connection: close

voteLog.vote_id=477&voteLog.open_id=oWK1XwEge86uYpX2i2f632-Oj7bY&voteLog.head_url=http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTKBrpXtgvny3cNBqSp6mDKJeXp7qwMsmnZyUVxquicDjkynRZONobFCHlQRwLfHN0q9BGqsZ9PAwIg%2F0&voteLog.nick_name=%E6%AF%94%E7%89%B9&voteLog.options=1&voteLog.vote_count=1&voteLog.k_id=30438&voteLog.c_id=30520&checkCodeMd5=6DAAAFCD2D4D3384803939F15F89CD8D&checkCode=b52d2455-e74c-4b0b-b7b7-2440f88df553'''
    x = x.split("\n")
    print  request_parser("https://www.baidu.com:8888/s/sd",x)