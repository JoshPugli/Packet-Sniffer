import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json
import dataset

class ShopifyScraper:

    def __init__(self, root_domain):
        self.domain_url = root_domain
        self.product_list_url = self.domain_url + "/products.json"
        self.product_list = []

    def get_products(self):

        self.fetch_products = requests.get(self.product_list_url)
        products = self.fetch_products.json()["products"]

        for i in products:
            title = i["title"]
            mainid = i['id']
            product_type = i["product_type"]
            publish_date = i["published_at"]
            vendor = i['vendor']
            handle = i['handle']
            for v in i['variants']:
                item = {'id': mainid,
                        'title': title,
                        'publish_date': publish_date,
                        'product_type': product_type,
                        'vendor': vendor,
                        'varid': v['id'],
                        'vartitle': v['title'],
                        'price': v['price'],
                        'available': v['available'],
                        'created_at': v['created_at'],
                        'updated_at': v['updated_at'],
                        'requires_shipping': v['requires_shipping'],
                        'compare_at_price': v['compare_at_price'],
                        'full_url': self.domain_url + "/products/" + handle
                        }
                self.product_list.append(item)
                # tags = i["tags"]

    def print_products(self):
        for product in self.product_list:
            print(product)


url = "https://trends.builtwith.com/websitelist/Shopify"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

for script in soup(["script", "style"]):
    script.decompose()

store_lst = []
strips = list(soup.stripped_strings)
for text in strips:
    try:
        if text[-4:] == '.com' or text[-4:] == '.org':
            store_lst.append(text)
    except IndexError:
        pass
print(store_lst)

x = ShopifyScraper("https://partakefoods.com/collections/all")

x.get_products()
x.print_products()
