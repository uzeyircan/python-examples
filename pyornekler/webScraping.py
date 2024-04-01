import requests
from bs4 import BeautifulSoup
import time


def urunKontrolEt():
    url = "https://www.amazon.com.tr/Lenovo-Ideapad-Diz%C3%BCst%C3%BC-Bilgisayar-82SB00B4TX/dp/B0BL7QDMDY/ref=sr_1_1?crid=16DE4223UHQKA&keywords=lenovo+ideapad+gaming+3&qid=1692701855&sprefix=lenovo+ideapad+gaming+3%2Caps%2C132&sr=8-1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    sayfa = requests.get(url, headers=headers)

    icerik = BeautifulSoup(sayfa.content, "html.parser")

    urunAdi = icerik.find(id="productTitle").get_text().strip()
    # print(urunAdi)

    urunfiyat = (
        icerik.find(id="corePriceDisplay_desktop_feature_div").get_text().strip()
    )
    ucretdonusturen = urunfiyat[0:6].replace(".", "")
    # print(ucretdonusturen)
    int = ucretdonusturen

    tesTarih = (
        icerik.find(id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE")
        .get_text()
        .strip()
        .replace("Ayrıntılar", "")
    )
    # print(tesTarih)

    if ucretdonusturen < "25000":
        print(f"{ucretdonusturen} TL {urunAdi} fiyatı düştü acele et !!!")
    else:
        print(f"{ucretdonusturen} TL {urunAdi} henüz düşmedi")


while True:
    urunKontrolEt()
    time.sleep(3)
