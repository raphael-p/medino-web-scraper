from enum import Enum
import requests

BASE_URL = "https://www.medino.com/"
PAGE_LIMIT = 3


class ProductPage(Enum):
    def __init__(self, value):
        self.__page_limit = "up-to-page=" + str(PAGE_LIMIT)
        self.__sort_by = ""
        self.__filter_by = ""

    def __build_url(self):
        return BASE_URL + self.url_part() + self.__page_limit + self.__sort_by + self.__filter_by

    def url_part(self):
        return

    # setters for search filters
    def sort_by(self, sort_enum):
        self.__sort_by = "&sort-by=" + sort_enum.value if sort_enum else ""
        return self

    def filter_by(self, filter_enum):
        self.__filter_by = "&tag=" + filter_enum.value if filter_enum else ""
        return self

    # getters
    def url(self):
        return self.__build_url()

    def html(self):
        request = requests.get(self.__build_url())
        if request.status_code == 200:
            return request.content
        else:
            raise Exception("Bad request")


class Category(ProductPage):
    ACCESSORIES = "accessories"
    ACHES_AND_PAINS = "aches-and-pain"
    ALLERGY_AND_HAYFEVER = "allergy-and-hayfever"

    def url_part(self):
        return "category/" + self.value + "?"


class Popular(ProductPage):
    POPULAR = "popular-products"

    def url_part(self):
        return self.value + "?"


class Search(ProductPage):
    SEARCH = ""

    @staticmethod
    def search_by(keyword):
        enum = Search.SEARCH
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
    # print(Test.VALUES.value)
    # print(ProductPage.search_by("hi").value)
    # a = Search.SEARCH("hi")
    # print(aż)
    # print(ProductPage.POPULAR.sort_by(SortBy.PRICE_LOW_TO_HIGH).filter_by(FilterBy.FOR_CHILDREN).url())
    # print(Category.ACCESSORIES.sort_by(SortBy.PRICE_LOW_TO_HIGH).filter_by(FilterBy.FOR_CHILDREN).url())
    print(Popular.POPULAR.sort_by(SortBy.PRICE_HIGH_TO_LOW).filter_by(FilterBy.VEGAN).url())
    print(Search.search_by("a").url())

