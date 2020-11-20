import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url = "https://www.ptt.cc/bbs/Digitalhome/index.html"

request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
 #print (data)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)


    
