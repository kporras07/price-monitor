#!/usr/bin/env python3

import yaml
from ParserAmazon import ParserAmazon

def get_parser(url):
    if "amazon" in url:
        return ParserAmazon()

with open("./products.yml", 'r') as stream:
    try:
        parsed_yaml=yaml.safe_load(stream)
        products = parsed_yaml["products"]

        for product in products:
            parser = get_parser(product["url"])
            oldPrice = None
            if "latestPrice" in product:
                oldPrice = product["latestPrice"]
            price = parser.parse(product)
            product["latestPrice"] = price

            if oldPrice and price != oldPrice:
                print("Price changed from " + oldPrice + " to " + price)

        print(products)
    except yaml.YAMLError as exc:
        print(exc)
