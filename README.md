# medproducts

## Description

`medproducts` is a command-line interface and library which retrieves products from www.medino.com.
It builds a query, which is converted to a url in the medino domain (for example, https://www.medino.com/search?q=allergy), 
and then gets the names and prices of all the products in the webpage (up to a limit of 10 pages).

## Installation Instructions

In a python 3 environment with pip installed (we recommend using a virtual environment), navigate to the project's
root directory and run the following:

```bash
pip install .
```


## Usage Instructions

### Command Line Interface

To get information on available parameters, use

```bash
medproducts --help
```

As an example, the following query displays 5 accessories 
with the tag 'for women' in alphabetical order in a table.

```bash
medproducts -p -n 5 -s alphabetical -t for_women browse accessories
```

### Library

To use this within a python script, add the following import statement:

```python
from medproducts.urlBuilder import Browse, Search
```

Next, you can construct a one-line query, such as:

```python
    Browse.ALLERGY_AND_HAYFEVER\
        .sort_by(SortBy.PRICE_LOW_TO_HIGH).filter_by(FilterBy.FOR_MEN)\
        .display_as_table(10)
```

In order to make your own query, first, choose whether \
to browse a page or search the website:
* Browse: choose a category from the medino website
    * example: `Browse.POPULAR`
    * options: POPULAR, ACCESSORIES, ACHES_AND_PAINS, ALLERGY_AND_HAYFEVER
* Search: use the `query()` method to perform a keyword search
    * example: `Search.query('allergy')`
    
Then, add sorting or filtering to your query:
* Sort: use the `sort_by()` method, and pass a sorting parameter as an argument
    * example: `.sort_by(SortBy.POPULARITY)`
    * options: POPULARITY, ALPHABETICAL, PRICE_HIGH_TO_LOW, PRICE_LOW_TO_HIGH
* Filter: use the `filter_by()` method, and pass a filtering parameter as an argument
    * example `.filter_by(FilterBy.FOR_CHILDREN)`
    * options: FOR_CHILDREN, FOR_MEN, FOR_WOMEN, VEGAN, VEGETARIAN
    
Finally, choose how to format the results:
* Save to file: invoke the `save_as_csv()` method
* CSV: invoke the `display_as_csv()` method
* Table: invoke the `display_as_table()` method
* Python dictionary: use the `product_list` variable

## Running Tests

In the root directory of this project run the command
```bash
python -m unittest discover -v
```
    

 