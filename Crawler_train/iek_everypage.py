import requests
from bs4 import BeautifulSoup
import json
import os
import time

#url = "http://ieknet.iek.org.tw/ieknews/Default.aspx?currentPageIndex=2&actiontype=ieknews&indu_idno=3"
headers = {'cookie':'__auc=23b3b60a16cbe66242cd1af405e; __utmz=171043199.1566562461.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); iek.org.tw=j_signon_username=nf520t&j_signon_passwd=jvKlSgR463co6gygqmzT/0x94VGXWNF754c4Atiw9PxMblzN0zhTX6300acwaM7q+2Qdm0n42OZZx2TcWi2MXQ==&j_signon_remember=on; j_signon_username=nf520t; j_signon_compidno=; ASP.NET_SessionId=a2ybubqeulhve4rbze0b3sze; j_signon_sessionid=a2ybubqeulhve4rbze0b3sze; __asc=0cef9d6c16cecf0217e63cdc10b; __utma=171043199.1769095807.1566562461.1567264835.1567343256.5; __utmc=171043199; __utmt=1; __utmb=171043199.8.10.1567343256'}
#print(response.text)

# 找出每頁所有文章連結
start = 1
while True:
    url = "http://ieknet.iek.org.tw/ieknews/Default.aspx?currentPageIndex=" + str(start) +"&actiontype=ieknews&indu_idno=12"
    print('在第幾頁:' + '在' + str(start) + '頁')

    try:
        response = requests.get(url, headers=headers)
    except:
        print("載完囉")
        break

    start += 1
    html = BeautifulSoup(response.text)
    for t in html.find_all("div", class_="conttxt-3-1"):
        # print(t)
        # 每頁的每篇新聞連結
        turl = "http://ieknet.iek.org.tw/ieknews" + t.find("a")["href"][1:7] + "detail" + t.find("a")["href"][11:]
        #print(turl)
        # 針對每一篇新聞內容下載
        response = requests.get(turl, headers=headers)
        html = BeautifulSoup(response.text)


        newstitle = html.find('h1', id="title")
        print("新聞標題:\n", newstitle.text)
        date = html.find('span', class_="H-date")
        print("日期:\n", date.text)
        news = html.find('div', class_="conttxt-3-3")
        print("新聞內容:\n", news.text)



        saved = {'newstitle': newstitle.text,
                 'date': date.text,
                 'news': news.text}
        #各篇新聞的json檔名
        notallowed = ["/", "|", "\\", "?",
                      "\"", "*", ":", "<",
                      ">", "."]
        title_news = ""
        for c in newstitle.text:
            if not c in notallowed:
                title_news = title_news + c

        dn = "Iek_News/"
        if not os.path.exists(dn):
            os.makedirs(dn)

        f = open(dn + title_news + ".json", "w", encoding="utf-8")
        json.dump(saved, f)
        f.close()
        time.sleep(2)







