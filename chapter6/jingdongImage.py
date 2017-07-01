#encoding:utf-8
#@Time : 2017/7/1 16:12
#@Author : JackNiu
import re
import urllib.request
import urllib.error

def craw(url,page):
    html1= urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1='<div id="plist".+? <div class="page clearfix">'
    result1= re.compile(pat1).findall(html1)

    result1=result1[0]
    print(result1)
    pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    print(len(imagelist))
    x=1
    for imageurl in imagelist:
        print(imageurl)
        imagename = "./img/"+str(page)+str(x)+".jpg"
        imageurl = "http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1


url="https://list.jd.com/list.html?cat=9987,653,655&page=6"
craw(url,6)