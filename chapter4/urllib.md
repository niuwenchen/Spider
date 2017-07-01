## Urllib 和URLError
Urllib是python中一个功能很强大的库，用于操作URL，并在做爬虫的时候经常用到。在Python2.X中，分为UrllibheUrllib2库，在Python3.x中合并到Urllib库中，使用方法稍有不同。


    python2:import urllib ,python3: import urliib.request,urllib.error,urllib.parse
    urllib.request.urlopen  urllib.parse.urlencode , urllib.request.quote
    http.CookieJar 
    urllib.request.Request
    
看下一些基本操作：

    ● urllib.quote(string[, safe])：对字符串进行编码。参数safe指定了不需要编码的字符;
    ● urllib.unquote(string) ：对字符串进行解码；
    ● urllib.quote_plus(string[,safe]) ：与urllib.quote类似，但这个方法用'+'来替换' '，而quote用'%20'来代替' '
    ● urllib.unquote_plus(string) ：对字符串进行解码；
    ● urllib.urlencode(query[, doseq])：将dict或者包含两个元素的元组列表转换成url参数。例如 字典{'name': 'dark-bull', 'age': 200}将被转换为"name=dark-bull&age=200"
    ● urllib.pathname2url(path)：将本地路径转换成url路径；
    ● urllib.url2pathname(path)：将url路径转换成本地路径；
    ● urllib.urlretrieve(url[, filename[, reporthook[, data]]])：
            urlretrive方法直接将远程数据下载到本地。
    
    基本的方法也就这些了
    
    
代码：

    file = req.urlopen('http://www.baidu.com')
    data = file.read()
    print(data)
    
    file.read(): 读取文件的全部内容
    file.readlines():将读取的内容赋予一个列表变量
    file.readline(): 读取一行内容
    
    file = req.urlretrieve('http://www.baidu.com',filename='baidu.html')
    req.urlcleanup() 清楚retrive的缓存
    
    data = req.urlopen('http://www.baidu.com')
    print(data.info())  当前环境有关的信息
    
    Date: Sat, 01 Jul 2017 03:05:13 GMT
    Content-Type: text/html; charset=utf-8
    Transfer-Encoding: chunked
    Connection: Close
    Vary: Accept-Encoding
    Set-Cookie: BAIDUID=F2B067753EF6BC8B77DC9AD577BE55AF:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: BIDUPSID=F2B067753EF6BC8B77DC9AD577BE55AF; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: PSTM=1498878313; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: BDSVRTM=0; path=/
    Set-Cookie: BD_HOME=0; path=/
    Set-Cookie: H_PS_PSSID=1463_21113_17001_23632_20930; path=/; domain=.baidu.com
    P3P: CP=" OTI DSP COR IVA OUR IND COM "
    Cache-Control: private


    状态码： 好像没什么用。。。。
        data.getcode()  
        
编解码

    一般来说，URL标准中只会允许一部分ASCII字符比如数字、字母和部分符号等，而如汉字是不符合URL标准的。因此需要使用URL编码方案可解决 :  & 等符号需要编码。
    
    url = req.quote('http://www.baidu.com')
    print(url)
    
    http%3A//www.baidu.com
    
浏览器的属性

Headers属性：403错误，将一个python爬虫进行一些设计让python爬虫具有浏览器的特征，如何模拟，设置一些Headers信息

获取浏览器请求头的User-Agent
Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0

1： 使用build_opener()方法修改报头

    构造headers, opener 对象
    headers = ("K","V")
    opener = req.build_opener()
    opener.addheaders =[headers]
    data = opener.open(url).read()
    
2: add_header() 添加报头
当你创建一个Request对象时，你可以传递一个头信息的字典。
使用urllib.request.Request()的add_headers() 添加头

    Request对象， Request(url)
    add_header(k,v)
    设置报头后，用urlopen（） 打开对应网址
    
**超时设置**

有时候网页长时间为响应，即该网页超时

    urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            *, cafile=None, capath=None, cadefault=False, context=None):
    url: 
    timeout: 超时设置
    
**HTTP请求协议**

如果在客户端和服务器之间进行消息传递，可以使用HTTP协议进行请求。

1）GET请求：
2）POST请求：
3）PUT请求：请求服务器存储一个资源，需要指定存储的位置
4）DELETE请求： 请求服务器删除一个资源
5）HEAD请求： 请求获取对应的HTTP报头信息
6）OPTIONS请求： 可以获得当前URL所支持的请求类型


    bytes--> string:  bytes.decode()
    
    GET： urlopen()
    注意：
    keyword1="梅花"
    key_code= urllib.request.quote(keyword1)
    url = "http://www.baidu.com/s?wd="+key_code
    这里的编码只需要将关键字进行编码即可，不能对整个构造后的url进行构造，会将http://www.baidu.com 也进行编码
    就会查询出错。
    
    POST: Request对象， 但是Requests库有很好的实现，后面分析
    
    Request对象
    def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None):
    
    data即为post的data，data 由urlencode装配完成
    

**代理服务器的设置**

http://www.xicidaili.com/   许多代理服务器

    proxy = urllib.request.ProxyHandler({'http':proxy_addr}) 设置对应的代理服务器
    request.build_opener() 创建opener对象，参数为代理信息，urllib.request.HTTPHandler 类
    urllib.request.install_opener(opener) 定义全局opener，那么下面的urlopen()将会使用这个opener对象
     也就是proxy对象，如果不设置全局，这个代理对象是不起作用的
    


**DebugLog**

打印日志

    开启日志，但是我这边没有日志
    httphd =urllib.request.HTTPHandler(debuglevel=1)
    httpshd=urllib.request.HTTPSHandler(debuglevel=1)
    opener = urllib.request.build_opener(httphd,httpshd)
    urllib.request.install_opener(opener)
    
    
    状态码
    200  OK
    301  重新定向到新的URL，永久性
    302 重新定向到新的URL，非永久性
    304 请求的资源未更新
    400 非法请求
    401 请求未经授权
    403 禁止访问
    404 没有找到对应的页面
    500 服务器内部出现故障
    501 服务器不支持实现请求所需的功能
    
    if  hasattr(e,"code")   有属性
    