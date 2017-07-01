#encoding:utf-8
#@Time : 2017/7/1 13:40
#@Author : JackNiu

import urllib.request
import urllib.parse

url="http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LcZgM"
postdata = urllib.parse.urlencode({
    "username":"weisuen",
    "password":"aA123456"
}).encode('utf-8')

req= urllib.request.Request(url,data=postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
data = urllib.request.urlopen(req).read()
file=  open('1.html',"wb")
file.write(data)
file.close()

url2="http://blog.chinaunix.net/"
req2=urllib.request.Request(url2)
req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
data2= urllib.request.urlopen(req2).read()
file2= open('2.html',"wb")
file2.write(data2)
file2.close()