import requests

url = "https://e-dictionary.ilrdf.org.tw/wsReDictionary.htm"

ask = {
    "FMT": 2,
    "account": "E202403005",
    "TribesCode": 42,
    "qw": "dang"
}

response = requests.post(url, data=ask)

print(response.status_code)
print(response.text)