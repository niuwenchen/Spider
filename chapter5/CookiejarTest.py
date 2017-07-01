#encoding:utf-8
#@Time : 2017/7/1 14:02
#@Author : JackNiu
import urllib.request
import urllib.parse
import http.cookiejar

url="http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LcZgM"
postdata = urllib.parse.urlencode({
    "username":"weisuen",
    "password":"aA123456"
}).encode('utf-8')

req=urllib.request.Request(url,data=postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
cjar= http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)

data = opener.open(req).read()
file=open('3.html','wb')
file.write(data)
file.close()

url2="http://blog.chinaunix.net/"
data2= urllib.request.urlopen(url2).read()
fhandle = open('4.html','wb')
fhandle.write(data2)
fhandle.close()