import requests
import json

url = "https://triangl.com/products.json?limit=250&page=1"

r = requests.get(url)
data = r.json()

for item in data['products']:
    print(item['title'])
