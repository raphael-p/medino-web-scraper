from bs4 import BeautifulSoup
from productPage import *
from products import *


def get_products(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = Products()
    for product in soup.find_all('div', class_='product-list-item'):
        products.add_product(
            product.select_one('div.product-list-link-text').text,
            product.select_one('span.product-list-price-span').text
        )
    return products


if __name__ == "__main__":
    html = ProductPage.ACCESSORIES.sort_by(SortBy.POPULARITY).filter_by(FilterBy.VEGAN).html()
    medino_products = get_products(html)
    medino_products.save_as_csv("student.csv")
    print(medino_products.display_as_table())


