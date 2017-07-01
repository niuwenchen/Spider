#encoding:utf-8
#@Time : 2017/7/1 10:57
#@Author : JackNiu

import urllib.request as req

url = req.quote('http://www.baidu.com')
print(url)
print(req.unquote(url))