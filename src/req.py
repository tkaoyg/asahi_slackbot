import requests
from bs4 import BeautifulSoup as bs

try:
    url = "https://www.yahoo.co.jp/"
    resp = requests.get(url)
    soup = bs(resp.text, "html.parser")
    tags = soup.find_all("a")
    for tag in tags:
        print(tag.get_text())
except:
    print("取得できませんでした")