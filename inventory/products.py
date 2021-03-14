from tabulate import tabulate
import csv


class Products:
    def __init__(self):
        self.product_list = [['Name', 'Price']]

    def add_product(self, product_name, product_price):
        self.product_list.append([product_name, product_price])

    def save_as_csv(self, filename):
        with open(filename, 'w') as f:
            write = csv.writer(f)
            for row in self.product_list:
                write.writerow(row)

    def display_as_table(self):
        return tabulate(self.product_list[1:], headers=self.product_list[0])
