from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

_PLACEHOLDER_IMG = ""
_PLACEHOLDER_LINK = "#"
_PLACEHOLDER_TEXT = ""

_phoronix_img = "https://www.phoronix.net/image.php?id=2024&image=windows_dev_kit_2023"
_phoronix_link = "https://www.phoronix.com/news/Windows-Dev-Kit-2023-Linux"
_phoronix_title = "Updated DeviceTree Gets Microsoft Windows Dev Kit 2023 Booting Linux"

def index(request):
    try:
        pagezero = requests.get("https://events.linuxfoundation.org/", timeout=10)
        evt = BeautifulSoup(pagezero.content, 'html.parser')
        gg = evt.find("div", {"class": "cell medium-12 large-6 event callout"})
        link = gg.a['href']
        title = gg.find("h2", {"class": "event-title"}).a.text.strip()
        parr = gg.find("div", {"class": "event-description"}).p.text.strip()
        pagesub = requests.get(link, timeout=10)
        immg = BeautifulSoup(pagesub.content, 'html.parser')
        sty = immg.find("div", {"class": "site-container"}).header['style']
        svg = immg.find("a", {"class": "event-home-link"}).img['src']
    except Exception:
        link = _PLACEHOLDER_LINK
        title = _PLACEHOLDER_TEXT
        parr = _PLACEHOLDER_TEXT
        sty = ""
        svg = _PLACEHOLDER_IMG

    try:
        page3 = requests.get("https://www.huawei.com/en/news", timeout=10)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        huawei = soup3.find_all("div", {"class": "c-box"}, limit=2)
        hw = [[ele.img['src'], ele.a['href'], ele.h4.text] for ele in huawei if ele.img and ele.a and ele.h4]
        while len(hw) < 2:
            hw.append([_PLACEHOLDER_IMG, _PLACEHOLDER_LINK, _PLACEHOLDER_TEXT])
    except Exception:
        hw = [[_PLACEHOLDER_IMG, _PLACEHOLDER_LINK, _PLACEHOLDER_TEXT]] * 2

    try:
        page4 = requests.get("https://telecomstechnews.com/", timeout=10)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        elem = soup4.find_all("div", {"class": "cell small-3 medium-12 large-12"}, limit=2)
        tele = [[e.img['src'], e.a['href'], e.a['title']] for e in elem if e.img and e.a]
        while len(tele) < 2:
            tele.append([_PLACEHOLDER_IMG, _PLACEHOLDER_LINK, _PLACEHOLDER_TEXT])
    except Exception:
        tele = [[_PLACEHOLDER_IMG, _PLACEHOLDER_LINK, _PLACEHOLDER_TEXT]] * 2

    context = {
        "img1": hw[0][0],
        "link1": "https://www.huawei.com" + hw[0][1],
        "title1": hw[0][2],
        "img2": hw[1][0],
        "link2": "https://www.huawei.com/" + hw[1][1],
        "title2": hw[1][2],
        "img3": _phoronix_img,
        "link3": _phoronix_link,
        "title3": _phoronix_title,
        "img4": _phoronix_img,
        "link4": _phoronix_link,
        "title4": _phoronix_title,
        "img5": tele[0][0],
        "link5": tele[0][1],
        "title5": tele[0][2],
        "img6": tele[1][0],
        "link6": tele[1][1],
        "title6": tele[1][2],
        "title7": title,
        "parr": parr,
        "sty": sty,
        "svg": svg,
        "enl": link,
    }
    return render(request, 'main/main.html', context)
