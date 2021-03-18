from bs4 import BeautifulSoup
import requests
from medproducts.products import *


def get_html(url):
    """
    Extracts the html layer from a webpage
    :param url: a valid webpage url
    :rtype: String
    """
    request = requests.get(url)
    if request.status_code == 200:
        return request.content
    else:
        raise Exception("Bad request")


def get_products(html):
    """
    Gets the product names and prices from a url, and stores them in Products
    :param html: html from a page in the medino.com domain
    :rtype: Products
    """
    soup = BeautifulSoup(html, 'html.parser')
    products = Products()
    for product in soup.find_all('div', class_='product-list-item'):
        products.add_product(
            product.select_one('div.product-list-link-text').text,
            product.select_one('span.product-list-price-span').text
        )
    return products
