import requests
import json

api_url = "https://v6.exchangerate-api.com/v6/95644fdc171638e010be05df/latest/"

bozulan_doviz = input("Bozulan döviz türü: ")

alinan_doviz = input("Alınan döviz türü: ")

miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

result = requests.get(api_url + bozulan_doviz)

result = json.loads(result.text)


print(
    "1 {0} = {1} {2}".format(
        bozulan_doviz, result["conversion_rates"][alinan_doviz], alinan_doviz
    )
)

print(
    "{0} {1} = {2} {3}".format(
        miktar,
        bozulan_doviz,
        miktar * result["conversion_rates"][alinan_doviz],
        alinan_doviz,
    )
)
