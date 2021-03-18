import unittest
from medproducts.scraper import *


class TestUrlBuilder(unittest.TestCase):

    def setUp(self):
        self.front_page_html = get_html("https://www.medino.com/")

    def test_malformed_url(self):
        url = "https://ww.medino.com/sarch?q=allergy&up-to-page=10&tag=vegetarian"
        self.assertRaises(Exception, get_html, url)

    def test_get_medino_html(self):
        self.assertTrue(bool(BeautifulSoup(self.front_page_html, 'html.parser').find()))

    def test_extract_products(self):
        products = get_products(self.front_page_html)
        has_products = len(products.product_list) > 1
        self.assertTrue(has_products)


if __name__ == '__main__':
    unittest.main()
