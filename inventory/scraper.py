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
    html = Popular.show_all().sort_by(SortBy.PRICE_HIGH_TO_LOW).filter_by(FilterBy.VEGAN).html()
    medino_products = get_products(html)
    print(medino_products.display_as_csv(5))


