#encoding:utf-8
#@Time : 2017/7/1 11:12
#@Author : JackNiu
import urllib.request as req
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
# 可以访问成功，并没有出现403 错误
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
opener = req.build_opener()
# self.addheaders = [('User-agent', client_version)]
opener.addheaders =[headers]
data = opener.open(url).read()
fhandler = open("csdn.html",'wb')
fhandler.write(data)
fhandler.close()

