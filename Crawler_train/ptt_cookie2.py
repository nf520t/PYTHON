from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/Beauty/M.1566792730.A.D07.html"
r = Request(url)
r.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
response = urlopen(r)
html = BeautifulSoup(response)
print(html)