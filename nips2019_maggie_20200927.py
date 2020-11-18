# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:02:13 2020
Download  NIPS2019 Proceeding
@author: maggie
"""
from bs4 import BeautifulSoup 
import re
import urllib.request
import json
import time



def DownloadPaper(paper_dic_i):
    paper_url = "https://papers.nips.cc/paper/"+str(paper_dic_i[0])+".pdf"
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
    
url="https://papers.nips.cc/book/advances-in-neural-information-processing-systems-32-2019"

print ("method 1:")
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

paper_dic=re.findall('<a.*?href="/paper/(.*?)">(.*?)</a>',a_str,re.S)
#print(paper_dic)

"""
paper_name=json.loads(res_data)[0]["content"]["title"]
print(paper_name)
paper_id=json.loads(res_data)[0]["id"]
print(paper_id)#print(len(res_data))

paper_name=json.loads(res_data)[686]["content"]["title"]
print(paper_name)
paper_id=json.loads(res_data)[686]["id"]
print(paper_id)
"""
"""
test=[{"content":{"TLDR":"We show language understanding via reading is promising way to learn policies that generalise to new environments.","abstract":" ","authors":["Victor Zhong","Tim Rockt\u00e4schel","Edward Grefenstette"],"iclr_id":"SJgob6NKvH","keywords":["nlp","reading comprehension","reasoning","reinforcement learning"],"recs":[],"session":[],"session_links":[],"session_times":[],"title":"RTFM: Generalising to New Environment Dynamics via Reading"},"forum":"SJgob6NKvH","id":"SJgob6NKvH"},{"content":{"TLDR":"As the performance of computer systems stagnates due to the end of Moore\u2019s Law,\nthere is a need for new models that can understand and optimize the execution\nof general purpose code. While there is a growing body of work on using Graph\nNeural Network...","abstract":" ","authors":["Zhan Shi","Kevin Swersky","Daniel Tarlow","Parthasarathy Ranganathan","Milad Hashemi"],"iclr_id":"SJetQpEYvB","keywords":["graph embedding","graph networks","memory","transfer learning"],"recs":[],"session":[],"session_links":[],"session_times":[],"title":"LEARNING EXECUTION THROUGH NEURAL CODE FUSION"},"forum":"SJetQpEYvB","id":"SJetQpEYvB"},{"content":{"TLDR":"Neural text generation is a key tool in natural language applications, but it is well known there are major problems at its core. In particular, standard likelihood training and decoding leads to dull and repetitive outputs. While some post-hoc fixes...","abstract":" ","authors":["Sean Welleck","Ilia Kulikov","Stephen Roller","Emily Dinan","Kyunghyun Cho","Jason Weston"],"iclr_id":"SJeYe0NtvH","keywords":["generation","language modeling","nlp","text generation"],"recs":[],"session":[],"session_links":[],"session_times":[],"title":"Neural Text Generation With Unlikelihood Training"},"forum":"SJeYe0NtvH","id":"SJeYe0NtvH"}]
print(len(test))
"""

"""
paper_dic=json.loads(res_data)
#print(paper_dic)
"""
for i in range(239,1426):#第8296-9722 第8534篇Visual Sequence Learning  in Hierarchical Prediction Networks and Primate Visual Cortex链接失效
    print("第"+str(i+8296)+"篇")
    DownloadPaper(paper_dic[i])
   

    

