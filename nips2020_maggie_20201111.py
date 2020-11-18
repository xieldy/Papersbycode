# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:21:34 2020
Download  NIPS2020 Proceeding
@author: maggie
"""

from bs4 import BeautifulSoup 
import re
import urllib.request
import json
import time



def DownloadPaper(paper_dic_i):
    paper_url = "https://papers.nips.cc/paper/2020/file/"+str(paper_dic_i[0])+"-Paper.pdf"
    print("downloading paper: ")
    print(paper_dic_i[1])
        #papername = paper['title'].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_")
    paper_req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    paper_req= urllib.request.Request(url=paper_url, headers = paper_req_headers)
    try:
        paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
        paper_res_data=paper_res.read()#获取res响应体中的内容
    except:
        time.sleep( 10 )
        paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
        paper_res_data=paper_res.read()#获取res响应体中的内容       
    #paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
    #paper_res_data=paper_res.read()#获取res响应体中的内容
    
    #print(paper_res_data)
#   with open('C:\\Users\\maggie\\.spyder-py3\\CVPR2020\\'+paper_id,"wb") as code:
    papername = paper_dic_i[1].replace(" ","_").replace(":","").replace("?","").replace("/","").replace("|","_").replace(":","").replace('"','').replace("$","").replace("\\","_").replace("*","").replace("<","_").replace(">","_")
    with open('C:\\Users\\maggie\\.spyder-py3\\NIPS2020\\'+papername+".pdf","wb") as code:
            code.write(paper_res_data)
            #urllib.request.urlretrieve(url, papername+".pdf")
    print("Complete.")
    
url="https://papers.nips.cc/paper/2020"

#print ("method 1:")
response1=urllib.request.urlopen(url,)
print ("获取状态码，200表示成功:")
print (response1.getcode())
    
req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
req=urllib.request.Request(url=url,headers=req_headers)#构造请求对象req
res=urllib.request.urlopen(req)#发送请求对象req
res_data=res.read().decode('utf-8')#获取res响应体中的内容
#print(res_data)

html=BeautifulSoup(res_data,'html.parser')
html_body=html.body
#print(html_body)

a=html.select('a')
#print(a)
a_str = str(a)
#print(a_str)

paper_dic=re.findall('<a.*?href="/paper/2020/hash/(.*?)-Abstract.html">(.*?)</a>',a_str,re.S)
#print(paper_dic)


for i in range(841,1898):#第840篇paper的title有问题，无法存储
    print("第"+str(i)+"篇")
    DownloadPaper(paper_dic[i])


   

    

