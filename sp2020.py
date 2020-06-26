import urllib.request, urllib.parse
import json


def download(paper):
    url = "https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/"+paper["id"]+"/pdf"
    print("downloading paper: "+ paper['title'])
    papername = paper['title'].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_")
    request = urllib.request.Request(url=url, headers = headers)
    f = urllib.request.urlopen(request)
    #print(f.info())
    data = f.read()
    with open(papername+".pdf","wb") as code:
        code.write(data)
    #urllib.request.urlretrieve(url, papername+".pdf")
    print("Complete.")
    

query = """query ($proceedingId: String="1dAAQaOrrva"){
    proceeding: proceeding(proceedingId: $proceedingId) {
        id
        groupId
        acronym
        issn
        isbn
        startDate
        endDate
        location
        website
        title
        volume
        year
        __typename
    }
    articlesByProceeding: articlesByProceeding(proceedingId: $proceedingId) {
        id
        isOpenAccess
        sectionTitle
        title
    }
}"""

query = urllib.parse.quote(str(query))
url = "https://www.computer.org/csdl/api/v1/graphql"
queryurl = url + "?query=" + query
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

request = urllib.request.Request(url=queryurl, headers = headers)
response = urllib.request.urlopen(request)
content = response.read()
#print(content)
paperdict = json.loads(content)["data"]["articlesByProceeding"]
for i in paperdict:
    download(i)