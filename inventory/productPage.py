from enum import Enum
import requests

BASE_URL = "https://www.medino.com/"


class ProductPage(Enum):
    # category pages on the website, a subset of top-level product pages
    class Category(Enum):
        ACCESSORIES = "accessories"
        ACHES_AND_PAINS = "aches-and-pain"
        ALLERGY_AND_HAYFEVER = "allergy-and-hayfever"

        def __init__(self, value):
            self.url_part = "category/" + value

    # top-level product pages
    POPULAR = "popular-products"
    ACCESSORIES = Category.ACCESSORIES.url_part
    ACHES_AND_PAINS = Category.ACHES_AND_PAINS.url_part
    ALLERGY_AND_HAYFEVER = Category.ALLERGY_AND_HAYFEVER.url_part

    def __init__(self, page_limit=3):
        self.__page_limit = "up-to-page=" + str(page_limit)
        self.__sort_by = ""
        self.__filter = ""

    def __build_url(self):
        return BASE_URL + self.value + "?" + self.__page_limit + self.__sort_by + self.__filter

    # setters for search filters
    def sort_by(self, sort_enum):
        self.__sort_by = sort_enum.url_part if sort_enum is not None else ""
        return self

    def filter_by(self, filter_enum):
        self.__filter = filter_enum.url_part if filter_enum is not None else ""
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


class SortBy(Enum):
    POPULARITY = "popularity"
    ALPHABETICAL = "alphabetical"
    PRICE_HIGH_TO_LOW = "price-high-to-low"
    PRICE_LOW_TO_HIGH = "price-low-to-high"

    def __init__(self, value):
        self.url_part = "&sort-by=" + value


class FilterBy(Enum):
    FOR_CHILDREN = "for-children"
    FOR_MEN = "for-men"
    FOR_WOMEN = "for-women"
    VEGAN = "vegan"
    VEGETARIAN = "vegetarian"

    def __init__(self, value):
        self.url_part = "&tag=" + value


if __name__ == "__main__":
    print(ProductPage.POPULAR.sort_by(SortBy.POPULARITY).filter_by(FilterBy.FOR_CHILDREN).url())

