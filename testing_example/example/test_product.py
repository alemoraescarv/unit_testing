from product import Product
import unittest
from collections import defaultdict


class ProductTestCase(unittest.TestCase):
    def test_transform_name(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'SHOES'
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

    def test_generate_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = "SHOES-S-BLACK" 
        actual_value = small_black_shoes.generate_sku()
        self.assertEqual(expected_value, actual_value)


if __name__=="__main__":


    #unittest.main(argv=[''], verbosity=0, exit=False)
    test = "alex"
    print(len(test.split()))

    tst_defaultd_dict = defaultdict(lambda: defaultdict(2))
 




