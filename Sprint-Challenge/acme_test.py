"""Acme Test."""

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!."""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight is 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability is 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


class AcmeReportTests(unittest.TestCase):
    """Test accuracy of AcmeReport Script."""

    def test_default_num_products(self):
        """Verify it actually returns 30."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Verify this returns valid names."""
        # Got stuck here!! TODO


if __name__ == '__main__':
    unittest.main()
