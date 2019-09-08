import requests
from bs4 import BeautifulSoup
import json

start = 0
page = 0
while True:
    url = ("https://www.google.com/search?ei=vi9nXff8Co2_wAOqj524Ag&yv=3&q=%E6%96%B0%E5%9E%A3%E7%B5%90%E8%A1%A3&tbm=isch&vet=10ahUKEwj30_6B_KbkAhWNH3AKHapHBycQuT0IOCgB.vi9nXff8Co2_wAOqj524Ag.i&ved=0ahUKEwj30_6B_KbkAhWNH3AKHapHBycQuT0IOCgB&ijn="
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
        print("沒有新垣結衣了")
        break
    for p in pictures:
        data = json.loads(p.text)
        print("類型:", data["ity"])
        print("標題:", data["pt"])
        print("圖片:", data["ou"])
        print("第幾張:", start)
        try:
            response = requests.get(data["ou"], stream=True)
            if data["ity"] == "":
                fn = "yui/" + str(start) + ".jpg"
            else:
                fn = "yui/" + str(start) + "." + data["ity"]
            f = open(fn, "wb")
            f.write(response.raw.read())
            f.close()
            start = start + 1
        except:
            print("雖然心痛, 這張放棄")