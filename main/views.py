from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
pagezero=requests.get("https://events.linuxfoundation.org/")
evt=BeautifulSoup(pagezero.content,'html.parser')
print(evt)
gg=evt.find("div",{"class":"cell medium-12 large-6 event callout"})
link=gg.a['href']
h2_element = gg.find("h2", {"class": "event-title"})
title=h2_element.a.text.strip()
description_div = gg.find("div", {"class": "event-description"})
parr= description_div.p.text.strip()
pagesub=requests.get(link)
immg=BeautifulSoup(pagesub.content,'html.parser')
sty=immg.find("div",{"class":"site-container"}).header['style']
svg=immg.find("a",{"class":"event-home-link"}).img['src']

page=requests.get("https://www.bcg.com/industries/telecommunications/insights")
soup=BeautifulSoup(page.content,'html.parser')
bcg=soup.find_all("div",{"class":"panel"},limit=2)
page3=requests.get("https://www.huawei.com/en/news")
soup3=BeautifulSoup(page3.content,'html.parser')
huawei=soup3.find_all("div",{"class":"c-box"},limit=2)
page4=requests.get("https://telecomstechnews.com/")
soup4=BeautifulSoup(page4.content,'html.parser')
elem=soup4.find_all("div",{"class":"cell small-3 medium-12 large-12"},limit=2)
lis=[]
for ele in huawei:
    lis.append(ele.img['src'])
    lis.append(ele.a['href'])
    lis.append(ele.h4.text)
for tele in elem:
    lis.append(tele.img['src'])
    lis.append(tele.a['href'])
    lis.append(tele.a['title'])
#for dd in bcg:
#    lis.append(dd.source['srcset'])
#    lis.append(dd.a['href'])
#    lis.append(dd.h2.text)

lis.append("https://www.phoronix.net/image.php?id=2024&image=windows_dev_kit_2023")
lis.append("https://www.phoronix.com/news/Windows-Dev-Kit-2023-Linux")
lis.append("Updated DeviceTree Gets Microsoft Windows Dev Kit 2023 Booting Linux")
lis.append("https://www.phoronix.net/image.php?id=2024&image=windows_dev_kit_2023")
lis.append("https://www.phoronix.com/news/Windows-Dev-Kit-2023-Linux")
lis.append("Updated DeviceTree Gets Microsoft Windows Dev Kit 2023 Booting Linux")
lis.append("https://www.phoronix.net/image.php?id=2024&image=windows_dev_kit_2023")
lis.append("https://www.phoronix.com/news/Windows-Dev-Kit-2023-Linux")
lis.append("Updated DeviceTree Gets Microsoft Windows Dev Kit 2023 Booting Linux")
lis.append("https://www.phoronix.net/image.php?id=2024&image=windows_dev_kit_2023")
lis.append("https://www.phoronix.com/news/Windows-Dev-Kit-2023-Linux")
lis.append("Updated DeviceTree Gets Microsoft Windows Dev Kit 2023 Booting Linux")

print("##############3")
for element in lis:
    print("1 ",element)
print("############33")
print(len(lis))
one={
    "img3":lis[12][:-3],
    "link3":lis[13],
    "title3":lis[14],
    "img4":lis[15][:-3],
    "link4":lis[16],
    "title4":lis[17],
    "img1":lis[0],
    "link1":"https://www.huawei.com"+lis[1],
    "title1":lis[2],
    "img2":lis[3],
    "link2":"https://www.huawei.com/"+lis[4],
    "title2":lis[5],
    "img5":lis[6],
    "link5":lis[7],
    "title5":lis[8],
    "img6":lis[9],
    "link6":lis[10],
    "title6":lis[11],
    "title7":title,
    "parr":parr,
    "sty":sty,
    "svg":svg,
    "enl":link,
}
def index(request):
    return render(request,'main/main.html',one)
    
# Create your views here.
