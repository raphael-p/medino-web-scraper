import sys
import click
from medproducts.urlBuilder import Browse, Search, FilterBy, SortBy


def main():
    # print(Popular.show_all().fetch().display_as_table(5))
    print(Search.search_by("allergy").fetch().display_as_table(10))
