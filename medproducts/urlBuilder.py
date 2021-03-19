from enum import Enum
from medproducts.scraper import *


DOMAIN = "https://www.medino.com/"
PAGE_LIMIT = 10


class UrlBuilder(Enum):
    """
    Virtual enum class meant to generate the url of product page on medino.
    :implemented by: Browse, Search
    """

    def __init__(self, value):
        self.__page_limit = str(PAGE_LIMIT)
        self.__sort_by = ""
        self.__filter_by = ""
        self._keyword = ""

    def __build_url(self):
        return compose_url(DOMAIN, self.value,
                           q=self._keyword, up_to_page=self.__page_limit,
                           sort_by=self.__sort_by, tag=self.__filter_by)

    # setters for search filters
    def sort_by(self, sort_enum):
        """
        :param sort_enum: enum containing the type of sorting to apply
        :rtype: UrlBuilder
        """
        self.__sort_by = sort_enum.value if sort_enum else ""
        return self

    def filter_by(self, filter_enum):
        """
        :param filter_enum: enum containing the filter to apply
        :rtype: UrlBuilder
        """
        self.__filter_by = filter_enum.value if filter_enum else ""
        return self

    def url(self):
        """
        Getter method for url, for use in unit testing
        :return: url
        :rtype: String
        """
        return self.__build_url()

    def fetch(self):
        """
        Passes the url to the scraper, which retrieves the product information on that page
        :rtype: Products
        """
        return get_products(get_html(self.__build_url()))


class Browse(UrlBuilder):
    POPULAR = "popular-products"
    ACCESSORIES = "category/accessories"
    ACHES_AND_PAINS = "category/aches-and-pain"
    ALLERGY_AND_HAYFEVER = "category/allergy-and-hayfever"


class Search(UrlBuilder):
    __SEARCH = "search"

    @staticmethod
    def query(keyword):
        enum = Search.__SEARCH
        enum._keyword = keyword
        return enum


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


def compose_url(domain, path, **params):
    url = domain + path
    is_first = True
    for key, value in params.items():
        if not value:
            continue
        separator = "?" if is_first else "&"
        is_first = False
        url += separator + key.replace("_", "-") + "=" + value
    return url


if __name__ == "__main__":
    print(FilterBy[None])
    "a".upper()

