import requests

from bs4 import BeautifulSoup


url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class": "column"}, limit=1)


for li in list:
    name = li.div.a.text.strip()
    link = li.div.a.get("href")
    oldPrice = (
        li.find("div", {"class": "proDetail"}).find_all("a")[0].text.strip().strip("TL")
    )
    newPrice = (
        li.find("div", {"class": "proDetail"}).find_all("a")[1].text.strip().strip("TL")
    )

    print(oldPrice, newPrice)
