# coding=utf-8
my_host_name = 'zmirror-ya38.fcv3.1565187646146117.cn-hangzhou.fc.devsapp.net'
my_host_scheme = 'http://'
my_host_port = None  # None表示使用默认端口, 可以设置成非标准端口, 比如 81

target_domain = 'zhyy.myweimai.com'
target_scheme = 'https://'

# 这里面大部分域名都是通过 `enable_automatic_domains_whitelist` 自动采集的, 我只是把它们复制黏贴到了这里
# 实际镜像一个新的站时, 手动只需要添加很少的几个域名就可以了.
# 自动采集会不断告诉你新域名
external_domains = [
    # 微脉 Service
    'saas.myweimai.com',
    'ichoice.myweimai.com',
    # 微脉 Html，供iframe使用
    'm.myweimai.com',
    'internet-hospital.myweimai.com',
    'cdn.myweimai.com',
    'listen.cdn.myweimai.net',
    'listen.myweimai.net',
    'tj.myweimai.com',

    # 高德地图
    'a.amap.com',
    'restapi.amap.com',
    'vdata.amap.com',
    'webapi.amap.com',

    # 阿里云
    'g.alicdn.com',
    'acjs.aliyun.com',
    'cf.aliyun.com',
    'ynuf.aliapp.org',
    'at.alicdn.com',
    'weimai-zhihuiyiyuan.oss-cn-hangzhou.aliyuncs.com',
]

verbose_level = 2
force_https_domains = 'ALL'

built_in_server_host = '0.0.0.0'
built_in_server_debug = False

enable_automatic_domains_whitelist = False
domains_whitelist_auto_add_glob_list = ('*.myweimai.com', '*.amap.com')

custom_text_rewriter_enable = True

text_like_mime_keywords = ('text', 'json', 'javascript', 'xml', 'x-mpegurl')

# ############## Misc ##############
# 不加这个似乎也没影响的样子..... 不过以防万一还是加上吧
custom_allowed_remote_headers = {
    'access-control-allow-credentials', 'access-control-allow-headers', 'access-control-allow-methods',
    'access-control-max-age', 'access-control-allow-origin', 'x-connection-hash'
}
