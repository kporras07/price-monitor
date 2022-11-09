#!/usr/bin/env python3

import yaml
from ParserAmazon import ParserAmazon
from ParserPrimaCoffee import ParserPrimaCoffee
from os import path

def get_parser(url):
    if "amazon" in url:
        return ParserAmazon()
    if "prima-coffee.com" in url:
        return ParserPrimaCoffee()

latestProducts = []
products = []

if path.exists("latestProducts.yml"):
    with open("./latestProducts.yml", 'r') as latestProductsStream:
        latestProducts = yaml.safe_load(latestProductsStream)

with open("./products.yml", 'r') as stream:
    try:
        parsed_yaml=yaml.safe_load(stream)
        products = parsed_yaml["products"]

        for product_id in products:
            product = products[product_id]
            if product_id in latestProducts:
                latestProduct = latestProducts[product_id]
                if latestProduct["latestPrice"]:
                    product["latestPrice"] = latestProduct["latestPrice"]

        for product_id in products:
            product = products[product_id]
            parser = get_parser(product["url"])
            oldPrice = None
            if "latestPrice" in product:
                oldPrice = product["latestPrice"]
            price = parser.parse(product)

            if oldPrice and price != oldPrice:
                print("Price changed from " + oldPrice + " to " + price)

            product["latestPrice"] = price
    except yaml.YAMLError as exc:
        print(exc)

with open("./latestProducts.yml", 'w') as file:
    try:
        yaml.dump(products, file)
    except yaml.YAMLError as exc:
        print(exc)
