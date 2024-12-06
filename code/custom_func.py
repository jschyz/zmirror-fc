# coding=utf-8
import re
from flask import Response, Request
from zmirror.zmirror import *

# Weimai H5
regex_weimai_domain = re.compile(r'^https?://m\.myweimai\.com')
regex_weimai_router_base = re.compile(
    r'''(?P<var>window\.routerBase\s*=\s*)'''
    '''"(?P<path>/new/health/)"''')

def replace_router_base(mobj):
    var = mobj.group('var')
    path = mobj.group('path')
    return var + '"/extdomains/m.myweimai.com' + path + '"'

def custom_response_text_rewriter(raw_text, content_mime, remote_url):
    if content_mime == 'text/html':
        # Remove 
        raw_text = raw_text.replace('Content-Security-Policy', '')

        # window.routerBase = "/new/health/"
        # window.routerBase = "/extdomains/m.myweimai.com/new/health/"
        if regex_weimai_domain.search(remote_url):
            raw_text = regex_weimai_router_base.sub(replace_router_base, raw_text)

    # external_filenames 重写文件名
    # 源JS里，存在通过JS来判断资源请求域名，重写文件名是让此功能失效场景使用
    # 场景: g.alicdn.com/AWSC/AWSC/awsc.js
    # awsc -> awsc-extmirror
    if re.search(r'javascript', content_mime):
        raw_text = raw_text.replace('/AWSC/AWSC/awsc', '/AWSC/AWSC/awsc-extmirror')

    return raw_text
