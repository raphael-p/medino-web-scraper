from tabulate import tabulate
import csv


class Products:
    """
    Stores the results of the data extraction (name and price of each product)
    """

    def __init__(self):
        self.product_list = [['Name', 'Price']]

    def add_product(self, product_name, product_price):
        self.product_list.append([product_name, product_price])

    def save_as_csv(self, filename):
        with open(filename, 'w') as f:
            write = csv.writer(f)
            for row in self.product_list:
                write.writerow([entry.replace("£", "") for entry in row])

    def display_as_csv(self, max_results, start_row=1):
        output = ""
        if max_results:
            for row in self.product_list[start_row:max_results+1]:
                output += ",".join(row).replace("£", "") + "\n"
        else:
            for row in self.product_list[start_row:]:
                output += ",".join(row).replace("£", "") + "\n"
        return output

    def display_as_table(self, max_results):
        return tabulate(self.product_list[:max_results+1], headers="firstrow")
