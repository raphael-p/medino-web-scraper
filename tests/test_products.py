import unittest
from medproducts.products import *


class TestBasicFunction(unittest.TestCase):

    def setUp(self):
        self.prod = Products()
        self.prod.add_product('Prod 1', '£1.29')
        self.prod.add_product('Prod 2', '£2.59')
        self.prod.add_product('Prod 3', '£1.58')
        self.prod.add_product('Prod 4', '£7.29')
        self.prod.add_product('Prod 5', '£8.13')
        self.prod.add_product('Prod 6', '£0.50')

    def test_display_csv_first_two(self):
        output = self.prod.display_as_csv(2)
        self.assertTrue(output == "Prod 1,1.29\nProd 2,2.59\n")

    def test_display_csv_more_lines_than_results(self):
        output = self.prod.display_as_csv(8)
        self.assertTrue(output == "Prod 1,1.29\nProd 2,2.59\nProd 3,1.58\nProd 4,7.29\nProd 5,8.13\nProd 6,0.50\n")


if __name__ == '__main__':
    unittest.main()