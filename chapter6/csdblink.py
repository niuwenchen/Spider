#encoding:utf-8
#@Time : 2017/7/1 16:25
#@Author : JackNiu
import re
import urllib.request
def getLink(url):
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
    opener = urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

    data = str(urllib.request.urlopen(url).read())

    # 根据需求构建链接表达式
    pat='(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link =list(set(link))
    return link

url="http://blog.csdn.net"

linklist = getLink(url)
for i in linklist:
    print(i[0])