#encoding:utf-8
#@Time : 2017/7/1 11:45
#@Author : JackNiu
import urllib.request
import urllib.parse


def get():
    keyword = "hello"
    keyword1 = "梅花"
    key_code = urllib.request.quote(keyword1)
    url = "http://www.baidu.com/s?wd=" + key_code
    data = urllib.request.urlopen(url).read()
    fhadnler = open('梅花.html', 'wb')
    fhadnler.write(data)
    fhadnler.close()


def post():
    # 这个网址应该是失效了，可以自己做一个用于测试
    url='http://www.iqianyue.com/mypost'
    postdata = urllib.parse.urlencode({
        "name":"JackNiu",
        "pass":"1234"
    }).encode('utf-8')
    req= urllib.request.Request(url,postdata)
    data = urllib.request.urlopen(req).read()
    fhandle =open("表单.html",'wb')
    fhandle.write(data)
    fhandle.close()

def use_proxy(proxy_addr,url):
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    # 下面调用 urlopen将会使用上面的opener
    data = urllib.request.urlopen(url).read()
    print(data)

def debuglog():
    httphd =urllib.request.HTTPHandler(debuglevel=1)
    httpshd=urllib.request.HTTPSHandler(debuglevel=1)
    opener = urllib.request.build_opener(httphd,httpshd)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen('http://edu.51cto.com')
    print(data.code)

# proxy_addr="219.150.242.54:9999"
# use_proxy(proxy_addr,"http://www.baidu.com")
debuglog()