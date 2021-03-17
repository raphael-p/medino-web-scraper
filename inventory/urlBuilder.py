from enum import Enum
from scraper import *


BASE_URL = "https://www.medino.com/"
PAGE_LIMIT = 10


class UrlBuilder(Enum):
    """
    Virtual enum class meant to generate the url of product page on medino.
    :implemented by: Category, Popular, Search
    """
    def __init__(self, value):
        self.__page_limit = "up-to-page=" + str(PAGE_LIMIT)
        self.__sort_by = ""
        self.__filter_by = ""

    def __build_url(self):
        return BASE_URL + self.url_part() + self.__page_limit + self.__sort_by + self.__filter_by

    def url_part(self):
        """
        Abstract method which is implemented by subclasses of UrlBuilder
        :rtype: String
        """
        return ""

    # setters for search filters
    def sort_by(self, sort_enum):
        """
        :param sort_enum: enum containing the type of sorting to apply
        :rtype: UrlBuilder
        """
        self.__sort_by = "&sort-by=" + sort_enum.value if sort_enum else ""
        return self

    def filter_by(self, filter_enum):
        """
        :param filter_enum: enum containing the filter to apply
        :rtype: UrlBuilder
        """
        self.__filter_by = "&tag=" + filter_enum.value if filter_enum else ""
        return self

    def fetch(self):
        """
        Passes the url to the scraper, which retrieves the product information on that page
        :rtype: Products
        """
        return get_products(self.__build_url())


class Category(UrlBuilder):
    ACCESSORIES = "accessories"
    ACHES_AND_PAINS = "aches-and-pain"
    ALLERGY_AND_HAYFEVER = "allergy-and-hayfever"

    def url_part(self):
        return "category/" + self.value + "?"


class Popular(UrlBuilder):
    __POPULAR = "popular-products"

    @staticmethod
    def show_all():
        return Popular.__POPULAR

    def url_part(self):
        return self.value + "?"


class Search(UrlBuilder):
    __SEARCH = ""

    @staticmethod
    def search_by(keyword):
        enum = Search.__SEARCH
        enum._value_ = "search?q=" + keyword
        return enum

    def url_part(self):
        return self.value + "&"


class SortBy(Enum):
    POPULARITY = "popularity"
    ALPHABETICAL = "alphabetical"
    PRICE_HIGH_TO_LOW = "price-high-to-low"
    PRICE_LOW_TO_HIGH = "price-low-to-high"


class FilterBy(Enum):
    FOR_CHILDREN = "for-children"
    FOR_MEN = "for-men"
    FOR_WOMEN = "for-women"
    VEGAN = "vegan"
    VEGETARIAN = "vegetarian"


if __name__ == "__main__":
    products = Search.search_by("allergy").filter_by(FilterBy.VEGETARIAN).fetch()
    print(products.display_as_table(5))
    print(products.display_as_csv(5))
    products.save_as_csv("my.csv")

