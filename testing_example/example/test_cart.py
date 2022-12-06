import unittest
from cart import ShoppingCart
from product import Product

from hypothesis import given
import hypothesis.strategies as st

import string


"""

Q1. The Stock Keeping Unit has to be updated, so if you add products or colours with whitespaces, the SKU removes them:

'tank top', 'm', 'navy blue' should look 'TANKTOP-M-NAVYBLUE'
Q2. The Stock Keeping Unit has to be updated, so if you add products with dashes, the SKU removes them:

'tshirt', 'm', 'navy blue' should look 'TSHIRT-M-NAVYBLUE'
Q3. Run the test_product you created during the lesson. Modify it so you don't get any failed test

Q4. Add the following tests to the test suite:

  1. test_cart_initially_empty(): tests that, after creating the cart instance, it starts as an empty dictionary

  2. test_add_prodcut(): tests that, after adding a product to the cart, cart.products will be equal to a dictionary like this: {'SHOES-S-BLUE': {'quantity': 1}}

  3. test_add_two_of_a_product: tests that, after adding a product passing the argument quantity equals 2, cart.product has a dictionary whose quantity is 2

  4. test_add_two_different_products

Q5. Add the following test to the test suite:

def test_remove_too_many(self):
    cart = ShoppingCart()
    product = Product('shoes', 'S', 'blue')

    cart.add_product(product)
    cart.remove_product(product, quantity=2)

    self.assertDictEqual({}, cart.products)
Does it run fine? How can you fix it?

"""


class ShoppingCartTestCase(unittest.TestCase):  # <1>

    def test_add_and_remove_product(self):
        cart = ShoppingCart()  # <2>
        product = Product('shoes', 'S', 'blue')  # <3>

        cart.add_product(product)  # <4>
        cart.remove_product(product)  # <5>

        self.assertDictEqual({}, cart.products)  # <6>

    def test_generate_sku(self):
        
        product = Product('tank top', 'M', 'navy blue')  # <3>
        self.assertEqual("TANKTOP-M-NAVYBLUE", product.generate_sku())  # <6>

    def test_cart_initially_empty(self):
        cart = ShoppingCart()
        self.assertDictEqual({},cart.products)
    
    def tes_one_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')  # <3>
        cart.add_product(product)
        self.assertDictEqual({"SHOES-S-BLUE" : {"quantity: 1"}}, cart.products)

    def test_add_2_same_products(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue') 

        cart.add_product(product,quantity=2)

        self.assertDictEqual({"SHOES-S-BLUE":{"quantity": 2}}, cart.products)

    def test_add_two_different_products(self):
        cart = ShoppingCart()
        product_one = Product('shoes', 'S', 'blue')
        product_two = Product('shirt', 'M', 'gray')

        cart.add_product(product_one)
        cart.add_product(product_two)

        self.assertDictEqual(
            {
                'SHOES-S-BLUE': {'quantity': 1},
                'SHIRT-M-GRAY': {'quantity': 1}
            },
            cart.products
        )

    def test_remove_too_many(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product, quantity=2)

        self.assertDictEqual({}, cart.products)

#    @given(st.integer())
#    def test_add_rando_products(self,x):
##        print(x)
#        cart = ShoppingCart()
#        product = Product("shoes", 'S', 'blue')
#        cart.add_product(product, quantity=y)
#        self.assertDictEqual({"SHOES":{'quantity': 0}}, cart.products)



unittest.main(argv=[''], verbosity=3, exit=False)

# Full test suite for product and shopping cart
class ProductTestCase(unittest.TestCase):
    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(
            'SHOES',
            small_black_shoes.transform_name_for_sku(),
        )

    def test_transform_color_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(
            'BLACK',
            small_black_shoes.transform_color_for_sku(),
        )

    def test_generate_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(
            'SHOES-S-BLACK',
            small_black_shoes.generate_sku(),
        )

    









# class ShoppingCartTestCase(unittest.TestCase):
#     def test_cart_initially_empty(self):
#         cart = ShoppingCart()
#         self.assertDictEqual({}, cart.products)

#     def test_add_product(self):
#         cart = ShoppingCart()
#         product = Product('shoes', 'S', 'blue')

#         cart.add_product(product)

#         self.assertDictEqual({'SHOES-S-BLUE': {'quantity': 1}},
#                              cart.products)

#     def test_add_two_of_a_product(self):
#         cart = ShoppingCart()
#         product = Product('shoes', 'S', 'blue')

#         cart.add_product(product, quantity=2)

#         self.assertDictEqual({'SHOES-S-BLUE': {'quantity': 2}},
#                              cart.products)

#     def test_add_two_different_products(self):
#         cart = ShoppingCart()
#         product_one = Product('shoes', 'S', 'blue')
#         product_two = Product('shirt', 'M', 'gray')

#         cart.add_product(product_one)
#         cart.add_product(product_two)

#         self.assertDictEqual(
#             {
#                 'SHOES-S-BLUE': {'quantity': 1},
#                 'SHIRT-M-GRAY': {'quantity': 1}
#             },
#             cart.products
#         )

#     def test_add_and_remove_product(self):
#         cart = ShoppingCart()
#         product = Product('shoes', 'S', 'blue')

#         cart.add_product(product)
#         cart.remove_product(product)

#         self.assertDictEqual({}, cart.products)

#     def test_remove_too_many_products(self):
#         cart = ShoppingCart()
#         product = Product('shoes', 'S', 'blue')

#         cart.add_product(product)
#         cart.remove_product(product, quantity=2)

#         self.assertDictEqual({}, cart.products)
