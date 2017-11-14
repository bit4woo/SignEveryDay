# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import requests

requests = requests.Session()

def http_request_get(url, headers, body_content_workflow=False, allow_redirects=True, custom_cookie="",custom_referer="", proxies = None):
    try:
        if custom_cookie:
            headers['Cookie']= custom_cookie
        if custom_referer:
            headers['Referer'] = custom_referer
        result = requests.get(url,
            stream=body_content_workflow,
            headers=headers,
            proxies=proxies,
            allow_redirects=allow_redirects,
            verify=False)
        return result
    except Exception, e:
        # return empty requests object
        return requests.models.Response()

def http_request_post(url, headers, payload, body_content_workflow=False, allow_redirects=True,custom_cookie="", custom_referer="",proxies = None):
    """ payload = {'key1': 'value1', 'key2': 'value2'} """
    try:
        if custom_cookie:
            headers['Cookie']= custom_cookie
        if custom_referer:
            headers['Referer'] = custom_referer
        result = requests.post(url,
            data=payload,
            headers=headers,
            stream=body_content_workflow,
            proxies=proxies,
            allow_redirects=allow_redirects,
            verify=False)
        return result
    except Exception, e:
        # return empty requests object
        return requests.models.Response()
