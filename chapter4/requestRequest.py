#encoding:utf-8
#@Time : 2017/7/1 11:35
#@Author : JackNiu
import urllib.request as req
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
request = req.Request(url)

request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")

data = req.urlopen(request)
print(data)