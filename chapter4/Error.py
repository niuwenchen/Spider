#encoding:utf-8
#@Time : 2017/7/1 12:37
#@Author : JackNiu
import urllib.request
import urllib.error

try:
    data=urllib.request.urlopen("http://weibo.com/5480534464/FacpHirNX?type=comment#_rnd1498884190677")
    print(data.code)

except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)