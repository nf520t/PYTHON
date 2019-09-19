import requests
from bs4 import BeautifulSoup
import json
import os

start = 0
page = 0




while True:
    url = ("https://www.google.com/search?ei=qe2BXdCCHI6HoASMg7-4BQ&rlz=1C1SQJL_zh-TWTW836TW836&yv=3&q=Selfie&tbm=isch&vet=10ahUKEwiQ-7vl_NnkAhWOA4gKHYzBD1cQuT0IPygB.qe2BXdCCHI6HoASMg7-4BQ.i&ved=0ahUKEwiQ-7vl_NnkAhWOA4gKHYzBD1cQuT0IPygB&ijn="
           + str(page) + "&start="
           + str(page * 100) +"&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc")
    page = page + 1
    headers = {
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    pictures = html.find_all("div", class_="rg_meta")
    if len(pictures) == 0:
        print("沒有照片了")
        break
    for p in pictures:
        data = json.loads(p.text)
        print("類型:", data["ity"])
        print("標題:", data["pt"])
        print("圖片:", data["ou"])
        print("第幾張:", start)
        try:
            dn = "pic/"
            if not os.path.exists(dn):
                os.makedirs(dn)

            response = requests.get(data["ou"], stream=True)
            if data["ity"] == "":
                fn = dn + str(start) + ".jpg"
            else:
                fn = dn + str(start) + "." + data["ity"]
            f = open(fn, "wb")
            f.write(response.raw.read())
            f.close()
            start = start + 1
        except:
            print("這張放棄")