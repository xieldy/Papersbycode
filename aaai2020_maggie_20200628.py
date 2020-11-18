# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:28:33 2020
Download  AAAI2020 Proceeding
@author: maggie
"""
"""
AAAI论文太多了 我只挑了4个涉及adversarial example的tissue下载
No.1
https://aaai.org/ojs/index.php/AAAI/issue/view/249

No.4
https://aaai.org/ojs/index.php/AAAI/issue/view/252

No.7
https://aaai.org/ojs/index.php/AAAI/issue/view/255

No.10
https://aaai.org/ojs/index.php/AAAI/issue/view/258

所有会场在这
https://aaai.org/Library/AAAI/aaai20contents.php
"""

from bs4 import BeautifulSoup 
import urllib.request
import re


def DownloadPaper(paper_dic,folder_name):
    paper_url = "https://aaai.org/ojs/index.php/AAAI/article/view/"+paper_dic[1]
    print("downloading paper: ")
    #papername = paper['title'].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_")
    req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    paper_req= urllib.request.Request(url=paper_url, headers = req_headers)
    paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
    paper_res_data=paper_res.read()#获取res响应体中的内容
    #print(res2_data)
    papername = paper_dic[0].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_").replace(":","").replace('"','').replace("$","").replace("\\","_")
 #  with open('C:\\Users\\maggie\\.spyder-py3\\AAAI2020\\No.'+folder_name+'\\'+papername+".pdf","wb") as code:
    with open('No.'+folder_name+'-'+papername+".pdf","wb") as code:
            code.write(paper_res_data)
            #urllib.request.urlretrieve(url, papername+".pdf")
    print("Complete.")


def DownloadProceeding(url_i,folder_i): 
    url="https://aaai.org/ojs/index.php/AAAI/issue/view/"+url_i
    req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    req=urllib.request.Request(url=url,headers=req_headers)#构造请求对象req
    res=urllib.request.urlopen(req)#发送请求对象req
    res_data=res.read().decode('utf-8')#获取res响应体中的内容
    html=BeautifulSoup(res_data,'html.parser')
    #html_body=html.body
    #print(html_body)
    
    #paper_html=html.select('.obj_article_summary > .title >a')#按class 名称查找
    paper_html=html.select('.obj_article_summary')#按class 名称查找
    #print(paper_html)
    paper_html_str=str(paper_html)
    paper_dic=re.findall('<div.*?>.*?<a.*?>\n\t\t\t(.*?)\n\t\t\t\t\t</a>.*?<a.*?href="https://aaai.org/ojs/index.php/AAAI/article/view/(.*?)">\n\n\t\t\n\tPDF\n\n\t</a>.*?</div>',paper_html_str,re.S)#这个网页中间搞这么多空格 难怪我PDF匹配不上
    #print(paper_dic)
    #print(len(paper_dic))
    
    """
    paper_html_str = str(paper_html)
    paper_name=re.findall('<a.*?>\n\t\t\t(.*?)\n\t\t\t\t\t</a>',paper_html_str,re.S)#这个网页中间搞这么多空格 难怪我PDF匹配不上
    print(paper_name)
    #print(len(paper_name))#tissue1主题157篇
    
    #div_str = str(div)
    #paper_dic=re.findall('<a.*?href="content_CVPR_2020/papers/(.*?)">pdf</a>',a_str,re.S)
    
    
    paper_link=html.select('.obj_galley_link')#按class 名称查找
    #print(paper_link)
    #a=html.select('a')
    paper_link_str = str(paper_link)
    #print(paper_link_str)
    #<a class="obj_galley_link pdf" href="https://aaai.org/ojs/index.php/AAAI/article/view/5393/5249">PDF</a>
    paper_id=re.findall('<a.*?href="https://aaai.org/ojs/index.php/AAAI/article/view/(.*?)">\n\n\t\t\n\tPDF\n\n\t</a>',paper_link_str,re.S)#这个网页中间搞这么多空格 难怪我PDF匹配不上
    #print(paper_id)
    #print(len(paper_id))#tissue1主题157篇
    """
    """
    print(paper_dic[0])
    print(paper_dic[0][0])
    print(paper_dic[0][1])
    """
    
    for i in range(len(paper_dic)):
        DownloadPaper(paper_dic[i],folder_i)
 
 
#urls=['249','252','255','258']
#folder=['1','4','7','10']
#tissue 4有一篇paper过大 不能用urllib下 以后再debug

urls=['249','255','258']
folder=['1','7','10']

for i in range(len(urls)):
    DownloadProceeding(urls[i],folder[i])
