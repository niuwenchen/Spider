#encoding:utf-8
#@Time : 2017/7/1 16:31
#@Author : JackNiu
import urllib.request
import re

def getContent(url,page):
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    data = urllib.request.urlopen(url).read().decode('utf-8')
    # 提取用户
    userpart= 'target="_blank" title="(.*?)">'
    # 提取段子
    contentpart = '<div class="content">(.*>)</div>'
    # 寻找所有用户
    userlist = re.compile(userpart,re.S).findall(data)
    contentlist = re.compile(contentpart,re.S).findall(data)
    x=1
    for content in contentlist:
        content =content.replace("\n","")
        name="content"+str(x)
        exec(name+'=content')
        x+=1
    y=1
    for user in userlist:
        name ="content"+str(y)
        print('用户'+str(page)+str(y)+"是："+user)
        print("内容是：")
        exec("print("+name+")")
        y+=1

url = "http://www.qiushibaike.com/8hr/page/1"
getContent(url,1)