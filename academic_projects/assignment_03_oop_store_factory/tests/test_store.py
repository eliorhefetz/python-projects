import unittest

from src.store import DiscountProduct, Product, Store


class TestStore(unittest.TestCase):
    def test_total_value_includes_discount_products(self):
        store = Store("My Shop", "Elior")
        store.AddProduct(Product("A", "Cable", "Electronics", 10), 3)
        store.AddProduct(DiscountProduct("B", "Screen", "Electronics", 100, 25), 2)

        self.assertEqual(store.TotalValue(), 180)

    def test_buy_returns_change_and_updates_quantity(self):
        store = Store("My Shop", "Elior")
        store.AddProduct(Product("A", "Cable", "Electronics", 10), 5)

        result = store.Buy("A", 2, 30)

        self.assertEqual(result, 10)
        self.assertEqual(store.products[0][1], 3)

    def test_get_discount_product_returns_names(self):
        store = Store("My Shop", "Elior")
        store.AddProduct(Product("A", "Cable", "Electronics", 10), 1)
        store.AddProduct(DiscountProduct("B", "Screen", "Electronics", 100, 25), 1)

        self.assertEqual(store.GetDiscountProduct(), ["Screen"])


if __name__ == "__main__":
    unittest.main()
