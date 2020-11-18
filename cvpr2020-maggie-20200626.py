# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:22:43 2020
Download CVPR2020 Proceeding
@author: maggie
"""
#用#写注释

"""
用来写多行注释
1行
2行
3行
"""

'''
也可以用来写多行注释
1行
'''

"""
import cookielib
import urllib2
python3对urllib2进行了重构，拆分成了urllib.request,urllib.response, urllib.parse, urllib.error
"""
from bs4 import BeautifulSoup 
import urllib.request
import re

#import http.cookiejar

def DownloadPaper(paper_id):
    paper_url = "http://openaccess.thecvf.com/content_CVPR_2020/papers/"+paper_id
    print("downloading paper: ")
    #papername = paper['title'].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_")
    paper_req= urllib.request.Request(url=paper_url, headers = req_headers)
    paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
    paper_res_data=paper_res.read()#获取res响应体中的内容
    #print(res2_data)
#   with open('C:\\Users\\maggie\\.spyder-py3\\CVPR2020\\'+paper_id,"wb") as code:
    with open(paper_id,"wb") as code:

            code.write(paper_res_data)
            #urllib.request.urlretrieve(url, papername+".pdf")
    print("Complete.")

#定义带爬取网页url地址
url="http://openaccess.thecvf.com/CVPR2020.py"

"""
print ("method 1:")
response1=urllib.request.urlopen(url,)
print ("获取状态码，200表示成功:")
print (response1.getcode())
print ("获取网页内容的长度:")
print (len(response1.read()))

print("method 2：")
request=urllib.request.Request(url)
request.add_header("user-agent","Mozilla/5.0")#将爬虫伪装成浏览器Mozilla/5.0
response2=urllib.request.urlopen(request)#why这里是是urlopen(request)
print ("获取状态码，200表示成功:")
print (response2.getcode())
print ("获取网页内容的长度:")
print (len(response2.read()))

print("method 3：")
cookie=http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))#加入urllib2处理cookie的能力
urllib.request.install_opener(opener)
response3=urllib.request.urlopen(url)
print ("获取状态码，200表示成功:")
print (response3.getcode())
print ("获取网页内容的长度:")
print (len(response3.read()))
"""

"""
(1) urllib.request.urlopen()方法可以实现最基本请求的发起，但这几个简单的参数并不足以构建一个完整的请求
(2) 我们可以使用 urllib.request.Request() 先构造一个请求对象，这个请求对象可以包含请求头信息，或者包含要向服务器传递的数据，然后再发送请求
(3) 语法：urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False,method=None)
(4) 其中 url 是要请求的URL，这是必传参数，其他都是可选参数；data 是要向服务器传递的数据，headers 用来构造请求头信息，method 用来指定请求方法
"""

#定义请求头信息，通常只定义 User-Agent
req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

#发送给服务器的表单
"""req_data={
    "name":"Germey"
}"""

#req_data=bytes(urllib.parse.urlencode(req_data).encode(),encoding='utf8')#把要传递的数据转换成字节流编码格式

req=urllib.request.Request(url=url,headers=req_headers)#构造请求对象req
res=urllib.request.urlopen(req)#发送请求对象req
res_data=res.read().decode('utf-8')#获取res响应体中的内容
#print(res_data)

#用BeautifulSoup解析数据 python3 必须传入参数二'html.parser' 得到一个对象，接下来获取对象的相关属性
html=BeautifulSoup(res_data,'html.parser')
# 读取title内容
#print(html.title)
# 读取title属性
#attrs=html.title.attrs
#print(attrs)
# 读取body
#html_body=html.body
#print(html_body)

#download

"""how to extract paper_dic from html_body"""

"""
#文章标题
<dt class="ptitle"><br><a href="content_CVPR_2020/html/Wu_Unsupervised_Learning_of_Probably_Symmetric_Deformable_3D_Objects_From_Images_CVPR_2020_paper.html">Unsupervised Learning of Probably Symmetric Deformable 3D Objects From Images in the Wild</a></dt>
<dd>
#作者1
<form id="form-ShangzheWuUnsupervisedLearningof" action="./CVPR2020_search.py" method="post" class="authsearch">
<input type="hidden" name="query" value="Shangzhe Wu">
<a href="#" onclick="document.getElementById('form-ShangzheWuUnsupervisedLearningof').submit();">Shangzhe Wu</a>,
</form>
#作者2
<form id="form-ChristianRupprechtUnsupervisedLearningof" action="./CVPR2020_search.py" method="post" class="authsearch">
<input type="hidden" name="query" value=" Christian Rupprecht">
<a href="#" onclick="document.getElementById('form-ChristianRupprechtUnsupervisedLearningof').submit();"> Christian Rupprecht</a>,
</form>
#作者3
<form id="form-AndreaVedaldiUnsupervisedLearningof" action="./CVPR2020_search.py" method="post" class="authsearch">
<input type="hidden" name="query" value=" Andrea Vedaldi">
<a href="#" onclick="document.getElementById('form-AndreaVedaldiUnsupervisedLearningof').submit();"> Andrea Vedaldi</a>
</form>
</dd>
<dd>
#正文链接
[<a href="content_CVPR_2020/papers/Wu_Unsupervised_Learning_of_Probably_Symmetric_Deformable_3D_Objects_From_Images_CVPR_2020_paper.pdf">pdf</a>]
#支撑材料
[<a href="content_CVPR_2020/supplemental/Wu_Unsupervised_Learning_of_CVPR_2020_supplemental.pdf">supp</a>]
#引用
<div class="link2">[<a class="fakelink" onclick="$(this).siblings('.bibref').slideToggle()">bibtex</a>]
<div class="bibref">
@InProceedings{Wu_2020_CVPR,<br>
author = {Wu, Shangzhe and Rupprecht, Christian and Vedaldi, Andrea},<br>
title = {Unsupervised Learning of Probably Symmetric Deformable 3D Objects From Images in the Wild},<br>
booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},<br>
month = {June},<br>
year = {2020}<br>
}
</div>
</div>
</dd>
"""

#a=html.select('a[href="content_CVPR_2020/papers/Wu_Unsupervised_Learning_of_Probably_Symmetric_Deformable_3D_Objects_From_Images_CVPR_2020_paper.pdf"]')
#print(a)
a=html.select('a')
#print(a)
#print('a type:',type(a))
#for i in a:
#    print(type(i))
    
#正则查找
#pattern=re.compile(r'<a href="(.*?)">(.*?)</a>',re.S)
#string=
"""
.*?是跳过的意思,
(.*?) 加括号的意思是,匹配括号里的数据,也就是取出数据
"""
a_str = str(a)
paper_dic=re.findall('<a.*?href="content_CVPR_2020/papers/(.*?)">pdf</a>',a_str,re.S)
#[<a href="content_CVPR_2020/papers/Wu_Unsupervised_Learning_of_Probably_Symmetric_Deformable_3D_Objects_From_Images_CVPR_2020_paper.pdf">pdf</a>]
#print(paper_dic)



#for i in a:
#	print(i['href'])
#paper_dic=XXX

for paper_id in paper_dic:
    DownloadPaper(paper_id) #paper_id='Wu_Unsupervised_Learning_of_Probably_Symmetric_Deformable_3D_Objects_From_Images_CVPR_2020_paper.pdf'






























