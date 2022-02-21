import requests


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
            slug = i["handle"]
            publish_date = i["published_at"]
            updated_date = i["updated_at"]
            vendor = i["vendor"]
            product_type = i["product_type"]
            tags = i["tags"]
            full_url = self.domain_url + "/products/" + slug

            details = [title, full_url, publish_date, updated_date, vendor, product_type, tags]
            self.product_list.append(details)

    def print_products(self):
        for product in self.product_list:
            print(product)


x = ShopifyScraper("https://shop.protonmail.com/")
x.get_products()
x.print_products()
