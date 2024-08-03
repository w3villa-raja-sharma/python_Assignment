import requests
from bs4 import BeautifulSoup
url = "https://www.croma.com/searchB?q=ac%3Arelevance&text=ac"
proxies = {
    "http" : "http://167.179.45.56"
}
response = requests.get(url, proxies=proxies)
croma = BeautifulSoup(response.text , "html.parser")
# print(soup.find_all(class_="KzDlHZ"))
for data in croma.find_all(class_="product-title plp-prod-title 999") :
    print(data.text)
for data in croma.find_all(class_="amount plp-srp-new-amount") :
    print(data.text)

