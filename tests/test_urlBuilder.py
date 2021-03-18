import unittest
from medproducts.urlBuilder import *


class TestUrlBuilder(unittest.TestCase):

    def test_search_with_filter(self):
        url = Search.query("allergy").filter_by(FilterBy.VEGETARIAN).url()
        self.assertTrue(url == "https://www.medino.com/search?q=allergy&up-to-page=10&tag=vegetarian")

    def test_search_with_multiple_filter_and_sort(self):
        url = Search.query("allergy") \
            .sort_by(SortBy.PRICE_HIGH_TO_LOW).sort_by(SortBy.PRICE_LOW_TO_HIGH) \
            .filter_by(FilterBy.FOR_CHILDREN).filter_by(FilterBy.VEGETARIAN).url()
        self.assertTrue(url == "https://www.medino.com/search?q=allergy&up-to-page=10&sort-by=price-low-to-high&tag=vegetarian")

    def test_category_two_categories(self):
        url = Browse.ACHES_AND_PAINS.ACCESSORIES.url()
        self.assertTrue(url == "https://www.medino.com/category/accessories?up-to-page=10")

    def test_category_with_multiple_filter_and_sort(self):
        url = Browse.ALLERGY_AND_HAYFEVER\
            .sort_by(SortBy.PRICE_LOW_TO_HIGH).filter_by(FilterBy.FOR_MEN)\
            .sort_by(SortBy.ALPHABETICAL).filter_by(FilterBy.VEGAN).url()
        self.assertTrue(url == "https://www.medino.com/category/allergy-and-hayfever?up-to-page=10&sort-by=alphabetical&tag=vegan")

    def test_popularity_with_sort(self):
        url = Browse.POPULAR.sort_by(SortBy.POPULARITY).filter_by(None).url()
        self.assertTrue(url == "https://www.medino.com/popular-products?up-to-page=10&sort-by=popularity")


if __name__ == '__main__':
    unittest.main()
